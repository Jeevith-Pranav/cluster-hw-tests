I2C_BUS = 1
PCF8591_ADDR = 0x48

CH_BATTERY = 0      # AIN0: battery voltage from the 25 V sensor module
CH_FUEL = 1         # AIN1: fuel potentiometer

VREF = 3.3          # measure the Pi 3.3 V pin with a multimeter and enter it
DIVIDER = 5.0       # 25 V module ratio; fix it with calibrate_battery.py

# (voltage, percent) for a resting LiFePO4 cell. APPROXIMATE, tune it later.
SOC_TABLE = [
    (2.80, 0), (3.00, 5), (3.20, 20), (3.25, 30),
    (3.30, 50), (3.32, 70), (3.35, 80), (3.40, 90), (3.50, 100),
]

LOW_WARN = 20       # amber at or below this percent
LOW_CRIT = 10       # red at or below this percent