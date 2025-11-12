

; testing (cond) special form: 
; footnote bottom of page 24 (PDF)

(define x 2)

(define y
    (cond
      ((= x 1) 'this 'is 'executed 'but 'ignored (< 2 3) "one")
      ((= x 2) '(and so is this and the next) "foo" "two"))
)

(display (string-append "y is: '" y "'"))
(newline)

