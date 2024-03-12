# Prueba Practica 07: Componentes y cosenos directores de un vector


import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#from mpl_toolkits.mplot3d.art3d import Line3DCollection

# Banderita improvisada 2: El regreso
print("Dadas las coordenadas obtener los cosenos directores (α, β y ɣ) y la magnitud de un vector y sus componentes")

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
    print("No se puede graficar ya que: |v| =",0)
    exit(00)
else:
    alpha = np.arccos(np.absolute(rz) / magnitud)
    beta = np.arccos(np.absolute(rx) / magnitud)
    gamma = np.arccos(np.absolute(ry) / magnitud)
    
    alphaDeg = np.degrees(alpha)
    betaDeg = np.degrees(beta)
    gammaDeg = np.degrees(gamma)
    
    respuesta = (pow(np.cos(alpha), 2) + pow(np.cos(beta), 2) + pow(np.cos(gamma), 2)) 

    # Impresion de resultados
    print("|v| =",magnitud)
    print("Coseno director respecto al eje Z, α =", alpha, "rad /", alphaDeg, "°")
    print("Coseno director respecto al eje Y, β =", beta,  "rad /", betaDeg, "°")
    print("Coseno director respecto al eje X, ɣ =", gamma, "rad /", gammaDeg, "°")
    print('cos**2(α) + cos**2(β) + cos**2(ɣ) =', respuesta )
    
# Obtencion de un vector a partir de sus cosenos directores y magnitud

# -------------------- GRAFICACION --------------------

fig = plt.figure()
ax = plt.axes(projection = '3d')
# Titulo de la grafica
plt.suptitle("Grafica de un Vector")
# Nombres de los ejes
ax.set_xlabel("Posición_X", fontdict = {'fontsize':10, 'fontweight':'normal', 'color':'blue'})   # Inserta el nombre al eje X
ax.set_ylabel("Posición_Y", fontdict = {'fontsize':10, 'fontweight':'normal', 'color':'blue'})
ax.set_zlabel("Posición_Z", fontdict = {'fontsize':10, 'fontweight':'normal', 'color':'blue'})


# ----------   Dibuja  Vector  ----------
if rx == 0 or ry ==0 or rz ==0: 
  ax.quiver(0,0,0, rx, ry, rz, arrow_length_ratio=0.1, color = 'black' )

  var1x = "X"
  var2x = "X"
  var1y = "Y"
  var2y = "-Y"
  var1z = "Z"
  var2z = "-Z" 
  if rx == 0:
    rx = magnitud
  else:
    rx = rx + 0.2*magnitud*np.sign(rx)
  if ry ==0:
     ry=magnitud
  else:     
     ry = ry + 0.2*magnitud*np.sign(ry)
  if rz ==0:  
     rz = magnitud
  else:     
     rz = rz + 0.2*magnitud*np.sign(rz)

#dibuja el nombre del eje correspondiente al final de este
  ax.text(1.05*rx, 0, 0, var1x, color='blue', fontsize=12, fontweight='normal')
  ax.text(0, 1.05*ry, 0, var1y, color='blue', fontsize=12, fontweight='normal')
  ax.text(0, 0, 1.05*rz, var1z, color='blue', fontsize=12, fontweight='normal')
  ax.text(-0.2*rx, 0, 0, var2x, color='blue', fontsize=12, fontweight='normal')
  ax.text(0, -0.2*ry, 0, var2y, color='blue', fontsize=12, fontweight='normal')
  ax.text(0, 0, -0.2*rz, var2z, color='blue', fontsize=12, fontweight='normal')

# ----------   Ejes de la grafica    ----------
  ax.plot((rx, -0.2*rx), (0, 0), (0, 0), color = "orange", label='X')
#ax.plot((0, -0.2*rx), (0, 0), (0, 0), color = "orange", label='X(-)')
  ax.plot((0, 0), (1.0*ry, -0.2*ry), (0, 0), color = "green", label='Y')
#ax.plot((0, 0), (0, -0.2*ry), (0, 0), color = "green", label='Y(-)')
  ax.plot((0, 0), (0, 0), (1.0*rz, -0.2*rz), color = "cyan", label='Z')
#ax.plot((0, 0), (0, 0), (0, -0.2*rz), color = "cyan", label='Z(-)')  



  plt.legend(loc = 'lower center', bbox_to_anchor=(0.3, -0.1, 0.5, 0.5), ncols = 6, draggable = True)
  plt.tight_layout()
  plt.show()

  exit(0)

else: 


#cambia los signos de los ejes coordenados

#var1y = "Y"
#var2y = "-Y"
#var1z = "Z"
#var2z = "-Z"

    srx = np.sign(rx)
if (srx==1):
             var1x = 'X'
             var2x ='-X'
else:
             var1x = '-X'  
             var2x = 'X'

sry = np.sign(ry)

if (sry==1):
             var1y = 'Y'
             var2y ='-Y'
else:
             var1y = '-Y'  
             var2y = 'Y'

srz = np.sign(rz)

if (srz==1):
             var1z = 'Z'
             var2z ='-Z'
else:
             var1z = '-Z'  
             var2z = 'Z'



#dibuja el nombre del eje correspondiente al final de este
ax.text(1.05*rx, 0, 0, var1x, color='blue', fontsize=12, fontweight='normal')
ax.text(0, 1.05*ry, 0, var1y, color='blue', fontsize=12, fontweight='normal')
ax.text(0, 0, 1.05*rz, var1z, color='blue', fontsize=12, fontweight='normal')
ax.text(-0.2*rx, 0, 0, var2x, color='blue', fontsize=12, fontweight='normal')
ax.text(0, -0.2*ry, 0, var2y, color='blue', fontsize=12, fontweight='normal')
ax.text(0, 0, -0.2*rz, var2z, color='blue', fontsize=12, fontweight='normal')

# ----------   Ejes de la grafica    ----------
ax.plot((rx, -0.2*rx), (0, 0), (0, 0), color = "orange", label='X')
#ax.plot((0, -0.2*rx), (0, 0), (0, 0), color = "orange", label='X(-)')
ax.plot((0, 0), (1.0*ry, -0.2*ry), (0, 0), color = "green", label='Y')
#ax.plot((0, 0), (0, -0.2*ry), (0, 0), color = "green", label='Y(-)')
ax.plot((0, 0), (0, 0), (1.0*rz, -0.2*rz), color = "cyan", label='Z')
#ax.plot((0, 0), (0, 0), (0, -0.2*rz), color = "cyan", label='Z(-)')




ax.quiver(0,0,0, rx, ry, rz, arrow_length_ratio=0.1, color = 'black' )

rx1 =rx
ry1 = ry
rz1 = rz



#========================================================================
# nombre del vector
ax.text(rx1, ry1, rz1, f"({rx},{ry},{rz})", style='normal', fontweight='normal', color = 'blue')
#ax.text(rx, ry, rz, 'vector', style='italic', fontweight='normal', color = 'red')

#=============recupera sus valores==========

# ----------    Componentes i, j y k   ----------
ax.quiver(0, 0, 0, rx, 0, 0, arrow_length_ratio=0.1, color = "black",  alpha = 0.7, linestyle = '--' )
ax.quiver(0, 0, 0, 0, ry, 0, arrow_length_ratio=0.1, color = "black", alpha = 0.7, linestyle = '--' )
ax.quiver(0, 0, 0, 0, 0, rz, arrow_length_ratio=0.1, color = "black", alpha = 0.7, linestyle = '--' )
# nombres de los ejes
ax.text(rx/2, 0, 0, 'rx_i', style='italic', fontweight='bold', color = "black")
ax.text(0, ry/2, 0, 'ry_j', style='italic', fontweight='bold', color = "black")
ax.text(0, 0, rz/2, 'rz_k', style='italic', fontweight='bold', color = "black")


# ----------    Componentes i, j y k traslapados   ----------
ax.plot((0, rx), (ry, ry), (0, 0), color = "black", linestyle = "dotted")
ax.plot((rx, rx), (0, ry), (0, 0), color = "black", linestyle = "dotted")
ax.plot((rx, rx), (ry, ry), (0, rz), color = "black", linestyle = "dotted")


# ----------    Efecto del "librito"    ----------
ax.plot((0, rx), (0, ry), (0, 0), color = "gray", linestyle = "dotted")
ax.plot((0, rx), (0, ry), (rz, rz), color = "green", linestyle = "dotted")

#-----Efecto planos inclinados ---------

ax.plot((0, rx), (ry, ry), (0, rz), color = "blue", linestyle = "dotted")
ax.plot((rx, rx), (0, ry), (0, rz), color = "red", linestyle = "dotted")



# ----------    Curvas de los angulos   ----------
sgnRx = rx/np.absolute(rx)
sgnRy = ry/np.absolute(ry)
sgnRz = rz/np.absolute(rz)

# ->    Curva con respecto al eje z (angulo α)
# generacion de todos los valores de x 
x = np.linspace(0, (0.5 * rx * rz)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 1000) 

# formulas
X = np.absolute(x) * sgnRx
Y = np.absolute((ry / rx) * x) * sgnRy
Z = sgnRz * np.sqrt((pow(rz, 2)/4) - pow(x, 2) * ((pow(rx, 2) + pow(ry, 2))/pow(rx, 2)))
ax.plot(X, Y, Z, color = "green", label = 'α')

# ->    Curva con respecto al eje y (angulo ɣ)
# generacion de todos los valores de y
z = np.linspace(0, (0.5 * rz * ry)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 1000)

# formulas
X = np.absolute((rx / rz) * z) * sgnRx
Y = sgnRy * np.sqrt((pow(ry, 2)/4) - pow(z, 2) * ((pow(rx, 2) + pow(rz, 2))/pow(rz, 2)))
Z = np.absolute(z) * sgnRz 
ax.plot(X, Y, Z, color = "blue", label = 'ɣ')

# ->    Curva con respecto al eje x (angulo β)
# generacion de todos los valores de x
y = np.linspace(0, (0.5 * ry * rx)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 1000) 

# formulas
X = sgnRx * np.sqrt((pow(rx, 2)/4) - pow(y, 2) * ((pow(ry, 2) + pow(rz, 2))/pow(ry, 2)))
Y = np.absolute(y) * sgnRy
Z = np.absolute((rz / ry) * y) * sgnRz

ax.plot(X, Y, Z, color = "red", label = 'β')


plt.legend(loc = 'lower center', bbox_to_anchor=(0.3, -0.1, 0.5, 0.5), ncols = 6, draggable = True)
plt.tight_layout()
plt.show()

## NFALTA AGREGAR NOMBRES A LOS COSENOS SOBRE LA GRAFICA