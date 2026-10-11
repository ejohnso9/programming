; 2025Oct03
; hello.nasm.asm
; Author: Erik Johnson
;
; DESCRIPTION
; Intel syntax assembly for macOS (64-bit)
; No C runtime — pure syscall

section .text
global _start

_start:
    ; write(1, message, 17)
    mov     rax, 0x2000004     ; syscall: write
    mov     rdi, 1             ; stdout
    lea     rsi, [rel message] ; pointer to message
    mov     rdx, 17            ; message length
    syscall

    ; exit(42)
    mov     rax, 0x2000001     ; syscall: exit
    mov     rdi, 42
    syscall

section .data
message:
    db      "Hello, Assembly!", 10   ; \n = 10

; to assemble:
;   $ nasm -f macho64 hello.nasm.asm -o hello.nasm.o
;
; to link:
;   ld -o hello hello.nasm.o -e _start -lSystem -macosx_version_min 10.13 -no_pie
;
; EOF
