set architecture aarch64
target remote :1234
b * 0xFFFFFFFFC0008C64 
c
set *(long long *)0xffffffffc0019bb8=0xffffffffc0009430
set *(long long *)0xffffffffc0019c08=0xffffffffc0008408
c