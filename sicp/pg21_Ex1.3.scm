
; AUTHOR: Erik Johnson
;   DATE: 2022Jan25
;
; DESCRIPTION
;    SICP Exercize 1.3, pg 21
;
; PROBLEM STATEMENT
;   Define a procedure that takes three numbers as arguments and returns
;   the sum of the squares of the two larger numbers.



(define (sum_sq_big2 x y z)
    ; NB: nothing wrong with putting a (define ...) inside a (define ...)
    (define (sum_sq a b)
        (define (sq x) (* x x))
        (+ (sq a) (sq b))
    )
    (define (le a b) (not (> a b)) )  ; less then or equal to
    (cond
        ; CASE 1: x is smallest
        ((and (le x y) (le x z)) (sum_sq y z))

        ; CASE 2: y is smallest
        ((and (le y x) (le y z)) (sum_sq x z))

        ; CASE 3: z is smallest
        ((and (le z x) (le z y)) (sum_sq x y))
    )
)

;
; TEST CASES
;
(define answer (sum_sq_big2 1 3 2)) ; should be 13
(display "(sum_sq_big2 1 3 2) is: ") (display answer) (newline)

(define answer (sum_sq_big2 4 2 1)) ; should be 20
(display "(sum_sq_big2 4 2 1) is: ") (display answer) (newline)

(define answer (sum_sq_big2 3 3 3)) ; should be 18
(display "(sum_sq_big2 3 3 3) is: ") (display answer) (newline)


; So, this raises a pedogogic question...
; I want something like a test harness...
; I want to specify ((1 3 2), 13), automatically print out what
; the function call was, then verify whether calling my function
; w/ args of (1 3 2) gives expected answer of 13.
