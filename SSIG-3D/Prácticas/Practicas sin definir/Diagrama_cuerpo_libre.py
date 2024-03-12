import numpy as np
import matplotlib.pyplot as plt

theta = np.pi / 3.0  # Ángulo de la pendiente (theta)
alpha = np.pi / 8  # Ángulo de la fuerza F con respecto al eje X positivo (alpha)
magnitude = 6.8   # Magnitud del vector F (Fuerza externa) en [N]
m = 2.0
mk = 0.5  #Coeficiente de fricción cinética
ms = 0.7  #Coeficiente de fricción estática
g = 9.81  #gravedad

#Ajusta el tamaño de la salida de los ejes de la figura
maxval = {magnitude, m*g}
maxi = max(maxval)
print('maxi =', maxi)
maxi = int(1.1*maxi)


def rotate(points, angle):
    rotation_matrix = np.array([
        [np.cos(angle), np.sin(angle)],
        [-np.sin(angle), np.cos(angle)]
    ])
    return np.dot(points, rotation_matrix)

# Dibujar el sistema de coordenadas rotado y la fuerza F
fig, ax = plt.subplots()
ax.set_aspect('equal')

origin = np.array([[0, 0]])
x_axis = np.array([[maxi, 0], [-maxi, 0]])
y_axis = np.array([[0, maxi], [0, -maxi]])

rotated_x_axis = rotate(x_axis, theta)
rotated_y_axis = rotate(y_axis, theta)

#ax.arrow(0, 0, *rotated_x_axis[0], color='red', head_width=0.3, head_length=0.5)
#ax.arrow(0, 0, *rotated_y_axis[0], color='blue', head_width=0.3, head_length=0.5)
# Dibujar ejes positivos y negativos
ax.arrow(0, 0, *rotated_x_axis[0], color='red', head_width=0.3, head_length=0.5)
ax.arrow(0, 0, *rotated_x_axis[1], color='red', head_width=0.3, head_length=0.5)
ax.arrow(0, 0, *rotated_y_axis[0], color='blue', head_width=0.3, head_length=0.5)
ax.arrow(0, 0, *rotated_y_axis[1], color='blue', head_width=0.3, head_length=0.5)


# Calcular las componentes del vector F (fuerza_externa)
Fx = magnitude * np.cos(alpha)
Fy = magnitude * np.sin(alpha)

# Dibujar el vector F (fuerza_externa)
F = np.array([Fx, Fy])
F_rotated = rotate(F, theta)
ax.arrow(0, 0, *F_rotated, color='black', head_width=0.3, head_length=0.5)
F1 = magnitude
F1_r = round(F1, 2)
ax.text(*(1.1*F_rotated), f'F = {F1_r}', fontsize=10, color='black', rotation=np.degrees(theta))

#ax.text(*F_rotated, 'F', fontsize=12, color='gray', rotation=np.degrees(theta))

# Dibujar el vector Fx (Fuerza_externa_x)
Fx = np.array([Fx, 0])
F_rotatedx = rotate(Fx, theta)
ax.arrow(0, 0, *F_rotatedx, color='black', head_width=0.3, head_length=0.5)
F1x = magnitude*np.cos(alpha)
F1x_r = round(F1x, 2)
ax.text(*(0.7*F_rotatedx), f'Fx = {F1x_r}', fontsize=10, color='black', rotation=np.degrees(theta))


# Dibujar el vector Fy (Fuerza_externa_y)
Fy = np.array([0, Fy])
F_rotatedy = rotate(Fy, theta)
ax.arrow(0, 0, *F_rotatedy, color='black', head_width=0.3, head_length=0.5)
F1y = magnitude*np.sin(alpha)
F1y_r = round(F1y, 2)
ax.text(*(0.7*F_rotatedy), f'Fy = {F1y_r}', fontsize=10, color='black', rotation=np.degrees(theta))


# Etiquetas de los ejes en el extremo de cada eje
ax.text(*rotated_x_axis[0], 'X', fontsize=10, color='gray', rotation=np.degrees(theta))
ax.text(*rotated_y_axis[0], 'Y', fontsize=10, color='gray', rotation=np.degrees(theta))


#Calcula el vector del peso W
W = m*g
W = np.array([0, -W])
ax.arrow(0, 0, *W, color='cyan', head_width=0.3, head_length=0.5)
W1 = m * g 
W1_r = round(W1, 2)
ax.text(*(1.1*W), f'W = {W1_r}', fontsize=10, color='c', rotation=np.degrees(theta))

###################################
#Calcula el vector del peso Wy
Wy = m*g*np.cos(theta)
Wy = np.array([0, -Wy])
Wy = rotate(Wy, theta)
ax.arrow(0, 0, *Wy, color='cyan', head_width=0.3, head_length=0.5)
W1y = m*g*np.cos(theta)
W1y_r = round(W1, 2)
ax.text(*(0.6*Wy), f'Wy = {W1y_r}', fontsize=10, color='c', rotation=np.degrees(theta))



#Calcula el vector del peso Wx
Wx = m*g*np.sin(theta)
Wx = np.array([-Wx, 0])
Wx = rotate(Wx, 1.0*theta)
ax.arrow(0, 0, *Wx, color='cyan', head_width=0.3, head_length=0.5)
W1x = m*g*np.sin(theta)
W1x_r = round(W1x, 2)
ax.text(*(1.3*Wx), f'Wy = {W1x_r}', fontsize=10, color='c', rotation=np.degrees(theta))

#Calcula la fuerza Normal
Wy = m*g*np.cos(theta)
Fy = magnitude*np.sin(alpha)
N = -1.0*(Fy - Wy)  #Esto es porque la suma de las fuerzas en Y son cero, no hay aceleración en Y.
print('N :', N)
if  N <=0:
    print( 'El valor máximo permitido de Fy es:', Fy, '. Reduzca F o incremente {\alpha}')
    exit(0)
N = np.array([0, N])
N = rotate(N, theta)
ax.arrow(0, 0, *N, color='orange', head_width=0.3, head_length=0.5)
N1 = -1.0*(Fy - Wy)
N1_r = round(N1, 2)
ax.text(*(1.1*N), f'N = {N1_r}', fontsize=10, color='orange', rotation=np.degrees(theta))


#Calcular la fuerza de friccion



Wy = m*g*np.cos(theta)
Fy = magnitude*np.sin(alpha)
N = -1.0*(Fy - Wy)  #Esto es porque la suma de las fuerzas en Y son cero, no hay aceleración en Y.
print('N :', N)
Fk = N*mk
Fsmax = N*ms       #Fuerza de frición estática máxima
    #Calcula suma de fuerzas en X
sumx = (magnitude*np.cos(alpha) -m*g*np.sin(theta) - Fsmax )
acex = sumx/m
print ('acex1  =', acex)
if acex <= 0.0:
    acexi = (magnitude*np.cos(alpha) - m*g*np.sin(theta) + Fsmax  )
    print('acexi =', acexi)
    if acexi >=0:
        acex = 0.0
        print('Se mantiene en reposo con, acex  =', acex)
        Fsmax1 = -magnitude*np.cos(alpha) + m*g*np.sin(theta)
        Fsmax1 = np.array([Fsmax1, 0])
        Fsmax1 = rotate(Fsmax1, theta)
        ax.arrow(0, 0, *Fsmax1, color='m', head_width=0.3, head_length=0.5)
        Fk1 = -magnitude*np.cos(alpha) + m*g*np.sin(theta)
        Fk1_r = round(Fk1, 2)
        ax.text(*(1.01*Fsmax1), f'Fs = {Fk1_r}', fontsize=10, color='m', rotation=np.degrees(theta))

        ####################################################################################################################
          ##################################   CALCULA LA ACELERACIÓN EN X  ###############################################
        #####################################################################################################################
        # Configurar límites de la gráfica
        print('maxi  =', maxi)
        ax.set_xlim(-maxi, maxi)
        ax.set_ylim(-maxi, maxi)


        fig.suptitle('Diagrama de cuerpo libre', fontsize=16, fontweight='bold')
        ax.set_title(f'Se mantiene en reposo con una aceleración ={acex}', fontsize=14)

        # Ocultar el sistema de coordenadas original
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])

        plt.show()        
       # print ('hola')
        exit(0)
        ############################################################################################
    else:
        sumx =   (magnitude*np.cos(alpha) -m*g*np.sin(theta) + Fk)
        acex = sumx/m 
        print('Se acelera hacia abajo, con acex =  :', acex)
        Fsmax1 = N*mk
        Fsmax1 = np.array([Fsmax1, 0])
        Fsmax1 = rotate(Fsmax1, theta)
        ax.arrow(0, 0, *Fsmax1, color='m', head_width=0.3, head_length=0.5)
        Fk1 = N*mk
        Fk1_r = round(Fk1, 2)
        ax.text(*(0.2*Fsmax1), f'Fk = {Fk1_r}', fontsize=10, color='m', rotation=np.degrees(theta))

    

        # Configurar límites de la gráfica
        print('maxi   =', maxi)
        ax.set_xlim(-maxi, maxi)
        ax.set_ylim(-maxi, maxi)

        fig.suptitle('Diagrama de cuerpo libre', fontsize=16, fontweight='bold')
        ax.set_title(f'Se acelera hacia abajo con una aceleracion ={acex}', fontsize=14)

         # Ocultar el sistema de coordenadas original
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])

        plt.show()        
        exit(0)

else:

    sumx = (magnitude*np.cos(alpha) -m*g*np.sin(theta) - Fk )
    acex = sumx/m

    print('Se acelera hacia arriba con, acex  =', acex)



Fk = N*mk
Fk = np.array([-Fk, 0])
Fk = rotate(Fk, theta)
ax.arrow(0, 0, *Fk, color='m', head_width=0.3, head_length=0.5)
Fk1 = N*mk
Fk1_r = round(Fk1, 2)
ax.text(*(1.01*Fk), f'Fk = {Fk1_r}', fontsize=10, color='m', rotation=np.degrees(theta))


########################################################################################################

# Dibujar cuadrícula rotada
print(' maxi  =', maxi)
for i in np.linspace(-maxi, maxi, 2*maxi + 1):
    line_points = np.array([[-maxi, i], [maxi, i]])
    rotated_line_points = rotate(line_points, theta)
    ax.plot(rotated_line_points[:, 0], rotated_line_points[:, 1], color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

    line_points = np.array([[i, -maxi], [i, maxi]])
    rotated_line_points = rotate(line_points, theta)
    ax.plot(rotated_line_points[:, 0], rotated_line_points[:, 1], color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Configurar límites de la gráfica
ax.set_xlim(-maxi, maxi)
ax.set_ylim(-maxi, maxi)


fig.suptitle('Diagrama de cuerpo libre', fontsize=16, fontweight='bold')
ax.set_title(f'Se acelera hacia arriba con una aceleracion ={acex}', fontsize=14)

# Ocultar el sistema de coordenadas original
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

plt.show()

