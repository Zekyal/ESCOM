# Prueba Practica 03: Esfericas -> Cartesianas

# Importacion de librerias
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
import numpy as np

# Banderita improvisada ewe
print("0 = Coordenadas Esfericas (r, θ, φ) -> Coordenadas Cartesianas (x, y, z)")
print("1 = Coordenadas Cartesianas (x, y, z) -> Coordenadas Esfericas (r, θ, φ)")
b = int(input())

# Spherical coordinates -> Cartesian Coordinates
if b == 0:
    # Insercion de valores
    
    # valor 'r'
    r = float(input('r = '))
    
    # valor 'theta'
    theta = float(input('θ = '))
    deg = int(input("0 para grados / 1 para radianes -> "))
    
    if(deg == 0):   # Si el valor de theta esta dado en grados
        theta = np.radians(theta)   # Valor de theta se convierte a radianes
        print(theta)
    
    # valor 'phi'
    phi = float(input('φ = '))
    deg = int(input("0 para grados / 1 para radianes -> "))
    
    if(deg == 0):   # Si el valor de phi esta dado en grados
        phi = np.radians(phi)   # Valor de phi se convierte a radianes
        print(phi)
    

    # Formulas de conversion
    rx = r * np.sin(theta) * np.cos(phi) + 0
    ry = r * np.sin(theta) * np.sin(phi) + 0
    rz = r * np.cos(theta) + 0
    
    # Impresion de Resultados
    print("x =", rx)
    print("y =", ry)
    print("z =", rz)
# Cartesian coordinates -> Spherical Coordinates
else:
    # Insercion de valores
    rx = float(input('x = '))
    ry = float(input('y = '))
    rz = float(input('z = '))
    
    # Formulas de conversion
    
    # Coordenada 'r'
    r = np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2))
    
    # Coordenada 'theta'
    if(rz > 0):     # z > 0
        theta = np.arctan(np.sqrt(pow(rx, 2) + pow(ry, 2))/rz)
    elif(rz < 0):   # z < 0
        theta = np.pi + np.arctan(np.sqrt(pow(rx, 2) + pow(ry, 2))/rz)
    else:           # z = 0
        if(rx == 0 and ry == 0):    # z = x = y = 0
            theta = 0
        else:                       # z = 0 and xy =! 0                   
            theta = np.pi/2
    
    # Coordenada 'phi'
    if(rx > 0 ):    # x > 0
        phi = np.arctan(ry/rx)
    elif(rx < 0):   # x < 0
        if(ry >= 0):    # x < 0 and y >= 0 
           phi = np.arctan(ry/rx) + np.pi
        elif(ry < 0):   # x < 0 and y < 0
            phi = np.arctan(ry/rx) - np.pi
    else:           # x = 0 
        if(ry > 0):     # x = 0 and y > 0
            phi = np.pi/2
        elif(ry < 0):   # x = 0 and y < 0
            phi = -np.pi/2
        else:           # x = 0 and y = 0
            phi = 0
    
    # Conversion de radianes a angulos
    thetaDeg = np.degrees(theta)
    phiDeg = np.degrees(phi)
    
    # Impresion de Resultados
    print("r =", r)
    print("θ =", theta, "rad /", thetaDeg, "°")
    print("φ =", phi, "rad /", phiDeg, "°")

# -------------------- GRAFICACION --------------------

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.xaxis.set_label_text('x', color = 'b')
ax.yaxis.set_label_text('y', color = 'b')
ax.zaxis.set_label_text('z', color = 'b')

ax.plot((5, -5), (0, 0), (0, 0), color="grey")
ax.plot((0, 0), (5, -5), (0, 0), color="grey")
ax.plot((0, 0), (0, 0), (5, -5), color="grey")

ax.plot((rx, rx), (0, ry), (0, 0), color = "red", linestyle = "dashed")
ax.plot((0, rx), (ry, ry), (0, 0), color = "red", linestyle = "dashed")
ax.plot((rx, rx), (ry, ry), (0, rz), color = "red", linestyle = "dashed")
ax.plot((0, rx), (0, rx*np.tan(phi)), (0, 0), color = "red", linestyle = "dashed")
ax.plot((0, rx), (0, rx*np.tan(phi)), (rz, rz), color = "red", linestyle = "dashed")

ax.quiver(0, 0, 0, rx, ry, rz, arrow_length_ratio=0.1)

plt.show()