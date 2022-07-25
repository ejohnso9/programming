
SCHEME NOTES 
=============

'guile' is installed at pythonanywhere.com (i.e., /usr/bin/guile)

To run the REPL (interactively):
    $ guile

To quit the REPL:
    guile> (quit)  ; note the parentheses placement!
    guile> ,q      ; same thing? (seems to have same effect)

invoke the interpreter on a scheme file:
    $ guile filename.scm

start the REPL, first evaluating file:
    $ guile -l filename.scm

from REPL, to load file:
    guile> (load "filename.scm")

See also:
    guile> ,h  ; print some basic help info
    $ main guile
    $ info guile
    $ info guile-tut


; Guile environment PROBELMS
;=============================
; Arrows keys, backspace, etc. not working?
; see this article: https://lists.gnu.org/archive/html/guile-user/2003-04/msg00047.html
; It says to put this in your ~/.guile:
(use-modules (ice-9 readline))
(activate-readline)
; YAY!!!  Seems to work!


; OTHER SCHEME RESOURCES
;========================
; home page for the GNU GUILE project
    https://www.gnu.org/software/guile/

; guile reference manual
    https://www.gnu.org/software/guile/manual/html_node/index.html

; SICP answers in Wiki format
    http://community.schemewiki.org/?SICP-Solutions

; the top of the Wiki above - general scheme interest
    http://community.schemewiki.org/

; the SICP book (2E) online @ MIT
    https://mitpress.mit.edu/sites/default/files/sicp/index.html

; other books @ MIT Press by Gerald Jay Sussman
; https://mitpress.mit.edu/contributors/gerald-jay-sussman
; SICP in Javascript: 
;   https://mitpress.mit.edu/books/structure-and-interpretation-computer-programs-1
;   https://sicp.sourceacademy.org/sicpjs.pdf  ; Full text as PDF


; GENERAL SCHEME SUMMARY NOTES...
====================================

; TYPES (so far)
;=================
; number
; symbol
; null (i.e., the empty list: '() )


; PREDICATES
;===========================
(define x 42)
(number? x)  ; #t
(number? 'x) ; #f

(define ab (cons 'a 'b))
(pair? (cons 1 '()))    ; #t
(pair? (cdr '(1 2 3)))  ; #f
(pair? ab)  ; #t

(symbol? ban) ; #t
(symbol? 'x)  ; #f
(symbol? #f)  ; #f
(symbol? (car '(ban hammer))) ; #t

(boolean? #t)  ; #t
(boolean? #f)  ; #t
(boolean? 42)  ; #f
(boolean? (symbol? 42))  ; #t (all results of predicates are boolean!)
(boolean? (symbol? #f))  ; #t

(define mt '())
(null? '()) ; #t
(null? mt)  ; #t
(null? 'mt) ; #f  (NB: symbol)
(null? (cdr (cons 'a '())))  ; #t
(null? (cdr '((1)) ))        ; #t

; this is used in SICP but is not a language built-in:
(define atom?
  (lambda (x)
    (and (not (pair? x)) (not (null? x)))))


; EQUALITY TESTS
;================
(= 42 (* 6 7)) ; #t - really should only be used on ints (and rationals)

(= (/ 1 3) (- (/ 2 3) (/ 1 3))) ; #t  
; CAREFUL... Guile has built-in rationals, but not all Schemes do!

(define Garfield 'cat)
(eq? Garfield 'cat)  ; #t  (i.e., symbol sameness)
(eq? (car '(Garfield cat)) 'Garfield) ; #t

(eq? '(1 2) '(1 2))  ; #t - symbolically equivalent
; however, note carefully:
(define a (cons 1 '()))
(define b (cons 1 '()))                                                                                                                  
(eq? a b)  ; #f !!! different list instances (holding same data)!
(eqv? a b) ; #f NB: *also* false! eqv? tests: numbers, symbols, booleans
(equal? a b) ; #t - this tests list *content* sameness




EOF

