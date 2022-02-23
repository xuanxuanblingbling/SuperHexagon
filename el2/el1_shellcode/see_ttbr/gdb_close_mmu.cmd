set architecture aarch64
target remote :1234
b * 0x401B48
c
si
set $x0=0x30d00800
set $pc=0xffffffffc000002c
si