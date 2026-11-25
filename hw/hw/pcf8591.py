from smbus2 import SMBus
import config


class Pcf8591:
    def __init__(self, bus=config.I2C_BUS, address=config.PCF8591_ADDR):
        self._bus = SMBus(bus)
        self._addr = address

    def read_raw(self, channel):
        """One reading, 0 to 255."""
        self._bus.write_byte(self._addr, 0x40 | channel)
        self._bus.read_byte(self._addr)          # first byte is old data, discard
        return self._bus.read_byte(self._addr)

    def read_fraction(self, channel, samples=8):
        """Average of several readings, 0.0 to 1.0 (less noise)."""
        total = sum(self.read_raw(channel) for _ in range(samples))
        return total / samples / 255.0

    def close(self):
        self._bus.close()