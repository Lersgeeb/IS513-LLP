;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Ejemplo de programa en commn Lisp
; Usando SBCL
; @author swd
; @date 2020/07/22
; @version 0.1
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; Mesnaje de bienvenida
(write-line "")
(write-line "")
(write-line "Escriba en pantalla un dato numérico: ")
(write-line "")

; Definir una variable y se solicita el dato al usuario
(defvar *unaVariableCualquiera*)
(setf *unaVariableCualquiera* (read))
(write-line "")

;Se imprimen los resultados de una operación cualquiera
(write-line "El resultado de su número * por 5 es: ")
(write (* 5 *unaVariableCualquiera*))
(write-line "")