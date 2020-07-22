;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Factorial usando Common lISp en SBCL
; @author swd
; @date 2020/07/22
; @version 0.1
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(deffun factorial (n) (
    if(< n 2) 1 (* n (factorial(- n 1)))
))

(write (factorial 5))