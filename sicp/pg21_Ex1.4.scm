
; AUTHOR: Erik Johnson
;   DATE: 2022Jan25
;
; DESCRIPTION
;    SICP Exercize 1.4, pg 21
;
; PROBLEM STATEMENT
;   Observer that our model of evaluation alows for combinations whose
;   operators are compound expressions. Use this observation to describe
;   the bvehavior of the following procedure

(define (a-plus-abs-b a b)
    ((if (> b 0) + -) a b ))

; The first element of a list application is an operator or an
; expression that evaluates to an operator. The latter, in this case, so
; we evaluate the 'if' operator, the predicate of which is a test for
; whether b is positive. If b is positive, the result is '+', else '-'.
; So, in the case of positive b, we simply add b. In the case of
; negative b, we subtract the value of b (which is negative) effectively
; adding the magnitude of b (which is effectively the same as taking the
; absolute value of b, then adding it to a).

