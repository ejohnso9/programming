
; 2025Oct20
; Code defining a few things such that the environment is compatible
; with "The Little Schemer" book, Friedman & Felleisen, 4E 1996


; (define atom? (let ((f1 pair?) (f2 not)) (lambda (x) (f2 (f1 x)))))
(define atom?
  (lambda (x)
    (and (not (pair? x)) (not (null? x)))))


(define add1 (let ((f +)) (lambda (x) (f x 1))))
(define sub1 (let ((f -)) (lambda (x) (f x 1))))



(define add1 (lambda (x) (+ x 1)))
; ChatGPT gave me this and claims they are equivalent
; (define add1 (let ((f +)) (lambda (x) (f x 1))))

