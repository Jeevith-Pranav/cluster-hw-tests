from smbus2 import SMBus
import config

found = []
with SMBus(config.I2C_BUS) as bus:
    for addr in range(0x03, 0x78):
        try:
            bus.read_byte(addr)
            found.append(addr)
        except OSError:
            pass

if found:
    print("I2C devices found:", ", ".join(hex(a) for a in found))
    if config.PCF8591_ADDR in found:
        print("PCF8591 found. Good.")
    else:
        print("PCF8591 NOT found at", hex(config.PCF8591_ADDR))
else:
    print("No I2C devices found. Check wiring and that I2C is enabled.")