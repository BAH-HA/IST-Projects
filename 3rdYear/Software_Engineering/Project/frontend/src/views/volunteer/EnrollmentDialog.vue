<template>
  <v-dialog v-model="dialog" persistent width="1300">
    <v-card>
      <v-card-title>
        <span class="headline">
          {{ 'New Application' }}
        </span>
      </v-card-title>
      <v-card-text>
        <v-form ref="form" lazy-validation>
          <v-row>
            <v-col cols="12">
              <v-text-field
                label="*Motivation"
                :rules="[
                  (v) => (v && v.length >= 10) || 'Motivation is required',
                ]"
                required
                v-model="editEnrollment.motivation"
                data-cy="motivationInput"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="blue-darken-1"
          variant="text"
          @click="$emit('close-enrollment')"
        >
          Close
        </v-btn>
        <v-btn
          v-if="isMotivationValid(editEnrollment.motivation)"
          color="blue-darken-1"
          variant="text"
          @click="applyForActivity"
          data-cy="saveEnrollment"
        >
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script lang="ts">
import { Vue, Component, Prop, Model } from 'vue-property-decorator';
import Enrollment from '@/models/enrollment/Enrollment';
import RemoteServices from '@/services/RemoteServices';
import { ISOtoString } from '@/services/ConvertDateService';
@Component({
  methods: { ISOtoString },
})
export default class EnrollmentDialog extends Vue {
  @Model('dialog', Boolean) dialog!: boolean;
  @Prop({ type: Enrollment, required: true }) readonly enrollment!: Enrollment;
  @Prop({ type: Number, required: true }) readonly activityId!: number;

  editEnrollment: Enrollment = new Enrollment();
  editActivityId: number = 0;

  cypressCondition: boolean = false;

  async created() {
    this.editEnrollment = new Enrollment(this.enrollment);
    this.editActivityId = this.activityId;
  }
  isMotivationValid(value: any) {
    return value && value.trim().length >= 10;
  }
  get canSave(): boolean {
    return (
      this.cypressCondition ||
      (!!this.editEnrollment.motivation &&
        !!this.editEnrollment.enrollmentDateTime &&
        !!this.editEnrollment.enrollmentActivityId)
    );
  }

  async applyForActivity() {
    if ((this.$refs.form as Vue & { validate: () => boolean }).validate()) {
      try {
        const result = await RemoteServices.createEnrollment(
          this.$store.getters.getUser.id,
          this.editActivityId,
          this.editEnrollment,
        );
        this.$emit('save-enrollment', result);
      } catch (error) {
        console.log(error);
        await this.$store.dispatch('error', error);
      }
    }
  }
}
</script>

<style scoped lang="scss"></style>
