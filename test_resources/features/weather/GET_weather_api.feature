@test
Feature:Sample API Test


    @weather_api
   Scenario: Find Weather in London
    Given I am Sample Weather API user
    Then I want to call the weather api to know the current weather


