<template>
  <v-dialog v-model="dialog" persistent width="1300">
    <v-card>
      <v-card-title>
        <span class="headline">
          {{ 'Select Participant' }}
        </span>
      </v-card-title>
      <v-card-text>
        <v-form ref="form" lazy-validation>
          <v-row>
            <v-col cols="12">
              <v-text-field
                label="Rating"
                :rules="[isNumberValid]"
                op
                v-model="enrollment.rating"
                data-cy="ratingInput"
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
          @click="$emit('close-participation-dialog')"
        >
          Close
        </v-btn>
        <v-btn
          color="blue-darken-1"
          variant="text"
          @click="makeParticipant"
          data-cy="makeParticipant"
        >
          Make Participant
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script lang="ts">
import { Vue, Component, Prop, Model } from 'vue-property-decorator';
import RemoteServices from '@/services/RemoteServices';
import { ISOtoString } from '@/services/ConvertDateService';
import Enrollment from '@/models/enrollment/Enrollment';
import Activity from '@/models/activity/Activity';

@Component({
  methods: { ISOtoString },
})
export default class ParticipationSelectionDialog extends Vue {
  @Model('dialog', Boolean) dialog!: boolean;
  @Prop({ type: Enrollment, required: true }) readonly enrollment!: Enrollment;
  @Prop({ type: Activity, required: true }) readonly activity!: Activity;

  cypressCondition: boolean = false;

  isNumberValid(value: any) {
    if (value && (isNaN(value) || value < 1 || value > 5)) {
      return 'Rating must be a number between 1 and 5';
    }
  }

  get canSave(): boolean {
    return (
      this.cypressCondition ||
      (!!this.enrollment.name &&
        !!this.enrollment.participating &&
        !!this.enrollment.rating &&
        !!this.enrollment.motivation &&
        !!this.enrollment.enrollmentDateTime)
    );
  }

  async makeParticipant() {
    if ((this.$refs.form as Vue & { validate: () => boolean }).validate()) {
      try {
        await RemoteServices.createParticipation(this.activity.id, {
          rating: this.enrollment.rating,
          activityId: this.activity.id,
          volunteerId: this.enrollment.enrollmentVolunteerId,
        });
        this.$emit('save-participation', this.enrollment);
      } catch (error) {
        console.log(error);
        await this.$store.dispatch('error', 'Error creating participation');
      }
    }
  }
}
</script>

<style scoped lang="scss"></style>
