# Archivo con el proceso de graficación y animaciones. Practica 18

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from mpl_toolkits import mplot3d
import numpy as np
from matplotlib.colors import LightSource
from scipy.integrate import solve_ivp

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Camp_Elec_Coulumb(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        super().__init__(self.fig)

    #------------ Grafica (muestra) -------------------------------------
    def graficar_muestra(self):    
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

            # Crear un nuevo subplot para cada carga
            self.ax = self.fig.add_subplot(1, 2, i + 1, projection='3d')

            # Dibujar la carga como un punto en el centro
            if q > 0:
                self.ax.scatter([0], [0], [0], color='red', s=100)
                self.ax.set_title('Líneas de campo eléctrico de una carga positiva')

                # Color de Fondo
                self.ax.set_facecolor("darkgrey")
                self.ax.grid(False)

                plt.tight_layout()
            else:
                self.ax.scatter([0], [0], [0], color='blue', s=100)
                self.ax.set_title('Líneas de campo eléctrico de una carga negativa')

                # Color de Fondo
                self.ax.set_facecolor("darkgrey")
                self.ax.grid(False)

                plt.tight_layout()

            # Dibujar las líneas de campo eléctrico
            self.ax.quiver(x, y, z, Ex, Ey, Ez, length=0.1, normalize=True)

            # Configurar los límites de los ejes
            self.ax.set_xlim([-1, 1])
            self.ax.set_ylim([-1, 1])
            self.ax.set_zlim([-1, 1])

    #------------ Grafica (muestra) (FIN) -------------------------------
    def cerrarGraf(self):
	    plt.close(self.fig)

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Camp_Elec_Flujos(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica (muestra) -------------------------------------
    def graficar_muestra(self):    

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        self.ax.grid(False)

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

        self.ax.set_title("Líneas de flujo y campo eléctrico de una carga puntual\n"
                    r"$\vec{E} = \frac{1}{4 \pi \epsilon_0} \frac{q}{|\vec{r}|^2} \hat{r}$", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})


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

    #------------ Grafica (muestra) (FIN) -------------------------------
    def cerrarGraf(self):
	    plt.close(self.fig)