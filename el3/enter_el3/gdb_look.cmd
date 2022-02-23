set architecture aarch64
target remote :1234
b * 0x40051C
c
set $cpsr=0x800003cc
set $x0=0x30c5083a
set $pc=8
si
x /10gx 0x0
x /10gx 0xe000000
x /10gx 0xe400000
x /10gx 0x40000000
x /10gx 0x40100000
i r