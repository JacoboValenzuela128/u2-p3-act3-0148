import numpy as np

# Arath Valenzuela - NC:0148 (22/10/26)
# Array indexing in NumPy
import numpy as np

n0148 = np.array([10, 20, 30, 40, 50])
print(n0148)
print(n0148[0])
print(n0148[3])
print(n0148[-1])
print(n0148[-2])
print("--------------------------------------------------")
n0148 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(n0148)
print(n0148[0, 0])
print(n0148[1, 2])
print(n0148[-1, -1])
print(n0148[-2, -2])
print("--------------------------------------------------")
# 3D array 2x(2x3)
n0148 = np.array([
    # 0 -2
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    # 1 -1
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
print(n0148)
print(n0148[0, 0, 0])
print(n0148[1, 1, 2])
print(n0148[-1, -1, -2])
print("Arath Valenzuela - NC:0148 (22/10/26)")