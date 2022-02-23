set architecture aarch64
target remote :1234
b * 0xFFFFFFFFC00088F0
c
si
si
i r cpsr
i r SCTLR_EL2