
class AbstractSelector(object):
    """
    Just a marker interface.
    """
    def __init__(self):
        pass


class Input(AbstractSelector):
    """
    Just a selector that finds an input by its name.
    """
    def __init__(self, input_name):
        self._input_name = input_name

    def get_selector(self):
        # CSS selector.
        return "input[name='%s']" % self._input_name


class Button(AbstractSelector):
    """
    Just a selector that finds a button by its label or name.
    """
    def __init__(self, label = None, name = None):
        self._label = label
        self._name = name

    def get_selector(self):
        """ Return the CSS selector to find the button. """
        button_selector = "button"
        input_selector = "input[type='button']"

        if self._name:
            button_selector += "[name='%s']" % self._name
            input_selector += "[name='%s']" % self._name

        if self._label:
            input_selector += "[value='%s']" % self._label

        return "%s,%s" % (input_selector, button_selector)

