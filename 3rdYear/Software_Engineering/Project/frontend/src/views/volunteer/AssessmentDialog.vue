<template>
  <v-dialog v-model="dialog" persistent width="1300">
    <v-card>
      <v-card-title>
        <span class="headline">
          {{ 'Write Assessment' }}
        </span>
      </v-card-title>
      <v-card-text>
        <v-form ref="form" lazy-validation>
          <v-row>
            <v-col cols="12" sm="6" md="4">
              <v-text-field
                  label="*Review"
                  :rules="[
                  (v) =>
                    isReviewValid(v) ||
                    'Review must be atleast 10 characteres',
                ]"
                  required
                  v-model="createAssessment.review"
                  data-cy="reviewInput"
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
            @click="$emit('close-assessment-dialog')"
        >
          Close
        </v-btn>
        <v-btn
            v-if="showSave"
            color="blue-darken-1"
            variant="text"
            @click="makeAssessment"
            data-cy="makeAssessment"
        >
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script lang="ts">
import { Vue, Component, Prop, Model } from 'vue-property-decorator';
import Assessment from '@/models/assessment/Assessment';
import RemoteServices from '@/services/RemoteServices';
import VueCtkDateTimePicker from 'vue-ctk-date-time-picker';
import 'vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css';
import { ISOtoString } from '@/services/ConvertDateService';

Vue.component('VueCtkDateTimePicker', VueCtkDateTimePicker);
@Component({
  methods: { ISOtoString },
})
export default class AssessmentDialog extends Vue {
  @Model('dialog', Boolean) dialog!: boolean;
  @Prop({ type: Assessment, required: true }) readonly assessment!: Assessment;

  createAssessment: Assessment = new Assessment();
  cypressCondition: boolean = false;
  showSave: boolean = false;

  async created() {
    this.createAssessment = new Assessment(this.assessment);
    this.createAssessment.reviewDate = (new Date()).toString();
  }

  isReviewValid(value: String) {
    if (value != null && value.length >= 10){
      this.showSave = true;
      return true;
    }
    this.showSave = false;
    return false
  }

  get canSave(): boolean {
    return (
        this.cypressCondition ||
        (!!this.createAssessment.review &&
            !!this.createAssessment.reviewDate)
    );
  }

  async makeAssessment() {
    const inst = this.assessment.institutionId;
    this.createAssessment.institutionId = inst;
    if ((this.$refs.form as Vue & { validate: () => boolean }).validate()) {
      try {
        const result =
            await RemoteServices.createAssessment(
                this.$store.getters.getUser.id,
                inst,
                this.createAssessment,
            );

        this.$emit('save-assessment', result);
      } catch (error) {
        await this.$store.dispatch('error', error);
      }
    }
  }
}
</script>

<style scoped lang="scss"></style>