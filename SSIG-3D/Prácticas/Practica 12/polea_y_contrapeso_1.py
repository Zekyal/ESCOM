
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation



#Dame la longitud del plano inclinado que desas trabajar:
l = 5000
#Dame el valor de la masa m1 (masa sobre la pendiente)
nv = 100
m_add = 0.01*nv
m_add_0 = -1.0/np.sqrt(2)
print('m_add = ', m_add)
mo = 1.0/np.sqrt(2)
m1 = 1
m2 =  m_add
print('m1, m2 =', m1, m2)
#gravedad
g = 9.81
#muk =  Dame el coeficiente de fricción cinética
#muk= 0.57
muk = 0.0
#mus = Dame el coeficiente de fricción estática
mus = 1.43*muk
#Dame el ángulo de la pendiente
theta =  85
theta_0 = np.arctan(mus)
theta_0 = np.degrees(theta_0)
print('(thetha, theta_0) = ', theta, theta_0)


theta_r = np.radians(theta)

theta = theta_r
N = m1*g*np.cos(theta)
Fxs = mus*N # Fuerza de fricción estática en X
Fxk = muk*N # Fuerza de fricción cinética en X
wx = m1*g*np.sin(theta)
wy = m1*g*np.cos(theta)

#fuerza mínima necesaria para partir del reposo
feqxs =  Fxs + wx
#fuerza minima necesaria para estar en movimiento ascendente
feqxk =  Fxk + wx

w2 = m2*g
#Calculamos la aceleración en X
acx = (1.0/(m1+m2))*(w2 - feqxk)
print('acx =', acx)
if acx<= 0:
   print('0_acx =', acx)
   if wx <= (w2 + Fxs) and acx <=0:
    acx = 0.0
    print('wx, w2+Fxs, 1_final_acx =', wx, w2 + Fxs, acx)
   else:
    acx =  ((Fxk + w2)-wx)*(1.0/(m1+m2))
    print('wx, w2 + Fxs, 2_final_acx =', wx, w2 + Fxs,  acx) 
else:
   acx = acx
   print('aceleració_final_acx =', acx)

# Definimos las ecuaciones de movimiento del primer punto en 3D
def movimiento1(t):
    #x = 0.01*pow(t,2)*np.cos((np.pi)/4.0)
    x1 = 0
    y1 = 0.5*acx*t*t*(np.cos(theta))
    #z = 0.01*pow(t,2)*np.sin((np.pi)/4.0)
    z1 = 0.5*acx*pow(t,2)*(np.sin(theta))

    return x1, y1, z1

# sea l la longitud del recorrido del cuerpo desplazado sobre el plano

xf = l*np.cos(theta)
yf = l*np.cos(theta)
zf = l*np.sin(theta)
# Definimos las ecuaciones de movimiento del segundo punto en 3D
def movimiento2(t):
  x2 = 0.0
  y2 = yf
  z2 = 0.5*zf - acx*0.5*pow(t,2)

  return x2, y2, z2

# Creamos la figura y el objeto para la animación
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
punto1, = ax.plot([], [], [], 'rs', markersize=10)
punto2, = ax.plot([], [], [], 'gs', markersize=10)
trayectoria1, = ax.plot([], [], [], 'r--')
trayectoria2, = ax.plot([], [], [], 'b--')



##############################################################


# Agregar etiquetas a los ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')


ax.set_xlim(-0.1*l, 0.1*l)
ax.set_ylim(-0.1*l, l)
ax.set_zlim(0, l)

#===================================================
#Genera el triángulo

x3 = [0,0,0,0,]
y3 = [0, l*np.cos(theta), l*np.cos(theta),0]
z3 = [0, l*np.sin(theta), 0,0]

ax.scatter(x3, y3, z3, c='r', marker='o')

plt.plot(x3,y3,z3, color='blue')

# Inicializamos las listas para almacenar las coordenadas de los puntos y las trayectorias
x1_punto1 = []
y1_punto1 = []
z1_punto1 = []
x1_trayectoria1 = []
y1_trayectoria1 = []
z1_trayectoria1 = []

x2_punto2 = []
y2_punto2 = []
z2_punto2 = []
x2_trayectoria2 = []
y2_trayectoria2 = []
z2_trayectoria2 = []



# Definimos la función que actualizará la posición de los puntos en cada fotograma
def actualizar(i):
    x1, y1, z1 = movimiento1(i)
    x2, y2, z2 = movimiento2(i)
    
    # Actualizamos las coordenadas y las trayectorias del primer punto
    x1_punto1.append(x1)
    y1_punto1.append(y1)
    z1_punto1.append(z1)
    punto1.set_data(x1, y1)
    punto1.set_3d_properties(z1)
    x1_trayectoria1.append(x1)
    y1_trayectoria1.append(y1)
    z1_trayectoria1.append(z1)
    trayectoria1.set_data(x1_trayectoria1, y1_trayectoria1)
    trayectoria1.set_3d_properties(z1_trayectoria1)

    # Actualizamos las coordenadas y las trayectorias del segundo punto
    x2_punto2.append(x2)
    y2_punto2.append(y2)
    z2_punto2.append(z2)
    punto2.set_data(x2, y2)
    punto2.set_3d_properties(z2)
    x2_trayectoria2.append(x2)
    y2_trayectoria2.append(y2)
    z2_trayectoria2.append(z2)
    trayectoria2.set_data(x2_trayectoria2, y2_trayectoria2)
    trayectoria2.set_3d_properties(z2_trayectoria2)

    if z2 >=l*np.sin(theta) or z2 <=0.0:
       ani.event.source.stop()
       

    return punto1, punto2, trayectoria1, trayectoria2

#Crea la animación
ani = animation.FuncAnimation(fig, actualizar, frames=np.linspace(0, 300, 3000),
                              interval=100, blit=True)



plt.show()

