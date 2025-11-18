Feature: ReqRes API Testing
  As a test engineer
  I want to test the ReqRes API endpoints
  So that I can verify API functionality

  Background:
    Given the API base URL is "https://reqres.in/api"

  @smoke @api
  Scenario: Get single user by ID
    When I send GET request to "/users/2"
    Then response status code should be 200
    And response should contain "data" field
    And response data should have "id" equal to 2
    And response data should have "email" field
    And response data should have "first_name" field

  @api @users
  Scenario: Get list of users
    When I send GET request to "/users?page=2"
    Then response status code should be 200
    And response should contain "data" field
    And response should contain "page" field
    And response data should have "page" equal to 2
    And response data should contain multiple users

  @api @create
  Scenario: Create new user successfully
    When I send POST request to "/users" with body:
      | name    | job       |
      | Anitha  | SDET      |
    Then response status code should be 201
    And response should contain "name" field
    And response should contain "job" field
    And response should contain "id" field
    And response should contain "createdAt" field

  @api @update
  Scenario: Update existing user
    When I send PUT request to "/users/2" with body:
      | name       | job              |
      | Anitha M   | Senior SDET      |
    Then response status code should be 200
    And response should contain "name" field
    And response should contain "job" field
    And response should contain "updatedAt" field

  @api @delete
  Scenario: Delete user
    When I send DELETE request to "/users/2"
    Then response status code should be 204

  @api @negative
  Scenario: Get non-existent user returns 404
    When I send GET request to "/users/999"
    Then response status code should be 404

  @api @register
  Scenario Outline: User registration with different data
    When I send POST request to "/register" with body:
      | email   | password   |
      | <email> | <password> |
    Then response status code should be <status>
    
    Examples:
      | email              | password | status |
      | eve.holt@reqres.in | pistol   | 200    |
      | invalid@test.com   | pass123  | 400    |