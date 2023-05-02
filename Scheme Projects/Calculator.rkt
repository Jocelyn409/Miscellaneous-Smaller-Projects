; Find which operator is in the first item of list op,
; and return #f otherwise.
(define (find-op op)
  (cond
    ((equal? 'plus (car op)) +)
    ((equal? 'minus (car op)) -)
    ((equal? 'times (car op)) *)
    ((equal? 'divide (car op)) /)
    (else #f)
  )
)

; Remove first item in list arg, then get first item in arg.
(define (first-arg arg)
  (car (cdr arg))
)

; Remove first two items from list arg,
; then get first item in that list.
(define (second-arg arg)
  (car (cdr (cdr arg)))
)

; Return #t if exp is a number.
(define (simple-expression? exp)
  (number? exp)
)

; Return #t if exp is a list, length of list exp is 3,
; and first item in exp is an operator.
(define (compound-expression? exp)
  (and (list? exp) (= (length exp) 3) (find-op exp) #t)
)

; Returns input if value is a number or displays an invalid input.
; If input is a compound expression, recursively calculate it.
(define (calculate input)
  (cond
      ((simple-expression? input) input) ; Base case.
      ((compound-expression? input) ; Calculate compound expression.
          (car (list ((find-op input)
             (calculate (first-arg input))
             (calculate (second-arg input))))))
      (else display input) ; Error case.
  )
)

(calculate '(this is an incorrect input))
(calculate '(times 2 3)) ; 3 * 2 = 6
(calculate '(plus 1 (times 2 3))) ; (3 * 2) + 1 = 7
(calculate '(divide (times 10 2) 10)) ; (10 * 2) / 10 = 2
(calculate '(minus (plus 1 (plus 1 0)) 1)) ; (1 + (1 + 0)) - 1 = 1

