describe('Assessment', () => {
    beforeEach(() => {
        cy.deleteAllButArs();
        cy.createDemoAssessments();
    });

    afterEach(() => {
        cy.deleteAllButArs();
    });

    it('create assessments', () => {
        const ACTIVITY_NAME = 'A1';
        const REVIEW = 'review 123';

        cy.demoVolunteerLogin()
        // intercept create assessment request
        cy.intercept('POST', '/institutions/*/assessments').as('writeAssessment');
        // confirm activities table has 6 activities
        cy.intercept('GET', '/activities').as('getActivities');
        cy.get('[data-cy="volunteerActivities"]').click();
        cy.wait('@getActivities');
        cy.get('[data-cy="volunteerActivitiesTable"] tbody tr')
            .should('have.length', 6)
            .eq(0)
            .children()
            .should('have.length', 10)
        // confirm first activity has 'A1' has name
        cy.get('[data-cy="volunteerActivitiesTable"] tbody tr')
            .eq(0).children().eq(0).should('contain', ACTIVITY_NAME)
        // go to create assessment form
        cy.get('[data-cy="writeAssessmentButton"]').eq(0).click();
        // fill form
        cy.get('[data-cy="reviewInput"]').type(REVIEW);
        // save form
        cy.get('[data-cy="makeAssessment"]').click()
        // check request was done
        cy.wait('@writeAssessment')
        cy.logout();

        cy.demoMemberLogin()
        // confirm assessments table has 1 assessment
        cy.get('[data-cy="institution"]').click();
        cy.get('[data-cy="assessments"]').click();
        cy.get('[data-cy="institutionAssessmentsTable"] tbody tr')
            .should('have.length', 1)
        // check results
        cy.get('[data-cy="institutionAssessmentsTable"] tbody tr')
            .eq(0).children().eq(0).should('contain', REVIEW)
        cy.logout();
    });
});

