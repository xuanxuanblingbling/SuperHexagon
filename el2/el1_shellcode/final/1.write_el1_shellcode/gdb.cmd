set architecture aarch64
target remote :1234
b * 0x7ffeffffd008
c
b * 0x7ffeffffd024
c
i r x0
x /2i $x0