# GroveNFC
A full-featured NFC reader/writer & emulator supporting ISO14443A, ISO14443B, ISO15693, and FeliCa protocols.

# Core Functionality
- Tag reading/writing and tag emulation
- Supported interfaces: I2C, UART, USB

# Development Features
- Static libraries enable independent development for standalone product deployment
- Based on Raspberry Pi Pico / RP2040 C/C++ SDK v2.1.0

# Compatible Host Hardware
GroveNFC works as a peripheral module, and is compatible with most 3.3V/5V embedded hosts with standard Grove or Gravity interface:
- M5Stack Cardputer ADV
- M5Stack Core / Core2 / Atom series
- Seeed Studio XIAO RP2040
- Seeed Studio Wio Terminal
- Raspberry Pi Pico (with Grove/Gravity base hat)
- Raspberry Pi 4 / 5 / Zero
- DFRobot FireBeetle 2 (ESP32 / RP2040)
- Arduino Uno / Nano / ESP32 boards (with Grove/Gravity shield)
- micro:bit V1/V2 (with Grove/Gravity extension)
- All other hosts with standard Grove or Gravity I2C/UART port

# Electrical Characteristics
- Logic level for SDA, SCL, TXD, RXD: 3.3V

