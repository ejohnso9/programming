;
; SICP(2E) Problem 1.5, page 21
; AUTHOR: Erik Johnson
; DATE: 2022Jan25

(define (p) (p))

(define (test x y)
   (if (= x 0) 0 y) )


; This *WILL* in fact hang. I suppose it will eventually crash, but
; after leaving it run for like 30 seconds, it had not yet crashed.
;
; (test (p) 0)  ; uncomment this line if you really have to see it.

(newline)
(display "call: (test (p) 0)")
(display "...will, in fact, hang. Edit source to verify.")
(newline)
