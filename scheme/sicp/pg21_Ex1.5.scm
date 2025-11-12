#!/usr/bin/guile -s
!#

; SICP(2E) Problem 1.5, page 21
; AUTHOR: Erik Johnson
; DATE: 2022Jan25
;       2025Mar13 Looking at SICP again, and so I guess this exercize
;       drives hom the point that the interpreter is in fact
;       "applicative" order and not "normal" order as described on pages
;       15-16.
;
; 2025Oct27 just to clarify: Ben is correct in his thinking: applicative 
;   evaluation leads to infinite recursion on (p), whereas "normal-order" 
;   evaluation would have presumably stopped right away in (test).
;   We never get to the second display statement, but I can't tell
;   whether guile is mindlessly spinning or something internally hangs.
;   It does *NOT* "blow out the stack" with a complaint about not being
;   able to allocate memory or max recursion limit exceeded. 
;   ChatGPT points out that proper tail recursion is a requirement of
;   the specification. There is nothing new to allocate within, p, so no
;   memory being consumed...
;   Still... I left the process running for ~15 minutes and it did not
;   crash, nor did it seem to burn up the few seconds of CPU time that
;   PythonAnywhere allocates to me per day.
;
; USAGE
;   This file can be invoked (on Linux w/ a 'guile') as:
;   $ guile pg21_Ex1.5.scm


; modifying p per ChatGPT suggestions so we can see it running
; (use-modules (ice-9 sleep)) ; for (sleep 1)  ; ej: NOT needed

; (define (p) (p))
(define (p)
  (display "(p) ")
  (sleep 1)
  (p))


(define (test x y)
   (if (= x 0) 0 y) )

(newline)
(display "just before calling: (test 0 (p))  ; (This will, in fact, hang. Hit CTRL-C to exit.)")

; This *WILL* in fact hang. I suppose it will eventually crash, but
; after leaving it run for a couple minutes, it had not yet crashed.
(test 0 (p))  ; uncomment this line if you really have to see it.

(display "just after (test 0 (p))")

(newline)

; The full question is:
;
; What behavior will Ben observe with an interpreter that
; uses applicative-order evaluation? What behavior will he
; observe with an interpreter that uses normal-order evaluation?
; Explain your answer. (Assume that the evaluation
; rule for the special form if is the same whether the interpreter
; is using normal or applicative order: The predicate
; expression is evaluated first, and the result determines
; whether to evaluate the consequent or the alternative expression.)
;
; Indeed, guile appears to be "hung up" evaluating (p). Changing p to
; actually print something (with a sleep) verifies the process is not
; really hung - it's still running, but not returning.

; EOF
