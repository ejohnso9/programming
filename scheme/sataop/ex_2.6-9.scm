
; "Scheme and the Art of Programming",
; Springer and Friedman, The MIT Press
; ISBN: 0-262-19288-8, 

; Exercizes 2.6 through 2.9, pg 46, 46

(load "show-prob.scm") ; dump problem results to stdout helper


; 2.6 - (human reasoning)
; TRUE: (a b c), FALSE: (e f)
(define a #t) (define b #t) (define c #t) (define e #f) (define f #f)
(show-prob "2.6a" (and a (or b e)))  ; #t
(show-prob "2.6b" (or e (and (not f) a c))) ; #t
(show-prob "2.6c" (not (or (not a) (not b)))) ; #t
(show-prob "2.6d" (and (or a f) (not (or b e))))  ; #f

; 2.7
