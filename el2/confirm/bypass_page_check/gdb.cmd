set architecture aarch64
target remote :1234
b * 0xFFFFFFFFC0000030
c
b * 0x40100240
c
x /10gx 0x40107000
si
x /10gx 0x40107000