def clean_ax_response(a: dict) -> dict:
    """
    Remove null values from the action set
    :param a:
    :return:
    """
    return dict(filter(lambda k: k[1] is not None, a.items()))

