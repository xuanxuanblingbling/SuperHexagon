set architecture aarch64
target remote :1234
b * 0x7ffeffffd044
c
set $pc = 0x7ffeffffd040
si
x /gx 0xffffffffc001e000
x /20gx 0xffffffffc0000000
x /2i 0xffffffffc0000030