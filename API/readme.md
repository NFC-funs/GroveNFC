# API first release: GroveNFC_API-20261001.zip
- This demo demonstrates reading/writing and emulating Tags via I2C.
- Core1 runs NFC functions; Core0 handles user interface such as I2C.
- USB for CDC and MSC: 

CDC emulates GroveNFC as PN532Killer-compatible device;

MSC emulates GroveNFC as USB drive to store Tag data, Amiibo data and Mifare1 dictionaries;

MSC ported from [https://github.com/oyama/pico-usb-flash-drive](https://github.com/oyama/pico-usb-flash-drive)

- The following functions are implemented based on this API.

Emulate various types of Mifare1 Tags;

All Mifare 1 attack types;

Mifare 1 local key recovery: mfkey32, mfkey64, StaticNested, dictionary;

Emulate Amiibo for unlimited usage;

# API & Secondary Development
- Purpose: For secondary development of the GroveNFC module itself (customize functionality, protocol, etc.)
- Based on: RP2040 C/C++ SDK v2.3.0

# API first release: GroveNFC_API-20260320.zip
- This is a demo program designed to demonstrate how to call relevant functions to implement NFC functionality.

# API & Secondary Development
- Purpose: For secondary development of the GroveNFC module itself (customize functionality, protocol, etc.)
- Based on: RP2040 C/C++ SDK v2.1.0
- Includes: Complete API documentation, static library, and development templates
