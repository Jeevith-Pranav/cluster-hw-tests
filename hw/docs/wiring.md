# Wiring
PCF8591 (powered from 3.3 V, never 5 V):
VCC -> Pi pin 1 | GND -> pin 6 | SDA -> pin 3 | SCL -> pin 5
AIN0 -> 25 V voltage module "S" | AIN1 -> fuel pot wiper
Voltage module: VCC terminal -> battery + | GND terminal -> battery - | "-" pin -> Pi GND
Remove the jumper caps on the PCF8591 board.