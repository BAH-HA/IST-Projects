package pt.ulisboa.tecnico.socialsoftware.humanaethica.enrollment.dto;

import pt.ulisboa.tecnico.socialsoftware.humanaethica.enrollment.domain.Enrollment;
import pt.ulisboa.tecnico.socialsoftware.humanaethica.utils.DateHandler;

public class EnrollmentDto {
    private Integer id;
    private String motivation;
    private String name;
    private String enrollmentDateTime;
    private boolean isParticipating;
	private Integer enrollmentActivityId;

    private Integer enrollmentVolunteerId;

    public EnrollmentDto() {}

    public EnrollmentDto(Enrollment enrollment) {
        this.id = enrollment.getId();
        this.motivation = enrollment.getMotivation();
        this.enrollmentDateTime = DateHandler.toISOString(enrollment.getEnrollmentDateTime());
		this.enrollmentActivityId = enrollment.getActivity().getId();
        this.name = enrollment.getVolunteer().getName();
        this.isParticipating = enrollment.isParticipating();
        this.enrollmentVolunteerId = enrollment.getVolunteer().getId();
    }
    public boolean isParticipating() {
        return isParticipating;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getMotivation() {
        return motivation;
    }

    public void setMotivation(String motivation) {
        this.motivation = motivation;
    }

    public String getEnrollmentDateTime() {
        return enrollmentDateTime;
    }

    public void setEnrollmentDateTime(String enrollmentDateTime) {
        this.enrollmentDateTime = enrollmentDateTime;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

	public Integer getEnrollmentActivityId() {
		return enrollmentActivityId;
	}

	public void setEnrollmentActivityId(Integer enrollmentActivityId) {
		this.enrollmentActivityId = enrollmentActivityId;
	}

	public Integer getEnrollmentVolunteerId() {
		return enrollmentVolunteerId;
	}

	public void setEnrollmentVolunteerId(Integer enrollmentVolunteerId) {
		this.enrollmentVolunteerId = enrollmentVolunteerId;
	}

}
