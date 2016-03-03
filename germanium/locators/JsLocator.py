from selenium.webdriver.remote.webelement import WebElement

from .DeferredLocator import DeferredLocator


class JsLocator(DeferredLocator):
    """
    A JS Deferred locator. This locator will execute some JavaScript
    code in order to find the elements.
    """
    def __init__(self, germanium, code):
        super(JsLocator, self).__init__(germanium)

        self._code = code

    def _find_element(self):
        """
        Find an element using the CSS locator provided at creation.
        """
        element = self._germanium.js(self._code)

        if not element:
            return element

        if not isinstance(element, WebElement):
            raise Exception("Code `%s` is not returning an element." % self._code)

        return element

    def _find_element_list(self):
        """
        Find an element using the CSS locator provided at creation.
        """
        result = self._germanium.js(self._code)

        if not result:
            return []

        for element in result:
            if not isinstance(element, WebElement):
                raise Exception("Code `%s` is not returning only elements, "
                                "is returning also: %s" % (self._code, element))

        return result
