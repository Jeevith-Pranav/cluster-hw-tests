import time
import config
from hw.pcf8591 import Pcf8591
from hw.battery import adc_to_volts

adc = Pcf8591()
time.sleep(0.5)
fractions = [adc.read_fraction(config.CH_BATTERY, samples=8) for _ in range(20)]
frac = sum(fractions) / len(fractions)
computed = adc_to_volts(frac)

print(f"Computed battery voltage: {computed:.3f} V")
measured = float(input("Type the voltage your multimeter shows (e.g. 3.28): "))
suggested = config.DIVIDER * measured / computed
print(f"\nSet this in config.py:  DIVIDER = {suggested:.3f}")
adc.close()