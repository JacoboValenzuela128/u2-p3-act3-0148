import numpy as np

# Arath Valenzuela - NC:0148 (22/10/26)
print("EJERCICIOS DE NUMPY")

# Ejercicio 1: Crear un arreglo
arre = np.array([10, 20, 30, 40, 50])
print("\nEjercicio 1: Arreglo")
print(arre)

# Ejercicio 2: Generar números con linspace
arre = np.linspace(start=0, stop=1, num=5)
print("\nEjercicio 2: Linspace")
print(arre)

# Ejercicio 3: Generar un número decimal aleatorio
n0148 = np.random.rand()
print("\nEjercicio 3: Número decimal aleatorio")
print(n0148)

# Ejercicio 4: Generar un número entero aleatorio
n0148 = np.random.randint(1, 11)
print("\nEjercicio 4: Número entero aleatorio")
print(n0148)

# Ejercicio 5: Generar cinco números enteros aleatorios
arre = np.random.randint(1, 11, size=5)
print("\nEjercicio 5: Cinco números aleatorios")
print(arre)

print("Arath Valenzuela - NC:0148 (22/10/26)")