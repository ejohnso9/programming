
(define expr_1_2
  ( /
    ; numerator
    (+ 5 4 (- 2
              (- 3
                 (+ 6
                    (/ 4 5)))))

    ; denomenator
    (* 3 (- 6 2) (- 2 7)) )
)

(display expr_1_2)  ; -37/150 (verfied at: http://community.schemewiki.org/?sicp-ex-1.2)
(newline)
