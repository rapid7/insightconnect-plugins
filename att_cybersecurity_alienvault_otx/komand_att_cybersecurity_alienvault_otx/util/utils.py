import IndicatorTypes


indicator_types = {
    "IPv4": IndicatorTypes.IPv4,
    "IPv6": IndicatorTypes.IPv6,
    "URL": IndicatorTypes.URL,
    "HOSTNAME": IndicatorTypes.HOSTNAME
}


def get_indicatortypes(indicator_type):
    if indicator_type not in indicator_types:
        raise Exception(f"Indicator type: {indicator_type} is not a supported indicator type")
    return indicator_types.get(indicator_type)
