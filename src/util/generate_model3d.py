import numpy as np
from stl import mesh

# Las dimensiones del rack en mm
length = 250
width = 433
height = 44

# Crear 8 vértices para el cuboide
vertices = np.array([[0, 0, 0],
                     [length, 0, 0],
                     [length, width, 0],
                     [0, width, 0],
                     [0, 0, height],
                     [length, 0, height],
                     [length, width, height],
                     [0, width, height]])

# Crear 12 triángulos (2 por cada cara del cuboide)
faces = np.array([[0,3,1], [1,3,2],  # inferior
                  [0,1,5], [0,5,4],  # frente
                  [1,2,6], [1,6,5],  # derecha
                  [2,3,7], [2,7,6],  # atrás
                  [3,0,4], [3,4,7],  # izquierda
                  [4,5,6], [4,6,7]]) # superior

# Crear la malla
rack_model = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        rack_model.vectors[i][j] = vertices[f[j],:]

# Guardar el modelo en un archivo STL
rack_model.save('rack_model.stl')
