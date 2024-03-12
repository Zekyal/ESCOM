# Prueba Practica 03: Vector en sus componentes i, j, k

# Importacion de librerias
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
import numpy as np

# Insercion de valores
i = float(input('i = '))
j = float(input('j = '))
k = float(input('k = '))

# -------------------- GRAFICACION --------------------
fig = plt.figure()
ax = plt.axes(projection = '3d')
# Titulo de la grafica
plt.suptitle("Grafica de un Vector")
# Nombres de los ejes
ax.set_xlabel("PosiciónX", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
ax.set_ylabel("PosiciónY", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_zlabel("PosiciónZ", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})

# Ejes de la grafica
ax.plot((abs(i)+50, 0), (0, 0), (0, 0), color = "orange", label='X(+)')
ax.plot((0, -abs(i)-50), (0, 0), (0, 0), color = "red", label='X(-)')
ax.plot((0, 0), (abs(j)+50, 0), (0, 0), color = "green", label='Y(+)')
ax.plot((0, 0), (0, -abs(j)-50), (0, 0), color = "blue", label='Y(-)')
ax.plot((0, 0), (0, 0), (abs(k)+50, 0), color = "yellow", label='Z(+)')
ax.plot((0, 0), (0, 0), (0, -abs(k)-50), color = "brown", label='Z(-)')

# Ejes i, j y k traslapados
ax.plot((0, i), (j, j), (0, 0), color = "cyan", linestyle = "dashed", label='i')
ax.plot((i, i), (0, j), (0, 0), color = "darkviolet", linestyle = "dashed", label='j')
ax.plot((i, i), (j, j), (0, k), color = "black", linestyle = "dashed", label='k')

# Ejes i, j y k en el origen
#ax.plot((0, i), (0, 0), (0, 0), color = "cyan", linestyle = "dashed")
#ax.plot((0, 0), (0, j), (0, 0), color = "darkviolet", linestyle = "dashed")
#ax.plot((0, 0), (0, 0), (0, k), color = "black", linestyle = "dashed")
ax.quiver(0, 0, 0, i, 0, 0, arrow_length_ratio=0.1, color = "cyan")
ax.quiver(0, 0, 0, 0, j, 0, arrow_length_ratio=0.1, color = "darkviolet")
ax.quiver(0, 0, 0, 0, 0, k, arrow_length_ratio=0.1, color = "black")

# r (Solo sirve para darle el efecto de librito)
ax.plot((0, i), (0, j), (0, 0), color = "red", linestyle = "dashed")
ax.plot((0, i), (0, j), (k, k), color = "red", linestyle = "dashed")

# Vector
ax.quiver(0, 0, 0, i, j, k, arrow_length_ratio=0.1, label='Vector')

plt.legend()
plt.show()