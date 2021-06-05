from komand import helper


def remove_null_and_clean(in_list):
    output = []

    for item in in_list:
        dict_ = item
        for key in list(dict_.keys()):
            if dict_[key] is None:
                dict_.pop(key)
        output.append(helper.clean(dict_))
    return output
