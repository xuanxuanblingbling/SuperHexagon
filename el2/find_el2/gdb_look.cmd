set architecture aarch64
target remote :1234
b * 0xFFFFFFFFC00088F0
c
si
si
x /10gx 0x0
x /10gx 0xe000000
x /10gx 0xe400000
x /10gx 0x40000000
x /10gx 0x40100000
x /10gx 0x40000000
x /10gx 0x40000000 + 0x20000
x /10gx 0x40000000 + 0x2c000
x /20i  0x40000000 + 0x91B8