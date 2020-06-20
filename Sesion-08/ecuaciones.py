import numpy as np

a = np.array(
    (  # contiene las filas del array
        [2, 1, -3],
        [5, -4, 1],
        [1, -1, -4]
    )
)
b = np.array( ([7, -19, 4]) )

x = np.linalg.solve(a, b)

print(x)

# Validando resultados
# A x = b
bp = np.dot(a, x)
print(bp)
