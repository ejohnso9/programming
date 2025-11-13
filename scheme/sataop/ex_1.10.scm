;
; "Scheme and the Art of Programming", Springer, Friedman, 1989
; ISBN: 0-262-19288-8
;
; Exercize 1.10, pg25 (of printed book)
;
; AUTHOR: Erik Johnson
; DATE: 2025Nov1
;
; TESTS given on pgs 24 - 25
;   number?
;   symbol?
;   boolean?
;   pair?  ; i.e., list?
;   procedure?

(newline)

; If the operands a, b evaluate to any values, what is...
; (NB: using 'a for alpha, 'b for beta (ASCII)

; a. (symbol? (cons a b))  ; #f (is list)
(let* (
      (stmt "a. (symbol? (cons a b))")
      (a 'a) (b 'b)
      (value (symbol? (cons a b))))
  (display stmt) (newline)
  (display "  is: ") (display value) (newline)
  value  ; return value
)
(newline)

; b. (pair? (cons a b))  ; #t (i.e., pair? is a list-type detector)
;                        ; and (cons a b) *IS* a list
(let* (
      (stmt "b. (pair? (cons a b))")
      (a 'a) (b 'b)
      (value (pair? (cons a b))))
  (display stmt) (newline)
  (display "  is: ") (display value) (newline)
  value  ; return value
)
(newline)

; c. (null? (cons a b))  ; #f (its a list w/ two elements in it!)
(let* (
      (stmt "c. (null? (cons a b))")
      (a 'a) (b 'b)
      (value (null? (cons a b))))
  (display stmt) (newline)
  (display "  is: ") (display value) (newline)
  value  ; return value
)
(newline)

; d. (null? (cdr (cons a '()))
;   OOPS: I initially got this wrong...
;   (cons a '()) is: (a)
;   and cdr called on any one-element list is a zero-element list: '()
;   that *IS* null (sometimes returned in LISP for false / #f)
;   i.e., the answer is: #t / True
(let* (
      (stmt "(null? (cdr (cons a '()))")
      (a 'a) (b 'b)
      (value (null? (cdr (cons a '())))))
  (display stmt) (newline)
  (display "  is: ") (display value) (newline)
  value  ; return value
)
(newline)


; Exercize 1.11 essentially asks what I said in d.
; Q: What is (null? (cdr ls))  ; where ls is a one-element ls?
; A: that's the one-element list minus the first element, which is: '()
; which *IS* null?

