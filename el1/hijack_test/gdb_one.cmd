set architecture aarch64
target remote :1234
b * 0xFFFFFFFFC0008BE0
c
set *(long long *)0xffffffffc0019bb8=0xffffffffc0008408
c