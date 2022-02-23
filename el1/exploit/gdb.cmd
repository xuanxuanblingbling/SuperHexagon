set architecture aarch64
target remote :1234
b * 0x7ffeffffd008
c
b * 0xffffffffc0008C34
c