import xed
print(xed.dis32([0,0]))
print(xed.dis64([0x48,0,0]))
print(xed.dis32([0x67, 0x8b, 0x46, 0xff]))
print(xed.dis32([0x75, 0x10]))
print(xed.dis64([0x75, 0x10], 0xaaaabbbffff0000))
