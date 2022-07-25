
; "Scheme and the Art of Programming",
; Springer and Friedman, The MIT Press
; ISBN: 0-262-19288-8, 

; Exercizes 2.1 through 2.5, pg 39, 40

(define (show-prob hdr output)
  (display hdr) (display ": ") (display output)
  (newline) (newline) )

(define ls '(one two three four five six))

; Ex 2.1
(define hdr "Ex 2.1")
(define (second ls) (cadr ls))
(show-prob hdr (second ls))

; Ex 2.2
(define hdr "Ex 2.2")
(define (third ls) (caddr ls))
(show-prob hdr (third ls))

; Ex 2.3
(define hdr "Ex 2.3")
(define make-list-of-one (lambda (item) (cons item '())))
; above could also be: (define (make-list-of-one item) (cons item '()) )
(define make-list-of-two
  (lambda (item1 item2)
    (cons item1 (make-list-of-one item2))))
(define firsts-of-both
  (lambda (list-1 list-2)
    (make-list-of-two (car list-1) (car list-2))))

(show-prob "Ex 2.3a" (firsts-of-both '(1 3 5 7) '(2 4 6)))
; NB: book is missing second single quote on the 2nd list in line above!
(show-prob "Ex 2.3b" (firsts-of-both '((a b) (c d)) '((e f) (g h)) ) )


