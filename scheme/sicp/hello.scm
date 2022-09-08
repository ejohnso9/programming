#!/usr/bin/guile -s
!#
; A trivial GUILE script, taken from:
; https://www.gnu.org/software/guile/manual/html_node/Running-Guile-Scripts.html 
;
; With 'x' permissions set, on a machine that has 'guile' installed (such
; as is the case at pythonanywhere.com) you should be able to execute
; this script as:
;   $ hello.scm
;
; Or, without 'x' permissions as:
;   $ guile hello.scm
;
; SEE ALSO: 
;   local README.txt
;   https://www.gnu.org/software/guile/manual/html_node/index.html
;   http://community.schemewiki.org/?SICP-Solutions

(display "Hello, world!")
(newline)

; EOF

