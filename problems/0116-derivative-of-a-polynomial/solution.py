def poly_term_derivative(c: float, x: float, n: float) -> float:
    c = c*n 
    n -= 1

    derivative = c*(x**n)

    return derivative
