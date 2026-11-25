import time
from hw.pcf8591 import Pcf8591

adc = Pcf8591()
print("Turn the potentiometer. Ctrl+C to stop.")
try:
    while True:
        vals = [adc.read_raw(ch) for ch in range(4)]
        print("AIN0 {:3d}   AIN1 {:3d}   AIN2 {:3d}   AIN3 {:3d}".format(*vals))
        time.sleep(0.3)
except KeyboardInterrupt:
    pass
finally:
    adc.close()