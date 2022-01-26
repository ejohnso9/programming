
SCHEME NOTES 
=============

'guile' is installed at pythonanywhere.com (i.e., /usr/bin/guile)

To run the REPL (interactively):
    $ guile

To quit the REPL:
    guile> (quit)  ; note the parentheses placement!

invoke the interpreter on a scheme file:
    $ guile filename.scm

start the REPL, first evaluating file:
    $ guile -l filename.scm

from REPL, to load file:
    guile> (load "filename.scm")

See also:
    $ main guile
    $ info guile
    $ info guile-tut


OTHER SCHEME RESOURCES
-----------------------
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
; e.g., SICP in Javascript: 
;   https://mitpress.mit.edu/books/structure-and-interpretation-computer-programs-1
    https://mitpress.mit.edu/contributors/gerald-jay-sussman


EOF

