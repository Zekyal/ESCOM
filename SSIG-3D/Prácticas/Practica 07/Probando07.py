# Prueba Practica 07: Componentes y cosenos directores de un vector

# Importacion de librerias
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
import numpy as np

# Banderita improvisada 2: El regreso
print("0 = Obtener los cosenos directores (α, β y ɣ) y la magnitud de un vector")
print("1 = Obtener un vector a partir de sus cosenos (α, β y ɣ) y magitud")
b = int(input())

# Obtencion de cosenos directores y magnitud de un vector
if b == 0:
    # Insercion de valores de los ejes del vector
    rx = float(input('x = '))
    ry = float(input('y = '))
    rz = float(input('z = '))
    
    # Cosenos Directores y Magnitud 
    magnitud = np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2))
    
    if (magnitud == 0):
        alpha = 0
        beta = 0
        gamma = 0
    else:
        alpha = np.arccos(np.absolute(rz) / magnitud)
        beta = np.arccos(np.absolute(rx) / magnitud)
        gamma = np.arccos(np.absolute(ry) / magnitud)
    
    alphaDeg = np.degrees(alpha)
    betaDeg = np.degrees(beta)
    gammaDeg = np.degrees(gamma)
    
    # Impresion de resultados
    print("|v| =",magnitud)
    print("α =", alpha, "rad /", alphaDeg, "°")
    print("β =", beta, "rad /", betaDeg, "°")
    print("ɣ =", gamma, "rad /", gammaDeg, "°")
    
# Obtencion de un vector a partir de sus cosenos directores y magnitud
else:
    # Insercion de valores
    
    # magnitud
    magnitud = float(input('|v| = '))
    
    if(magnitud < 0):
        print("ERROR: La magnitud de un Vector, siempre debe ser positiva")
        exit(0)
    
    # valor 'alpha'
    alpha = float(input('α = '))
    deg = int(input("0 para grados / 1 para radianes -> "))
    
    if(deg == 0):   # Si el valor de theta esta dado en grados
        alpha = np.radians(alpha)   # Valor de theta se convierte a radianes
        print(alpha, "rad")
    
    # valor 'beta'
    beta = float(input('β = '))
    deg = int(input("0 para grados / 1 para radianes -> "))
    
    if(deg == 0):   # Si el valor de theta esta dado en grados
        beta = np.radians(beta)   # Valor de theta se convierte a radianes
        print(beta, "rad")
    
    # valor 'gamma'
    gamma = float(input('ɣ = '))
    deg = int(input("0 para grados / 1 para radianes -> "))
    
    if(deg == 0):   # Si el valor de theta esta dado en grados
        gamma = np.radians(gamma)   # Valor de theta se convierte a radianes
        print(gamma, "rad")
        
    
    # Ejes del Vector
    # β es el angulo entre el vector y i
    rx = magnitud * np.cos(beta)
    # ɣ es el angulo entre el vector y j
    ry = magnitud * np.cos(gamma)
    # α es el angulo entre el vector y k
    rz = magnitud * np.cos(alpha)
    
    # Impresion de Resultados
    print("x =", rx)
    print("y =", ry)
    print("z =", rz)

# -------------------- GRAFICACION --------------------

fig = plt.figure()
ax = plt.axes(projection = '3d')
# Titulo de la grafica
plt.suptitle("Grafica de un Vector")
# Nombres de los ejes
ax.set_xlabel("PosiciónX", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
ax.set_ylabel("PosiciónY", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_zlabel("PosiciónZ", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})

# ----------   Ejes de la grafica    ----------
ax.plot((magnitud, 0), (0, 0), (0, 0), color = "orange", label='X(+)')
ax.plot((0, -magnitud), (0, 0), (0, 0), color = "red", label='X(-)')
ax.plot((0, 0), (magnitud, 0), (0, 0), color = "green", label='Y(+)')
ax.plot((0, 0), (0, -magnitud), (0, 0), color = "blue", label='Y(-)')
ax.plot((0, 0), (0, 0), (magnitud, 0), color = "slateblue", label='Z(+)')
ax.plot((0, 0), (0, 0), (0, -magnitud), color = "brown", label='Z(-)')


# ----------    Vector  ----------
ax.quiver(0, 0, 0, rx, ry, rz, arrow_length_ratio=0.1, label='Vector')
# nombre del vector
ax.text(rx, ry, rz, 'vector', style='italic', fontweight='bold', color = plt.rcParams['axes.prop_cycle'].by_key()['color'][0])


# ----------    Componentes i, j y k   ----------
ax.quiver(0, 0, 0, rx, 0, 0, arrow_length_ratio=0.1, color = "gray")
ax.quiver(0, 0, 0, 0, ry, 0, arrow_length_ratio=0.1, color = "darkviolet")
ax.quiver(0, 0, 0, 0, 0, rz, arrow_length_ratio=0.1, color = "black")
# nombres de los ejes
ax.text(3*rx/4, 0, 0, 'i', style='italic', fontweight='bold', color = "gray")
ax.text(0, 3*ry/4, 0, 'j', style='italic', fontweight='bold', color = "darkviolet")
ax.text(0, 0, 3*rz/4, 'k', style='italic', fontweight='bold', color = "black")


# ----------    Componentes i, j y k traslapados   ----------
ax.plot((0, rx), (ry, ry), (0, 0), color = "cyan", linestyle = "dotted", label='i')
ax.plot((rx, rx), (0, ry), (0, 0), color = "darkviolet", linestyle = "dotted", label='j')
ax.plot((rx, rx), (ry, ry), (0, rz), color = "black", linestyle = "dotted", label='k')


# ----------    Efecto del "librito"    ----------
ax.plot((0, rx), (0, ry), (0, 0), color = "red", linestyle = "dotted")
ax.plot((0, rx), (0, ry), (rz, rz), color = "red", linestyle = "dotted")


# ----------    Curvas de los angulos   ----------
sgnRx = rx/np.absolute(rx)
sgnRy = ry/np.absolute(ry)
sgnRz = rz/np.absolute(rz)

# ->    Curva con respecto al eje z (angulo α)
# generacion de todos los valores de x 
x = np.linspace(0, (0.5 * rx * rz)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 100) 

# formulas
X = np.absolute(x) * sgnRx
Y = np.absolute((ry / rx) * x) * sgnRy
Z = sgnRz * np.sqrt((pow(rz, 2)/4) - pow(x, 2) * ((pow(rx, 2) + pow(ry, 2))/pow(rx, 2)))
ax.plot(X, Y, Z, color = "green")

# ->    Curva con respecto al eje y (angulo ɣ)
# generacion de todos los valores de y
z = np.linspace(0, (0.5 * rz * ry)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 100)

# formulas
X = np.absolute((rx / rz) * z) * sgnRx
Y = sgnRy * np.sqrt((pow(ry, 2)/4) - pow(z, 2) * ((pow(rx, 2) + pow(rz, 2))/pow(rz, 2)))
Z = np.absolute(z) * sgnRz 
ax.plot(X, Y, Z, color = "blue")

# ->    Curva con respecto al eje x (angulo β)
# generacion de todos los valores de x
y = np.linspace(0, (0.5 * ry * rx)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 100) 

# formulas
X = sgnRx * np.sqrt((pow(rx, 2)/4) - pow(y, 2) * ((pow(ry, 2) + pow(rz, 2))/pow(ry, 2)))
Y = np.absolute(y) * sgnRy
Z = np.absolute((rz / ry) * y) * sgnRz
ax.plot(X, Y, Z, color = "red")


plt.legend(loc = 'lower center', bbox_to_anchor=(0.3, -0.1, 0.5, 0.5), ncols = 6, draggable = True)
plt.tight_layout()
plt.show()

## NFALTA AGREGAR NOMBRES A LOS COSENOS SOBRE LA GRAFICA