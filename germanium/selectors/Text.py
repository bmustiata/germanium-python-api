from .AbstractSelector import AbstractSelector


class Text(AbstractSelector):
    """
    Just a selector that finds the text in the page.
    """
    def __init__(self, text):
        super(AbstractSelector, self).__init__()
        self._text = text

    def get_selectors(self):
        """ Return the simple selector to find the text """
        simple_locator = """js:
            var searchedText = "%s";

            function text(node) {
                return node.innerText || node.textContent;
            }

            if (!text(document.body).contains(searchedText)) {
                return null;
            }

            var result = document.body;
            var foundChildElement = true;

            while (foundChildElement) {
                foundChildElement = false;

                for (var i = 0; i < result.children.length; i++) {
                    if (text(result.children[i]).contains(searchedText)) {
                        foundChildElement = true;
                        result = result.children[i];
                    }
                }
            }

            return result;
        """ % str(self._text).replace('"', '\\"', 100000)

        return [simple_locator]
