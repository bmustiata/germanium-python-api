Feature: Germanium wait utility function.
  When waiting for things, we generally wait for an element
  to appear. Unfortunately in many cases what might happen
  is that an error will occur, and our wait will be stuck
  in the waiting until the timeout occurs.

  Thus Germanium provides a wait that can be shortcircuited
  by error conditions, specified via its `while_not`
  attribute.

Scenario: Test simple wait
  Given I open firefox
  When I go to 'http://localhost:8000/features/test-site/wait-error.html'
  Then waiting for error to happen should pass

Scenario: Test simple while_not callback
  Given I open firefox
  When I go to 'http://localhost:8000/features/test-site/wait-error.html'
  Then waiting for success to happen should fail

Scenario: Test multiple wait callback as array
  Given I open firefox
  When I go to 'http://localhost:8000/features/test-site/wait-error.html'
  Then waiting for error or success to happen should pass with array callbacks

Scenario: Test multiple wait callback as vararg
  Given I open firefox
  When I go to 'http://localhost:8000/features/test-site/wait-error.html'
  Then waiting for error or success to happen should pass with multiarg callbacks
