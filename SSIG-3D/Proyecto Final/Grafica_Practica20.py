# Archivo con el proceso de graficación. Practica 20

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from mpl_toolkits import mplot3d
import numpy as np
import sympy as sp
from scipy.optimize import fsolve
from scipy.integrate import solve_ivp

#*************************** Clase de Gauss ***************************************************************************************************************************#
class Ley_Gauss(FigureCanvas):
    #------------------ Función Inicial---------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Gauss ---------------------------------------------------------------------------------------------------------------------------
    def graficar_gauss(self, theta_cone, valor):   

        # Parámetros de la esfera y el cono
        radius = 2
        #theta_cone = np.pi / 10  # Ángulo theta respecto al eje Z (30 grados en este caso)
        solid_angle = 2 * np.pi * (1 - np.cos(theta_cone))

        # Parámetros del elipsoide
        a = 1.5  # Semieje mayor en el eje x
        b = 2.5  # Semieje mayor en el eje y
        c = 1.7  # Semieje mayor en el eje z

        max_ax = 1.2*max(a, b, c)

        # Convertir el resultado en múltiplos de π
        solid_angle_pi = solid_angle / np.pi

        # Simplificar la fracción y mostrar el resultado en múltiplos de π
        fraction = sp.Rational(solid_angle_pi).limit_denominator(100)
        #print("Ángulo sólido subtendido por el cono:", fraction, "π estereorradianes")
        valor.setText("Ángulo sólido subtendido por el cono: " + str(fraction) + " π estereorradianes")

        ##########################################################################################

        # Coordenadas esféricas
        phi = np.linspace(0, 2 * np.pi, 100)
        theta = np.linspace(0, np.pi, 100)
        phi, theta = np.meshgrid(phi, theta)

        # Coordenadas cartesianas de la esfera
        x = radius * np.sin(theta) * np.cos(phi)
        y = radius * np.sin(theta) * np.sin(phi)
        z = radius * np.cos(theta)

        # Coordenadas cartesianas del elipsoide
        x_elipsoide = a*radius*np.sin(theta) * np.cos(phi)
        y_elipsoide = b*radius*np.sin(theta) * np.sin(phi)
        z_elipsoide = c*radius*np.cos(theta)

        # Coordenadas cilíndricas para el cono
        r_cone = np.linspace(0, max_ax*radius, 100)
        cone_phi = np.linspace(0, 2 * np.pi, 100)
        r_cone, cone_phi = np.meshgrid(r_cone, cone_phi)

        # Coordenadas cartesianas del cono
        cone_x = r_cone * np.sin(theta_cone) * np.cos(cone_phi)
        cone_y = r_cone * np.sin(theta_cone) * np.sin(cone_phi)
        cone_z = r_cone * np.cos(theta_cone)

        # Crear y configurar la figura y el objeto Axes3D
        self.ax.set_box_aspect([1, 1, 1])  # Establecer la misma escala en todos los ejes
        self.ax.axis('off')

        self.ax.set_xlim(-1.5*max_ax, 1.5*max_ax)
        self.ax.set_ylim(-1.5*max_ax, 1.5*max_ax)
        self.ax.set_zlim(-1.5*max_ax, 1.5*max_ax)

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        # Dibujar la esfera con un color azul suave y cierta transparencia
        self.ax.plot_surface(x, y, z, color='skyblue', alpha=0.3, rstride=1, cstride=1)

        # Dibujar el elipsoide con un color verde suave y cierta transparencia
        self.ax.plot_surface(x_elipsoide, y_elipsoide, z_elipsoide, color='orange', alpha=0.2, rstride=1, cstride=1)

        # Dibujar el cono con color gris y cierta transparencia
        self.ax.plot_surface(cone_x, cone_y, cone_z, color='gray', alpha=0.3, rstride=1, cstride=1)

        ################################################################################################
        #################CALCULA LA INTERSECCION ################################

        def equations(p, theta_cone, a, b, c, phi_3):
            r, theta_3 = p
            eq1 = radius * c * np.cos(theta_3) - r * np.cos(theta_cone)
            eq2 = r**2 - ((np.sin(theta_3))**2) * (pow(a * np.cos(phi_3), 2) + pow(b * np.sin(phi_3), 2)) - (c**2) * (np.cos(theta_3))**2
            return (eq1, eq2)

        def solve_equations(theta_cone, radius, a, b, c):
            phi_3 = np.linspace(0, 2 * np.pi, 100)

            x_3 = []
            y_3 = []
            z_3 = []

            for phi_a in phi_3:
                r, theta_3 = fsolve(equations, (1, 1), args=(theta_cone, a, b, c, phi_a))
            
                x_3.append(a*radius * np.sin(theta_3) * np.cos(phi_a))
                y_3.append(b*radius * np.sin(theta_3) * np.sin(phi_a))
                z_3.append(c*radius * np.cos(theta_3))

            return np.array(x_3), np.array(y_3), np.array(z_3)

        x_3, y_3, z_3 = solve_equations(theta_cone, radius, a, b, c)

        self.ax.axis('off')

        self.ax.scatter(x_3, y_3, z_3, color='green', s=1, alpha=0.5)

        ########################################################################################################
        # Máscara para el área intersectada por el cono
        mask1 = theta <= theta_cone
        # Coordenadas cartesianas de la intersección
        x_intersect1 = x[mask1]
        y_intersect1 = y[mask1]
        z_intersect1 = z[mask1]

        # Dibujar la intersección en color rojo
        self.ax.scatter(x_intersect1, y_intersect1, z_intersect1, color='red', s=1, alpha=1)

        ########################CALCULA EL CAMPO ELÉCTRICO ########################################################

        def electric_field(x, y, z, q, k):
            r = np.sqrt(x**2 + y**2 + z**2)
            Ex = k * q * x / r**3
            Ey = k * q * y / r**3
            Ez = k * q * z / r**3
            return Ex, Ey, Ez

        def field_line(t, pos, q, k):
            x, y, z = pos
            Ex, Ey, Ez = electric_field(x, y, z, q, k)
            return [Ex, Ey, Ez]

        q = 1e-9
        k = 8.9875517923e9

        #fig = plt.figure()
        #ax = fig.add_subplot(111, projection='3d')
        self.ax.set_title("Líneas de flujo y campo eléctrico de una carga puntual \n"
                    r"$\vec{E} = \frac{1}{4 \pi \epsilon_0} \frac{q}{|\vec{r}|^2} \hat{r}$ " )

        #subtitle = "Ley de Gauss\n" + r"$\int_{s} \vec{E} \dot d \vec{S} = \frac{q}{4 \pi \epsilon $" 
        #ax.text2D(0.5, 0.95, subtitle, transform=ax.transAxes, ha='center', fontsize=12)
        subtitle = ("Ley de Gauss :" 
                r"$\int_{s} \vec{E} \cdot d \vec{S} = \frac{q}{4 \pi \epsilon_0}$")
        self.ax.text2D(0.5, 0.95, subtitle, transform=self.ax.transAxes, ha='center', fontsize=12)

        # Dibuja líneas de flujo y vectores del campo eléctrico
        num_streamlines = 30
        num_vectors_per_streamline = 5

        for i in range(num_streamlines):
            theta = np.random.uniform(0, np.pi)
            phi = np.random.uniform(0, 2 * np.pi)
            x0 = 0.1 * np.sin(theta) * np.cos(phi)
            y0 = 0.1 * np.sin(theta) * np.sin(phi)
            z0 = 0.1 * np.cos(theta)

            sol = solve_ivp(field_line, [0, 5], [x0, y0, z0], args=(q, k), rtol=1e-6, atol=1e-6)
            #sol = fsolve(field_line, [0, 5], [x0, y0, z0], args=(q, k), rtol=1e-6, atol=1e-6)
            self.ax.plot(sol.y[0], sol.y[1], sol.y[2], color='blue', linestyle='dashed')

            # Dibuja vectores del campo eléctrico sobre las líneas de flujo
            num_points = len(sol.y[0])
            vector_indices = np.linspace(0, num_points-1, num_vectors_per_streamline, dtype=int)

            for idx in vector_indices:
                x, y, z = sol.y[0][idx], sol.y[1][idx], sol.y[2][idx]
                Ex, Ey, Ez = electric_field(x, y, z, q, k)
                E = np.sqrt(Ex**2 + Ey**2 + Ez**2)

                epsilon = 1e-9
                self.ax.quiver(x, y, z, Ex/(E + epsilon), Ey/(E + epsilon), Ez/(E + epsilon), length=0.5, color='red') 

            plt.tight_layout()
        
    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------------------------------------------------------------------------
    def cerrarGraf(self):
	    plt.close(self.fig)
