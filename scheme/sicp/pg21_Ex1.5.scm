#!/usr/bin/guile -s
!#

; SICP(2E) Problem 1.5, page 21
; AUTHOR: Erik Johnson
; DATE: 2022Jan25
;       2025Mar13 Looking at SICP again, and so I guess this exercize
;       drives hom the point that the interpreter is in fact
;       "applicative" order and not "normal" order as described on pages
;       15-16.

(define (p) (p))

(define (test x y)
   (if (= x 0) 0 y) )

(newline)
(display "just before calling: (test 0 (p))  ; (This will, in fact, hang. Hit CTRL-C to exit.")

; This *WILL* in fact hang. I suppose it will eventually crash, but
; after leaving it run for a couple minutes, it had not yet crashed.
(test 0 (p))  ; uncomment this line if you really have to see it.

(display "just after (test 0 (p))")

(newline)
