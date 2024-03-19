import random

def generar_polinomio(grado):
    """Genera un polinomio de un grado dado con coeficientes aleatorios entre 1 y 9."""
    return [random.randint(1, 9) for _ in range(grado + 1)]

def restar_polinomios(p1, p2):
    """Resta dos polinomios y devuelve el resultado."""
    max_len = max(len(p1), len(p2))
    # Asegurar que ambos polinomios tienen la misma longitud añadiendo ceros
    p1 = [0] * (max_len - len(p1)) + p1
    p2 = [0] * (max_len - len(p2)) + p2
    return [coef_p1 - coef_p2 for coef_p1, coef_p2 in zip(p1, p2)]

def eliminar_termino(polinomio, grado_termino):
    """Elimina un término de un polinomio basándose en su grado."""
    grado_polinomio = len(polinomio) - 1
    if grado_termino <= grado_polinomio:
        polinomio[grado_polinomio - grado_termino] = 0
    return polinomio

def existe_termino(polinomio, grado_termino):
    """Determina si un término específico existe en un polinomio."""
    grado_polinomio = len(polinomio) - 1
    if grado_termino > grado_polinomio:
        return False
    return polinomio[grado_polinomio - grado_termino] != 0

# Ejemplo de uso:
grado_polinomio = 4  # Polinomio de grado 4
p1 = generar_polinomio(grado_polinomio)
p2 = generar_polinomio(grado_polinomio)

print(f"Polinomio 1: {p1}")
print(f"Polinomio 2: {p2}")

resta = restar_polinomios(p1, p2)
print(f"Resta: {resta}")

# Eliminar el término x^2 (grado 2)
p1_sin_x2 = eliminar_termino(p1, 2)
print(f"Polinomio 1 sin x^2: {p1_sin_x2}")

# Verificar si existe el término x^3 en Polinomio 1
existe_x3 = existe_termino(p1, 3)
print(f"Existe x^3 en Polinomio 1: {'Sí' if existe_x3 else 'No'}")
