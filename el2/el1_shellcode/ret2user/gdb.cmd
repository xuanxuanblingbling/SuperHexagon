set architecture aarch64
target remote :1234
b * 0x401B48
c
si
set $pc=0x400104
si