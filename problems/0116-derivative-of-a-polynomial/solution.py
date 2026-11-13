def poly_term_derivative(c: float, x: float, n: float) -> float:
    if n == 0 or x == 0:
        return 0

    else:
        c_dx = c*n 
        n_dx = n - 1

        derivative = c_dx*(x**n_dx)

        return derivative
