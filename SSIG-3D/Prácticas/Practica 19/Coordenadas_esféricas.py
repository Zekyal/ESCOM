import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_sphere(radius, theta, phi, v_r,v_t,v_p): 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Parámetros de la esfera
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

    # Dibujar esfera
    ax.plot_surface(x, y, z, color='orange', alpha=0.3)

    # Dibujar círculo rojo paralelo al plano XY
    phi_red = np.linspace(0, 2 * np.pi, 100)
    x_red = radius * np.sin(theta) * np.cos(phi_red)
    y_red = radius * np.sin(theta) * np.sin(phi_red)
    z_red = radius * np.cos(theta) * np.ones_like(phi_red)
    ax.plot(x_red, y_red, z_red, linestyle='dashed', color='red')

 # Dibujar El ecuador plano XY
    phi_red = np.linspace(0, 2 * np.pi, 100)
    x_red = radius * np.sin(pi/2) * np.cos(phi_red)
    y_red = radius * np.sin(pi/2) * np.sin(phi_red)
    z_red = radius * np.cos(pi/2) * np.ones_like(phi_red)
    ax.plot(x_red, y_red, z_red, linestyle='dashed', color='black')

    # Dibujar círculo azul perpendicular al plano XY
    theta_blue = np.linspace(0,2*np.pi, 100)
    x_blue = radius * np.sin(theta_blue) * np.cos(phi)
    y_blue = radius * np.sin(theta_blue) * np.sin(phi)
    z_blue = radius * np.cos(theta_blue)
    ax.plot(x_blue, y_blue, z_blue, linestyle='dashed', color='blue')

    # Dibujar ejes ortogonales
    ax.quiver(0, 0, 0, radius, 0, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, radius, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 0, radius, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, -radius, 0, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, -radius, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 0, -radius, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)

    # Agregar etiquetas a los ejes
    ax.text(radius, 0, 0, 'X', fontsize=12)
    ax.text(0, radius, 0, 'Y', fontsize=12)
    ax.text(0, 0, radius, 'Z', fontsize=12)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Esfera de radio {radius}')

# Dibujar vector desde el origen al punto (r*sin(theta)*cos(phi), r*sin(theta)*sin(phi), r*cos(theta))
    vector_x = radius * np.sin(theta) * np.cos(phi)
    vector_y = radius * np.sin(theta) * np.sin(phi)
    vector_z = radius * np.cos(theta)
    ax.quiver(0, 0, 0, vector_x, vector_y, vector_z, color='green', linewidth=1.5, arrow_length_ratio=0.1)

# Línea 1
    x1_start, y1_start, z1_start = 0, 0, 0
    x1_end, y1_end, z1_end = vector_x, vector_y, 0
    ax.plot([x1_start, x1_end], [y1_start, y1_end], [z1_start, z1_end], linestyle='dotted', color='black')

# Línea 2
    x2_start, y2_start, z2_start = x1_end, y1_end, z1_end
    x2_end, y2_end, z2_end = vector_x, vector_y, vector_z
    ax.plot([x2_start, x2_end], [y2_start, y2_end], [z2_start, z2_end], linestyle='dotted', color='black')

# Línea 3
    x3_start, y3_start, z3_start = 0, 0, vector_z
    #x3_end, y3_end, z3_end = x2_end, y2_end, z2_end
    x3_end, y3_end, z3_end = vector_x, vector_y, vector_z
    ax.plot([x3_start, x3_end], [y3_start, y3_end], [z3_start, z3_end], linestyle='dotted', color='black')

# Dibujar vector desde el origen al punto (r*sin(theta)*cos(phi), r*sin(theta)*sin(phi), r*cos(theta))
    vector_x = radius * np.sin(theta) * np.cos(phi)
    vector_y = radius * np.sin(theta) * np.sin(phi)
    vector_z = radius * np.cos(theta)
    ax.quiver(0, 0, 0, vector_x, vector_y, vector_z, color='green', linewidth=1.5, arrow_length_ratio=0.1)

    # Dibujar vectores unitarios v_r, v_t y v_p
    #ax.quiver(vector_x, vector_y, vector_z, v_r[0], v_r[1], v_r[2], color='green', linewidth=1.5, arrow_length_ratio=0.1)
    #ax.quiver(vector_x, vector_y, vector_z, v_t[0], v_t[1], v_t[2], color='blue', linewidth=1.5, arrow_length_ratio=0.1)
    #ax.quiver(vector_x, vector_y, vector_z, v_p[0], v_p[1], v_p[2], color='red', linewidth=1.5, arrow_length_ratio=0.1)

# Dibujar vectores unitarios v_r, v_t y v_p y agregar etiquetas de texto
    ax.quiver(vector_x, vector_y, vector_z, v_r[0], v_r[1], v_r[2], color='green', linewidth=1.5, arrow_length_ratio=0.1)
    ax.text(vector_x + v_r[0], vector_y + v_r[1], vector_z + v_r[2], r'$\hat{r}$', fontsize=10)

    ax.quiver(vector_x, vector_y, vector_z, v_t[0], v_t[1], v_t[2], color='blue', linewidth=1.5, arrow_length_ratio=0.1)
    ax.text(vector_x + v_t[0], vector_y + v_t[1], vector_z + v_t[2], r'$\hat{\theta}$', fontsize=10)

    ax.quiver(vector_x, vector_y, vector_z, v_p[0], v_p[1], v_p[2], color='red', linewidth=1.5, arrow_length_ratio=0.1)
    ax.text(vector_x + v_p[0], vector_y + v_p[1], vector_z + v_p[2], r'$\hat{\phi}$', fontsize=10)

  # Agregar título y subtítulos
    ax.set_title('Coordenadas Esféricas')

    subt1 = r'$\hat{{\theta}} = ({:.3f}, {:.3f}, {:.3f})$'.format(v_t[0], v_t[1], v_t[2])
    subt2 = r'$\hat{{\phi}} = ({:.3f}, {:.3f}, {:.3f})$'.format(v_p[0], v_p[1], v_p[2])
    ax.text2D(0.05, 0.92, subt1, transform=ax.transAxes)
    ax.text2D(0.05, 0.88, subt2, transform=ax.transAxes)
    plt.show()


# Ejemplo de uso
pi = np.pi
v_x = np.array([1,0,0])
v_y = np.array([0,1,0])
v_z = np.array([0,0,1])

# Pedir la coordenada en X del vector
x_str = input("Por favor igresa el valor de la coordenada en X = ")
# Convertir la cadena de texto a un número de punto flotante
x_v = float(x_str)
# Pedir la coordenada en X del vector
y_str = input("Por favor igresa el valor de la coordenada en Y=  ")
# Convertir la cadena de texto a un número de punto flotante
y_v = float(y_str)
# Pedir la coordenada en X del vector
z_str = input("Por favor igresa el valor de la coordenada en Z=  ")
# Convertir la cadena de texto a un número de punto flotante
z_v = float(z_str)
radio = np.sqrt(pow(x_v,2) + pow(y_v,2) +pow(z_v,2))

#Calcula ángulo theta y ángulo phi
if x_v ==0 and y_v>0:
    angulo_phi = 0.5*pi
if x_v ==0 and y_v<0:
    angulo_phi = 1.5*pi
if y_v == 0 and x_v > 0:
    angulo_phi = 0
if y_v ==0 and x_v < 0:
    angulo_phi = pi
if x_v == 0 and y_v == 0:
    angulo_theta = 0
    angulo_phi = 0    
if x_v != 0:   
    angulo_phi = np.arctan(y_v/x_v)  

angulo_theta = np.arccos(z_v/radio)     
print('angulo_theta, angulo_phi =  ', angulo_theta, angulo_phi)
#exit(0)

v_r = np.sin(angulo_theta)*np.cos(angulo_phi)*v_x + np.sin(angulo_theta)*np.sin(angulo_phi)*v_y + np.cos(angulo_theta)*v_z
v_t = np.cos(angulo_theta)*np.cos(angulo_phi)*v_x + np.cos(angulo_theta)*np.sin(angulo_phi)*v_y - np.sin(angulo_theta)*v_z
v_p = -np.sin(angulo_phi)*v_x + np.cos(angulo_phi)*v_y


print("v_r:", v_r)
print("v_t:", v_t)
print("v_p:", v_p)


draw_sphere(radio, angulo_theta, angulo_phi,v_r,v_t,v_p)
