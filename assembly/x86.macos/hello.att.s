# 2025Oct02
# Author: Erik Johnson

# macOS-compatible AT&T syntax
# NB: ATT syntax: op source, dest

.global _start

# ENTRY POINT 
_start:
    # Set up dummy values (not used)
    mov $8, %rdi
    mov %rdi, %rsi

    # sys_write
    # mov $1, %rax       # syscall: write
    mov $0x2000004, %rax # syscall: write
    mov $1, %rdi       # fd: stdout
    lea hello_world(%rip), %rsi   # buf
    mov $17, %rdx      # count
    syscall

    # sys_exit (return code 42)
    # mov $60, %rax
    mov $0x2000001, %rax   # syscall number: exit
    mov $42, %rdi
    syscall

# Data section
hello_world:
    .asciz "Hello, Assembly!\n"

# to assemble:
#    $ as hello.att.s -o hello.att.o
# 
# With some help from ChatGPT, we arrived at this link command:
# (need to explicitly specify entry point: '_start' (not 'main'))
#    $ gcc -o hello hello.att.o -nostdlib -static -Wl,-e,_start
#
# EOF
