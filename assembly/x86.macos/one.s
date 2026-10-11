# 2025Oct02
# Author: Erik Johnson
# Code to go along with the video: 
#   https://www.youtube.com/watch?v=6S5KRJv-7RU
#
# to assemble:
#    $ as one.s -o one.o
# to link
#    $ gcc -o one one.o -nostdlib -static

.global _start
.intel_syntax noprefix

# ENTRY POINT 
_start:
    # doesn't really do anything, but works (presumably)
    mov rdi, 8
    mov rsi, rdi

    # sys_write
    mov rax, 1
    mov rdi, 1
    # PA works: lea rsi, [hello_world]
    lea rsi, hello_world(%rip)
    mov rdx, 17
    syscall

    # sys_exit (w/ value 42)
    # my 'as' does not like: ;-type comments
    # (despite that being used in the video)
    mov rax, 60
    mov rdi, 42
    syscall
    # 2025Oct02: clean exit working!

hello_world:
    .asciz "Hello, Assembly!\n"

# EOF
