

; Exercize 1.12
; a. '()
(cdr '((a (b c) d)))

; b. [X] 'd => '(d e)
(car (cdr cdr ('(a (b c) (d e)))))

; c. '(3 4)
(car (cdr '((1 2) (3 4) (5 6))))

; d. 2
(cdr (car '((1 2) (3 4) (5 6))))
