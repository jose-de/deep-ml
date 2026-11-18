def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
   if not a or any(len(row) != len(b) for row in a):
      return -1

   return [sum(val_a * val_b for val_a, val_b in zip(row, b))
        for row in a
    ]



