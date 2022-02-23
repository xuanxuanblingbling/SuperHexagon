set architecture aarch64
target remote :1234
b * 0x7ffeffffd050
c
b * 0xFFFFFFFFC0000030
c