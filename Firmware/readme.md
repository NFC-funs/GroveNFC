# 20261001:
1. Added 9632 LCD UI. Supports Chinese character display.
2. UI, I2C and USB can run independently.
3. Add file system, 128K for file storage
4. Added Amiibo emulation
5. Added various Mifare1 attack methods:
- Nested
- StaticNested, key recovery time: 2~110s (max)
- Hardnested, Collect ~100 nonces per second
- Darkside, ~10+ seconds
- Mfkey32, Key recovery time is only ~1/5 of Flipper Zero(For the same dataset, FlipperZero takes ~100s while GroveNFC only 19s.)
- Mfkey64, key recovery time: 2~110s
- Standard Dictionary, 512 keys(KEYA) time: 3.05 seconds

# 20260627:
1. I2C: Read/Write ISO14443A/B, ISO15693, FeliCa; Emulate Mifare1, NTAG21x, ISO15693, ISO14443B
2. UART: Compatible with PN532 & PN532Killer
