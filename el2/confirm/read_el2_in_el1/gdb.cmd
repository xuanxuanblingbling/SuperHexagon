set architecture aarch64
target remote :1234
b * 0xffffffffc000003c
c
x /20gx 0xffffffffc0002000
b * 0xffffffffc0000040
c
x /20gx 0xffffffffc0002000