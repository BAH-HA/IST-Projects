<template>
  <div>
    <v-card class="table">
      <v-data-table
        :headers="headers"
        :items="activities"
        :search="search"
        disable-pagination
        :hide-default-footer="true"
        :mobile-breakpoint="0"
        data-cy="volunteerActivitiesTable"
      >
        <template v-slot:top>
          <v-card-title>
            <v-text-field
              v-model="search"
              append-icon="search"
              label="Search"
              class="mx-2"
            />
            <v-spacer />
          </v-card-title>
        </template>
        <template v-slot:[`item.themes`]="{ item }">
          <v-chip v-for="theme in item.themes" v-bind:key="theme.id">
            {{ theme.completeName }}
          </v-chip>
        </template>
        <template v-slot:[`item.action`]="{ item }">
          <v-tooltip v-if="item.state === 'APPROVED'" bottom>
            <template v-slot:activator="{ on }">
              <v-icon
                class="mr-2 action-button"
                color="red"
                v-on="on"
                data-cy="reportButton"
                @click="reportActivity(item)"
                >warning</v-icon
              >
            </template>
            <span>Report Activity</span>
          </v-tooltip>
          <v-tooltip
            v-if="
              verifyDateCondition(item.applicationDeadline) &&
              verifyEnrollmentCondition(item.id)
            "
            bottom
          >
            <template v-slot:activator="{ on }">
              <v-icon
                class="mr-2 action-button"
                @click="applyForActivity(item)"
                v-on="on"
                data-cy="applyForActivity"
                color="blue"
                >fas fa-sign-in-alt
              </v-icon>
            </template>
            <span>Apply for Activity</span>
          </v-tooltip>
          <v-tooltip v-if="checkConditions(item)" bottom>
            <template v-slot:activator="{ on }">
              <v-icon
                class="mr-2 action-button"
                color="blue"
                v-on="on"
                data-cy="writeAssessmentButton"
                @click="writeAssessment(item)"
                >fa-solid fa-pen-to-square
              </v-icon>
            </template>
            <span>Create Assessment</span>
          </v-tooltip>
        </template>
      </v-data-table>
      <assessment-dialog
        v-if="currentAssessment && editAssessmentDialog"
        v-model="editAssessmentDialog"
        :assessment="currentAssessment"
        v-on:save-assessment="onSaveAssessment"
        v-on:close-assessment-dialog="onCloseAssessmentDialog"
      />
      <enrollment-dialog
        v-if="currentActivityId && currentEnrollment && enrollmentDialog"
        v-model="enrollmentDialog"
        :enrollment="currentEnrollment"
        :activityId="currentActivityId"
        v-on:save-enrollment="onSaveEnrollment"
        v-on:close-enrollment="onCloseEnrollment"
      />
    </v-card>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import RemoteServices from '@/services/RemoteServices';
import Activity from '@/models/activity/Activity';
import Enrollment from '@/models/enrollment/Enrollment';
import EnrollmentDialog from '@/views/volunteer/EnrollmentDialog.vue';
import { show } from 'cli-cursor';
import Assessment from '@/models/assessment/Assessment';
import AssessmentDialog from '@/views/volunteer/AssessmentDialog.vue';
import Participation from '@/models/participation/Participation';

@Component({
  components: {
    'assessment-dialog': AssessmentDialog,
    'enrollment-dialog': EnrollmentDialog,
  },
  methods: { show },
})
export default class VolunteerActivitiesView extends Vue {
  activities: Activity[] = [];
  volunteerAssessments: Assessment[] = [];
  volunteerParticipations: Participation[] = [];

  currentAssessment: Assessment | null = null;
  editAssessmentDialog: boolean = false;

  search: string = '';

  currentActivityId: number | null = null;
  currentEnrollment: Enrollment | null = null;
  enrollmentDialog: boolean = false;
  volunteerEnrollments: Enrollment[] = [];

  headers: object = [
    {
      text: 'Name',
      value: 'name',
      align: 'left',
      width: '5%',
    },
    {
      text: 'Region',
      value: 'region',
      align: 'left',
      width: '5%',
    },
    {
      text: 'Participants Limit',
      value: 'participantsNumberLimit',
      align: 'left',
      width: '5%',
    },
    {
      text: 'Themes',
      value: 'themes',
      align: 'left',
      width: '5%',
    },
    {
      text: 'Description',
      value: 'description',
      align: 'left',
      width: '30%',
    },
    {
      text: 'State',
      value: 'state',
      align: 'left',
      width: '5%',
    },
    {
      text: 'Start Date',
      value: 'formattedStartingDate',
      align: 'left',
      width: '5%',
    },
    {
      text: 'End Date',
      value: 'formattedEndingDate',
      align: 'left',
      width: '5%',
    },
    {
      text: 'Application Deadline',
      value: 'formattedApplicationDeadline',
      align: 'left',
      width: '5%',
    },
    {
      text: 'Actions',
      value: 'action',
      align: 'left',
      sortable: false,
      width: '5%',
    },
  ];

  async created() {
    await this.$store.dispatch('loading');
    try {
      this.activities = await RemoteServices.getActivities();
      this.volunteerAssessments = await RemoteServices.getVolunteerAssessments(
        this.$store.getters.getUser.id,
      );
      this.volunteerParticipations = await RemoteServices.getVolunteerParticipations(this.$store.getters.getUser.id);

      this.volunteerEnrollments =
        await RemoteServices.getVolunteerEnrollments();
    } catch (error) {
      await this.$store.dispatch('error', error);
    }

    await this.$store.dispatch('clearLoading');
  }

  writeAssessment(activity: Activity){
    this.currentAssessment = new Assessment();
    this.currentAssessment.institutionId = activity.institution.id;
    this.editAssessmentDialog = true;
  }

  onCloseAssessmentDialog(){
    this.currentAssessment = null;
    this.editAssessmentDialog = false;
  }

  async onSaveAssessment(assessment: Assessment) {
    this.volunteerAssessments.unshift(assessment);
    this.editAssessmentDialog = false;
    this.currentAssessment = null;
  }

  checkConditions(activity: Activity) {

    if (new Date(activity.endingDate) < new Date() && !this.checkDup(activity) && this.hasParticipation(activity)){
      return true;
    }

    return false;
  }

  checkDup(activity: Activity){
    return this.volunteerAssessments.some((assessment) =>
        assessment.institutionId === activity.institution.id
    )
  }

  hasParticipation(activity: Activity){
    return this.volunteerParticipations.some((participation) =>
        participation.activityId === activity.id
    )
  }

  applyForActivity(activity: Activity) {
    this.currentActivityId = activity.id;
    this.currentEnrollment = new Enrollment();
    this.enrollmentDialog = true;
  }

  verifyDateCondition(activityApplicationDeadline: string) {
    return new Date() < new Date(activityApplicationDeadline);
  }
  verifyEnrollmentCondition(activityId: number) {
    return !this.volunteerEnrollments.some(
      (enrollment) => enrollment.enrollmentActivityId === activityId,
    );
  }

  async reportActivity(activity: Activity) {
    if (activity.id !== null) {
      try {
        const result = await RemoteServices.reportActivity(
          this.$store.getters.getUser.id,
          activity.id,
        );
        this.activities = this.activities.filter((a) => a.id !== activity.id);
        this.activities.unshift(result);
      } catch (error) {
        await this.$store.dispatch('error', error);
      }
    }
  }

  async onSaveEnrollment(enrollment: Enrollment) {
    this.volunteerEnrollments.unshift(enrollment);
    this.currentEnrollment = null;
    this.enrollmentDialog = false;
    this.currentActivityId = null;
  }

  onCloseEnrollment() {
    this.currentEnrollment = null;
    this.enrollmentDialog = false;
    this.currentActivityId = null;
  }
}
</script>

<style lang="scss" scoped></style>