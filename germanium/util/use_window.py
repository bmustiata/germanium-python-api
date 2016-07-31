from .find_germanium_object import find_germanium_object


def use_window_g(context,
                 title=None,
                 index=None,
                 id=None,
                 *args,
                 **kw):
    """

    :param context:
    :param title:
    :param index:
    :param id:
    :return:
    """
    germanium = find_germanium_object(context)

    if index is not None:
        window_handle = germanium.web_driver.window_handles[index]
        germanium.switch_to.window(window_handle)

        return

    if id is not None:
        germanium.switch_to.window(id)

        return

    if title is not None:
        found_titles = []

        for window_handle in germanium.web_driver.window_handles:
            germanium.switch_to.window(window_handle)
            page_title = germanium.title
            if page_title == title:
                return

            found_titles.append(page_title)

        raise Exception("Unable to find a Window with title `%s` in the list of windows: %s.",
                        title,
                        ", ".join(map(lambda x: '`%s`' % x, found_titles)))

    raise Exception("When using a window, you need to either specify its `title`, either "
                    "its `id` that you can obtain from the `germanium.window_handles`, or the "
                    "index from the `germanium.window_handles`.")
