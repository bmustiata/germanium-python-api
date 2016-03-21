Feature: The S super locator, that returns deferred locators.

@1
Scenario: Find by inferred CSS locators.
    Given I open firefox
    When I go to 'http://localhost:8000/features/test-site/inputs.html'
    Then I type 'input test' into input
    Then the value for the input is 'input test'

@2
Scenario: Find by inferred XPath locators.
    Given I open firefox
    When I go to 'http://localhost:8000/features/test-site/inputs.html'
    Then I type 'input test' into //input
    Then the value for the //input is 'input test'

@3
Scenario: Find by inferred simple locators.
    Given I open firefox
    When I go to 'http://localhost:8000/features/test-site/inputs.html'
    Then I type 'input test' into simple:"Text input" > input
    Then the value for the simple:"Text input" > input is 'input test'

@4
Scenario: Find by javascript locators.
    Given I open firefox
    When I go to 'http://localhost:8000/features/test-site/inputs.html'
    Then I type 'input test' into js:return document.getElementById('textInput')
    Then the value for the #textInput is 'input test'

@5
Scenario: Finding elements that don't exist should not throw exceptions
    Given I open firefox
    When I go to 'http://localhost:8000/features/test-site/inputs.html'
    And I search using S for //does/not/exist
    And I search using S for div.what
    And I search using S for div["what"].what
    Then nothing happens

@6
Scenario: Element (not)exists(visible) should function.
    Given I open firefox
    When I go to 'http://localhost:8000/features/test-site/inputs.html'
    Then the selector '.textInput' exists somewhere
    And the selector '.textInput' exists and is visible
    And the selector '.displayHidden' exists somewhere
    And the selector '.displayHidden' doesn't exists as visible
    And the selector '.missingLocator' doesn't exists at all
    And the selector '.missingLocator' doesn't exists as visible

@7
Scenario: Calling S with an existing locator should return the existing locator.
    Given I open firefox
    When I go to 'http://localhost:8000/features/test-site/inputs.html'
    And I search using a nested locator for '#outsideTextFlowedInput'
    Then I find the element with id: 'outsideTextFlowedInput'

@8
Scenario: Calling S with a callable should invoke the callable, and re-eval S.
    Given I open firefox
    When I go to 'http://localhost:8000/features/test-site/inputs.html'
    And I search using a callable that returns a CssSelector '#outsideTextFlowedInput'
    Then I find the element with id: 'outsideTextFlowedInput'
