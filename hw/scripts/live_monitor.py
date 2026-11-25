import time
import config
from hw.pcf8591 import Pcf8591
from hw.battery import adc_to_volts, voltage_to_soc


class Smoother:
    def __init__(self, alpha):
        self.alpha, self.value = alpha, None

    def update(self, x):
        self.value = x if self.value is None else self.alpha * x + (1 - self.alpha) * self.value
        return self.value


def bar(percent, width=20):
    filled = round(width * percent / 100)
    return "█" * filled + "░" * (width - filled)


def level(percent):
    if percent <= config.LOW_CRIT:
        return "CRITICAL"
    if percent <= config.LOW_WARN:
        return "LOW"
    return "ok"


adc = Pcf8591()
volt_f, fuel_f = Smoother(0.1), Smoother(0.3)
print("Live monitor. Ctrl+C to stop.\n")
try:
    while True:
        volts = volt_f.update(adc_to_volts(adc.read_fraction(config.CH_BATTERY)))
        fuel = fuel_f.update(adc.read_fraction(config.CH_FUEL) * 100)
        soc = voltage_to_soc(volts)
        line = (f"Battery {volts:4.2f} V {soc:3.0f}% [{bar(soc)}] {level(soc):8s} | "
                f"Fuel {fuel:3.0f}% [{bar(fuel)}] {level(fuel):8s}")
        print("\r" + line, end="", flush=True)
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\nStopped.")
finally:
    adc.close()