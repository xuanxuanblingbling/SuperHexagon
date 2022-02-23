set architecture aarch64
target remote :1234
b * 0x7ffeffffd050
c
b * 0xFFFFFFFFC0008C68
c
x /i $pc
i r lr
x /i $lr
si
si