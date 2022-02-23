set architecture aarch64
target remote :1234
b * 0xFFFFFFFFC0008C64 
c
set *(long long *)0xffffffffc0019bb8=0xffffffffc0009430
si
si
i r $sp
x /4i $pc
x /20gx $sp