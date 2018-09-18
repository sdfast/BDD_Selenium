Feature: Test navigation between pages
  We can have a longer description
  That can span a few lines


  Scenario: Homepage can go to the Blog
    Given I am on the homepage
    When I click on the link id "blog-link"
    Then I am on the blog page

  Scenario: Homepage can go to the Homepage
    Given I am on the blog
    When I click on the link id "home-link"
    Then I am on the home page