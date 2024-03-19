def calcular_determinante_recursivo(matriz):
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        determinante = 0
        for i in range(len(matriz)):
            submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
            determinante += ((-1) ** i) * matriz[0][i] * calcular_determinante_recursivo(submatriz)
        return determinante

# Ejemplo de matriz 3x3
matriz_3x3 = [
    [2, 4, 3],
    [1, 5, 7],
    [6, 2, 9]
]

# Calcular y mostrar el determinante
determinante_recursivo = calcular_determinante_recursivo(matriz_3x3)
print("El determinante calculado recursivamente es:", determinante_recursivo)
