## Archivo para el módulo de "Campo Eléctrico"

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from mpl_toolkits import mplot3d
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import griddata
from scipy.optimize import fsolve
import sympy as sp

#*************************** Clase de Campo Eléctrico *****************************************************************************************************************#
class Campo_Electrico(FigureCanvas):
    #------------------ Función Inicial--------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        super().__init__(self.fig)

    #------------ Grafica de Campos Eléctricos -----------------------------------------------------------------------------------------------------------------------
    def graficar_camp_elect(self):    
        # Definir constantes
        k = 9e9  # Constante de Coulomb

        # Definir la función que calcula el campo eléctrico
        def E(q, r0, x, y, z):
            """
            q: Carga de la partícula en Coulombs.
            r0: Posición de la partícula como una tupla (x, y, z).
            x, y, z: Puntos donde queremos calcular el campo eléctrico.
            """
            den = np.sqrt((x - r0[0])**2 + (y - r0[1])**2 + (z - r0[2])**2)**3
            return k * q * (x - r0[0]) / den, k * q * (y - r0[1]) / den, k * q * (z - r0[2]) / den

        # Crear una malla de puntos en el espacio tridimensional
        x, y, z = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))

        # Loop para graficar tanto la carga positiva como la negativa
        for i, q in enumerate([1.0, -1.0]):

            # Calcular el campo eléctrico en cada punto de la malla
            Ex, Ey, Ez = E(q, (0, 0, 0), x, y, z)

            # Definir la posición y tamaño del subplot
            left = 0.1
            bottom = 0.55 - i*0.45
            width = 0.8
            height = 0.4

            # Crear un nuevo subplot para cada carga
            self.ax = self.fig.add_axes([left, bottom, width, height], projection='3d')

            # Dibujar la carga como un punto en el centro
            if q > 0:
                self.ax.scatter([0], [0], [0], color='red', s=100)
                self.ax.set_title('Líneas de campo eléctrico de una carga positiva', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

                # Color de Fondo
                self.ax.set_facecolor("darkgrey")
                self.ax.grid(False)
                self.ax.set_xticks([])
                self.ax.set_yticks([])
                self.ax.set_zticks([])

            else:
                self.ax.scatter([0], [0], [0], color='blue', s=100)
                self.ax.set_title('Líneas de campo eléctrico de una carga negativa', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

                # Color de Fondo
                self.ax.set_facecolor("darkgrey")
                self.ax.grid(False)
                self.ax.set_xticks([])
                self.ax.set_yticks([])
                self.ax.set_zticks([])

            # Dibujar las líneas de campo eléctrico
            self.ax.quiver(x, y, z, Ex, Ey, Ez, length=0.1, normalize=True)

            # Configurar los límites de los ejes
            self.ax.set_xlim([-1, 1])
            self.ax.set_ylim([-1, 1])
            self.ax.set_zlim([-1, 1])

    #------------ Grafica de Campo Eléctrico (FIN) --------------------------------------------------------------------------------------------------------

    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------------------------------------------------------------------------

#*************************** Clase de Campo Eléctrico (FIN) ***********************************************************************************************************#

#*************************** Clase de Lineas de Flujos ****************************************************************************************************************#
class Camp_Elec_Flujos(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica Lineas de Flujo ---------------------------------------
    def graficar_lineas_flujos(self):    
        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")
        self.ax.grid(False)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_zticks([])

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

        plt.suptitle("Líneas de flujo y campo eléctrico de una carga puntual\n"
                    r"$\vec{E} = \frac{1}{4 \pi \epsilon_0} \frac{q}{|\vec{r}|^2} \hat{r}$")

        #self.ax.set_xticks([])
        #self.ax.set_yticks([])
        #self.ax.set_zticks([])

        # Dibuja líneas de flujo y vectores del campo eléctrico
        num_streamlines = 45
        num_vectors_per_streamline = 5

        for i in range(num_streamlines):
            theta = np.random.uniform(0, np.pi)
            phi = np.random.uniform(0, 2 * np.pi)
            x0 = 0.1 * np.sin(theta) * np.cos(phi)
            y0 = 0.1 * np.sin(theta) * np.sin(phi)
            z0 = 0.1 * np.cos(theta)

            sol = solve_ivp(field_line, [0, 5], [x0, y0, z0], args=(q, k), rtol=1e-6, atol=1e-6)
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

    #------------ Grafica Lineas de Flujo (FIN) ----------------------------------

    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------------------------------------------------------------------------

#*************************** Clase de Dipolo **************************************************************************************************************************#
class Camp_Elec_Dipolo(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica Dipolo ------------------------------------------------
    def graficar_dipolo(self):    

        #self.ax.set_title('Campo Magnético de Cables Infinitos Paralelos Transportando Corriente (I)', loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        self.ax.grid(False)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_zticks([])


        def electric_field(x, y, z, q1, q2, k, d):
            r1 = np.array([x - d/2, y, z])
            r2 = np.array([x + d/2, y, z])

            smoothing_factor = 1e-12
            r1_mag = np.sqrt(np.sum(r1**2) + smoothing_factor)
            r2_mag = np.sqrt(np.sum(r2**2) + smoothing_factor)

            E1 = k * q1 / r1_mag**3 * r1
            E2 = k * q2 / r2_mag**3 * r2

            E_total = E1 + E2
            return E_total[0], E_total[1], E_total[2]

        def field_line(t, pos, q1, q2, k, d):
            x, y, z = pos
            Ex, Ey, Ez = electric_field(x, y, z, q1, q2, k, d)
            return [Ex, Ey, Ez]

        def stop_event(t, y, q1, q2, k, d):
            return np.sqrt((y[0] - (-d/2))**2 + y[1]**2 + y[2]**2) - distance_threshold

        stop_event.terminal = True

        k = 8.9875517923e9
        q1 = 25e-19
        q2 = -25e-19
        d = 1e-3
        distance_threshold = 1e-3 * d

        #self.ax.set_title("Líneas de flujo y campo eléctrico para dos cargas", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        plt.suptitle("Líneas de flujo y campo eléctrico para dos cargas")  
        # condiciones iniciales

        theta_divisions = 5  #numero de divisiones en theta (angulo en esféricas respecto al eje Z)
        phi_divisions = 9    #número de divisiones en phi  (ángulo respecto al eje x)

        event_positions = []
        num_vectors_per_streamline = 8

        for i in range(theta_divisions):
            for j in range(phi_divisions):
                theta = i * np.pi / theta_divisions
                phi = j * 2 * np.pi / phi_divisions

                x0 = d/2 + distance_threshold * np.sin(theta) * np.cos(phi)
                y0 = distance_threshold * np.sin(theta) * np.sin(phi)
                z0 = distance_threshold * np.cos(theta)

                sol = solve_ivp(field_line, [0, 12], [x0, y0, z0], args=(q1, q2, k, d), rtol=1e-8, atol=1e-8, events=stop_event)

                if sol.status == 1:  # Event was triggered, indicating close proximity to q2
                    sol.t_events[0] = np.append(sol.t_events[0], sol.t[-1])
                    event_positions.append(sol.y[:, -1].reshape(3, 1))

                self.ax.plot(sol.y[0], sol.y[1], sol.y[2], color='blue', linestyle='dashed')

                num_points = len(sol.y[0])
                vector_indices = np.linspace(0, num_points - 1, num_vectors_per_streamline, dtype=int)

                for idx in vector_indices:
                    x, y, z = sol.y[0][idx], sol.y[1][idx], sol.y[2][idx]
                    Ex, Ey, Ez = electric_field(x, y, z, q1, q2, k, d)
                    E = np.sqrt(Ex**2 + Ey**2 + Ez**2)

                    epsilon = 1e-9
                    self.ax.quiver(x, y, z, Ex/(E + epsilon), Ey/(E + epsilon), Ez/(E + epsilon), length=0.3*d, color='red')
        event_positions = np.hstack(event_positions)

        self.ax.set_xlim([-2*d, 2*d])
        self.ax.set_ylim([-2*d, 2*d])
        self.ax.set_zlim([-2*d, 2*d])

        plt.tight_layout()
    #------------ Grafica Dipolo (FIN) -------------------------------

    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------------------------------------------------------------------------

#*************************** Clase de Dipolo (FIN) *********************************************************************************************************************#

#*************************** Clase de Potencial Electrostático *********************************************************************************************************#
class Camp_Elec_Potencial(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    #------------ Grafica Potencial ------------------------------------------------
    def graficar_potencial(self):

        # Definir los valores de rho y phi
        rho_values = np.linspace(0, 1, 200)
        phi_values = np.linspace(0, 2*np.pi, 200)

        # Definir las coordenadas de los puntos rojo y azul
        a = 0.1
        k = 2 # Factor para incrementar los ejes
        x_red = -a
        y_red = 0.0
        x_blue = a
        y_blue = 0.0

        # Definir los parámetros de la función
        lambda_ = 5.0e-8    #[C/m]
        epsilon =  8.85e-12 # [C^2/N m^2]

        # Calcular y dibujar las líneas de campo eléctrico
        x_values = []
        y_values = []
        result_values = []
        for rho in rho_values:
            for phi in phi_values:
                numerator = a**2 + rho**2 + 2*a*rho*np.cos(phi)
                denominator = a**2 + rho**2 - 2*a*rho*np.cos(phi)
                result = lambda_ / (4*np.pi*epsilon) * np.log(numerator / denominator)
                x = rho * np.cos(phi)
                y = rho * np.sin(phi)
                x_values.append(x)
                y_values.append(y)
                result_values.append(result)

        # Crear una cuadrícula cartesiana regular
        xi = np.linspace(min(x_values), max(x_values), 500)
        yi = np.linspace(min(y_values), max(y_values), 500)
        xi, yi = np.meshgrid(xi, yi)

        # Interpolar los datos en la cuadrícula
        zi = griddata((x_values, y_values), result_values, (xi, yi), method='cubic')

        # Dibujar el mapa de colores
        plt.pcolormesh(xi, yi, zi, cmap='hot')
        # Definir los límites de los ejes
        plt.xlim(-k*a, k*a)  # Cambia los números según tus necesidades
        plt.ylim(-k*a, k*a)  # Cambia los números según tus necesidades
        #plt.axis('equal')

        # Dibujar las líneas de equipotencial
        contour_values = np.linspace(np.min(result_values), np.max(result_values), 19)  # 9 contornos incluyen 4 a cada lado y 1 en el medio
        contours = plt.contour(xi, yi, zi, contour_values, colors='black')
        plt.clabel(contours, inline=True, fontsize=8)

        # Dibujar los puntos rojo y azul
        plt.scatter(x_red, y_red, color='blue')
        plt.scatter(x_blue, y_blue, color='red')

        # Agregar una barra de colores
        cbar = plt.colorbar()
        cbar.set_label('Potencial')

        # ...
        # Mostrar el gráfico
        plt.suptitle(r'Potencial electrostático producido por dos líneas de carga opuestas: $\frac{\lambda}{4\pi\epsilon}\ln\left(\frac{a^{2} + \rho^{2}  + 2a\rho\cos(\phi)}{a^{2} + \rho^{2}  - 2a\rho\cos(\phi)}\right)$')
        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Agregar las etiquetas a los ejes
        plt.xlabel('Posición_X [m]')
        plt.ylabel('Posición_Y [m]')
        
        plt.tight_layout()
    #------------ Grafica Potencial (FIN) -------------------------------

    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------------------------------------------------------------------------

#*************************** Clase de Potencial Electrostático (FIN) ***************************************************************************************************#