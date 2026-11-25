import config


def adc_to_volts(fraction):
    return fraction * config.VREF * config.DIVIDER


def voltage_to_soc(v):
    table = config.SOC_TABLE
    if v <= table[0][0]:
        return 0.0
    if v >= table[-1][0]:
        return 100.0
    for (v0, s0), (v1, s1) in zip(table, table[1:]):
        if v0 <= v <= v1:
            return s0 + (s1 - s0) * (v - v0) / (v1 - v0)
    return 0.0