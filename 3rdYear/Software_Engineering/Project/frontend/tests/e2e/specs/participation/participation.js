describe('Participation', () => {
  beforeEach(() => {
    cy.deleteAllButArs();
    cy.createDemoParticipations();
  });

  afterEach(() => {
    cy.deleteAllButArs();
  });

  it('create participations', () => {

    cy.demoMemberLogin()

    cy.intercept('POST', '/activities/*/participations').as('createParticipation');

    cy.intercept('GET', '/users/*/getInstitution').as('getInstitutions');
    cy.intercept('GET', '/themes/availableThemes').as('availableTHEMES');
    cy.intercept('GET', '/activities/*/enrollments').as('getEnrollments');

    // verificar que a tabela de atividades tem 2 instâncias
    cy.get('[data-cy="institution"]').click();

    cy.get('[data-cy="activities"]').click();
    cy.wait('@getInstitutions');

    cy.get('[data-cy="memberActivitiesTable"] tbody tr')
        .should('have.length', 2)
        .eq(0)
        .children()
        .should('have.length', 13)

    // verificar que a primeira atividade da tabela tem 1 participação (1 entrada com participating a true)
    cy.get('[data-cy="memberActivitiesTable"] tbody tr')
        .eq(1).children().eq(4).should('contain', '1')

    // selecionar Show Enrollments da primeira atividade da tabela
    cy.get('[data-cy="showEnrollments"] ').eq(0).click()
    cy.wait('@availableTHEMES');
    cy.wait('@getEnrollments');

    // verificar que a tabela dos enrollments da atividade tem 2 instâncias
    cy.get('[data-cy="activityEnrollmentsTable"] tbody tr')
        .should('have.length', 2)
        .eq(0)
        .children()
        .should('have.length', 5)

    // verificar que o primeiro enrollment da tabela tem a coluna Participating como false
    cy.get('[data-cy="activityEnrollmentsTable"] tbody tr')
        .eq(0).children().eq(2).should('contain', 'false')

    // criar uma participação para esse enrollment
    cy.get('[data-cy="activityEnrollmentsTable"] tbody tr').eq(0).click();

    cy.get('[data-cy="selectParticipant"]').click();
    // fill form
    cy.get('[data-cy="ratingInput"]').type('3');
    // save form
    cy.get('[data-cy="makeParticipant"]').click()
    cy.wait('@createParticipation')

    // verificar que o primeiro enrollment que passou a ter participação tem a coluna Participating como true
    cy.get('[data-cy="activityEnrollmentsTable"] tbody tr')
        .eq(0).children().eq(2).should('contain', 'true')

    // voltar à tabela de atividades e verificar que a atividade passou a ter 2 participações
    cy.get('[data-cy="institution"]').click();
    cy.get('[data-cy="activities"]').click();
    cy.wait('@getInstitutions');

    cy.get('[data-cy="memberActivitiesTable"] tbody tr')
        .eq(0).children().eq(4).should('contain', '2')
    cy.logout();
  });
});

