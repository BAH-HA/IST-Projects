describe('Enrollment', () => {
	beforeEach(() => {
	  cy.deleteAllButArs();
	  cy.createDemoEnrollments();
	});

	afterEach(() => {
		cy.deleteAllButArs();
	  });

	it('create enrollments', () => {
		const MOTIVATION = 'enrollment motivation';

		cy.demoMemberLogin()

		cy.intercept('GET', '/users/*/getInstitution').as('getInstitutions');
		cy.intercept('GET', '/themes/availableThemes').as('availableTeams')
		cy.get('[data-cy="institution"]').click();
		cy.get('[data-cy="activities"]').click();
		cy.wait('@getInstitutions');
		cy.wait('@availableTeams');
		// check if activity table has 3 instances and 13 columns
		cy.get('[data-cy="memberActivitiesTable"] tbody tr')
			.should('have.length', 3)
			.eq(0)
			.children()
			.should('have.length', 13)
		// check if first activity has 0 applications
		cy.get('[data-cy="memberActivitiesTable"] tbody tr')
		.eq(0).children().eq(3).should('contain', '0');
		cy.logout();

		cy.demoVolunteerLogin();
		cy.intercept('POST', '/activities/*/enrollments', (req) => {
		}).as('registerEnrollment');
		cy.intercept('GET', '/activities').as('getActivities');
		cy.intercept('GET', '/enrollments/volunteer').as('getVolunteerEnrollments');
		cy.get('[data-cy="volunteerActivities"]').click();
		cy.wait('@getActivities');
		cy.wait('@getVolunteerEnrollments');
		// enroll in activity
		cy.get('[data-cy="applyForActivity"]').click();
		cy.get('[data-cy="motivationInput"]').type(MOTIVATION);
		cy.get('[data-cy="saveEnrollment"]').click();
		cy.wait('@registerEnrollment')
		cy.logout();

		cy.demoMemberLogin();
		cy.intercept('GET', '/users/*/getInstitution').as('getInstitutions');
		cy.intercept('GET', '/themes/availableThemes').as('availableTeams')
		cy.intercept('GET', '/activities/*/enrollments').as('getActivitiesEnrollments')
		cy.get('[data-cy="institution"]').click();
		cy.get('[data-cy="activities"]').click();
		cy.wait('@getInstitutions');
		cy.wait('@availableTeams');
		// check if first activity has 1 application
		cy.get('[data-cy="memberActivitiesTable"] tbody tr')
			.eq(0).children().eq(3).should('contain', '1');
		// select show enrollments for first activity in the table
		cy.get('[data-cy="showEnrollments"] ').eq(0).click()
		cy.wait('@getActivitiesEnrollments');
		// check if enrollment table for activity has 1 instance
		cy.get('[data-cy="activityEnrollmentsTable"] tbody tr')
			.should('have.length', 1)
		// check if first enrollment has motivation column equal to assigned motivation
		cy.get('[data-cy="activityEnrollmentsTable"] tbody tr')
			.eq(0).children().eq(1).should('contain', 'enrollment motivation')
		});
});
