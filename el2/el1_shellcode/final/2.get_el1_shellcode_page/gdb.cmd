set architecture aarch64
target remote :1234
b * 0x7ffeffffd008
c
b * 0x7ffeffffd024
c
set $pc=0x7ffeffffd018
si
i r TTBR0_EL1
x /gx 0xffffffffc0000000 + 0x20000 + 255*8
x /gx 0xffffffffc0000000 + 0x24000 + 507*8
x /gx 0xffffffffc0000000 + 0x27000 + 511*8
x /gx 0xffffffffc0000000 + 0x28000 + 508*8
x /2i 0xffffffffc0000000 + 0x35000
x /2i 0x7ffeffffc000