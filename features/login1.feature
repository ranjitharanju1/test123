Feature: Swaglabs text

  Scenario:Swaglabs text presence on Saucedemo home page
    Given I launch the browser
    When open Saucedemo home page
    Then I verify that the SwagLabs text present on page
    And I close the browser


  Scenario:Login with valid credentials
    Given I launch the browser
    When open Saucedemo home page
    Then I verify that the SwagLabs text present on page
    And Enter username "standard_user" and password "secret_sauce"
    And Click on login button
    Then user must successfully login to the product pageAnd I close the browser
    And I close the browser


Scenario: Add to cart product
    Given I launch the browser
    When open Saucedemo home page
    Then I verify that the SwagLabs text present on page
    And Enter username "standard_user" and password "secret_sauce"
    And Click on login button
    Then user must successfully login to the product pageAnd I close the browser
    And click on add to cart button for selected product
    And click on cart icon
    Then product should be visible in the your cart page

   @start
Scenario: Add to cart product
    Given I launch the browser
    When open Saucedemo home page
    Then I verify that the SwagLabs text present on page
    And Enter username "standard_user" and password "secret_sauce"
    And Click on login button
    Then user must successfully login to the product pageAnd I close the browser
    And click on add to cart button for selected product
    And click on cart icon
    Then product should be visible in the your cart page
    And click on the checkout button
    Then user should be navigated to checkout your information page
    And enter firstname "ranjitha" and lastname "b" and postalcode "577301"
    And click on continue button
    Then user should be navigated to checkout overview page
    And click on finish button
    Then user must navigated to checkout complete page
    And click on backhome button
    Then user must navigated to the product page
    And I close the browser