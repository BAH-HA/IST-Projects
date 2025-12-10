import { ISOtoString } from '@/services/ConvertDateService';

export default class Enrollment {
  id: number | null = null;
  motivation!: string;
  enrollmentDateTime!: string;
  name!: string;
  participating!: boolean;
  rating!: number | null;
  enrollmentVolunteerId!: number | null;
  enrollmentActivityId!: number | null;

  constructor(jsonObj?: Enrollment) {
    if (jsonObj) {
      this.id = jsonObj.id;
      this.motivation = jsonObj.motivation;
      this.enrollmentDateTime = ISOtoString(jsonObj.enrollmentDateTime);
      this.name = jsonObj.name;
      this.participating = jsonObj.participating;
      this.rating = jsonObj.rating;
      this.enrollmentVolunteerId = jsonObj.enrollmentVolunteerId;
      this.enrollmentActivityId = jsonObj.enrollmentActivityId;
    }
  }
}
