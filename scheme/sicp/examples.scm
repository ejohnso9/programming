#!/usr/bin/guile -s
!#
; see: https://www.gnu.org/software/guile/manual/html_node/Running-Guile-Scripts.html 
;
; With x permissions set, you should be able to execute this script as:
;   $ hello.scm
;
; Or, without, as:
;   $ guile hello.scm
;
; SEE ALSO: 
;   local README.txt
;   https://www.gnu.org/software/guile/manual/html_node/index.html
;   http://community.schemewiki.org/?SICP-Solutions

; output
(display "Hello, world!")
(newline)

; defining symbols
(define x 42)
(display "x is: ") (display x) (newline)

; one way to define a function
(define (euclid_dist x y)
  (define (sq x) (* x x))
  (sqrt (+ (sq x) (sq y)))
)

; a few "perfect" triangles are: (3 4 5), (5 12 13), (9 12 15)
(display "(euclid_dist 3 4) is: ")
(display (euclid_dist 3 4))
(newline)

(display "(euclid_dist 5 12) is: ")
(display (euclid_dist 5 12))
(newline)

(display "(euclid_dist 9 12) is: ")
(display (euclid_dist 9 12))
(newline)

; now, modify above to work with this:
(define data
  '(((3 4) 5) ((5 12) 13) ((9 12) 15)))

(define (test f args_exp)
    (define (result) (apply f (car args_exp)))
    (display "args are: ") (display (car args_exp)) (newline)
    (define (_exp) (cdr args))
    (if (= result _exp)
        (display "PASS: ")
        (display "FAIL ") )
    (display "(euclid_dist ")
    (display _args)
    (display ") is: ")
    (display _exp)
    (newline)
) ; define test

(test euclid_dist '((3 4) 5))
; cons examples
; car examples
; cdr examples

(newline)
; EOF

