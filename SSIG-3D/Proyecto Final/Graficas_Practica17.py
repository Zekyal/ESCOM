# Archivo con el proceso de graficación y animaciones. Practica 17

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
import numpy as np

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Camp_Magne_Cable(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica (muestra) -------------------------------------
    def graficar_muestra(self):    

        self.ax.set_title('Campo Magnético de un Cable Infinito Transportando Corriente (I)', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("Posición_X [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        self.ax.grid(False)

        # Constantes
        I = 10  # Corriente en amperios
        mu_0 = 4 * np.pi * 1e-7  # Permeabilidad magnética del vacío

        # Función para calcular el campo magnético en un punto P(x, y, z)
        def magnetic_field(x, y, z):
            rho = np.sqrt(x**2 + y**2)
            B = (mu_0 * I) / (2 * np.pi * rho)
            Bx = -B * y / rho
            By = B * x / rho
            Bz = z * 0
            return Bx, By, Bz

        # Establecer los límites de los ejes
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        self.ax.set_zlim(-2, 2)

        # Inicializar carga ficticia
        charge, = self.ax.plot([], [], [], 'o', color='orange', markersize=6)

        # Función de inicialización para la animación
        def init():
            charge.set_data([], [])
            charge.set_3d_properties([])
            return charge,

        # Función de actualización para la animación
        def update(frame):
            z_charge = -2 + 4 * frame / 30
            charge.set_data(0, 0)
            charge.set_3d_properties(z_charge)
            return charge,

        # Crear la animación
        self.ani = FuncAnimation(self.fig, update, frames=30, init_func=init, blit=True, interval=100, repeat=True)

        # Vectores del campo magnético (color azul)
        x = np.linspace(-2, 2, 10)
        y = np.linspace(-2, 2, 10)
        z = np.linspace(-2, 2, 10)
        X, Y, Z = np.meshgrid(x, y, z)
        Bx, By, Bz = magnetic_field(X, Y, Z)
        self.ax.quiver(X, Y, Z, Bx, By, Bz, color='b', length=0.2, normalize=True, arrow_length_ratio=0.2)

        # Cable infinito (color gris con transparencia)
        self.ax.plot([0, 0], [0, 0], [-2, 2], 'k-', linewidth=5, alpha=0.5, label='Cable infinito')

        self.ax.legend()
        plt.tight_layout()

    #------------ Grafica (muestra) (FIN) -------------------------------
    def cerrarGraf(self):
	    plt.close(self.fig)

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Camp_Magne_Cables_Par(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica (muestra) -------------------------------------
    def graficar_muestra(self):    

        self.ax.set_title('Campo Magnético de Cables Infinitos Paralelos Transportando Corriente (I)', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("Posición_X [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        self.ax.grid(False)

        # Constantes
        I = 10  # Corriente en amperios
        mu_0 = 4 * np.pi * 1e-7  # Permeabilidad magnética del vacío

        def magnetic_field(x, y, z, current_direction):
            rho1 = np.sqrt((x - 1)**2 + y**2)  # Distancia al primer cable
            rho2 = np.sqrt((x + 1)**2 + y**2)  # Distancia al segundo cable

            # Campo magnético generado por el primer cable
            B1 = (mu_0 * I) / (2 * np.pi * rho1)
            B1x = -B1 * y / rho1
            B1y = B1 * (x - 1) / rho1
            B1z = z * 0

            # Campo magnético generado por el segundo cable
            B2 = (mu_0 * I * current_direction) / (2 * np.pi * rho2)
            B2x = -B2 * y / rho2
            B2y = B2 * (x + 1) / rho2
            B2z = z * 0

            # Campo magnético total
            Bx = B1x + B2x
            By = B1y + B2y
            Bz = B1z + B2z

            return Bx, By, Bz

        def plot_magnetic_field(current_direction):
            # Generar una malla de puntos para evaluar el campo magnético
            x = np.linspace(-3, 3, 10)
            y = np.linspace(-3, 3, 10)
            z = np.linspace(-2, 2, 10)
            X, Y, Z = np.meshgrid(x, y, z)

            # Calcular el campo magnético en cada punto de la malla
            Bx, By, Bz = magnetic_field(X, Y, Z, current_direction)

            # Vectores del campo magnético (color azul)
            self.ax.quiver(X, Y, Z, Bx, By, Bz, color='b', length=0.2, normalize=True, arrow_length_ratio=0.2)

            # Cables infinitos (color gris con transparencia)
            self.ax.plot([1, 1], [0, 0], [-2, 2], linewidth=5, color="gray", label='Cable infinito 1')
            self.ax.plot([-1, -1], [0, 0], [-2, 2], linewidth=5, color="gray", label='Cable infinito 2')
            
            # Animación de carga en movimiento (color naranja)
        
            charge_positions = np.linspace(-2, 2, 100)

        #    def update_charge_position(num, charge, current_direction):
        #        charge.set_data([current_direction * (-1)**num * -1, 0])
        #        charge.set_3d_properties(charge_positions[num])
        #        return charge,

            def update_charge_position(num, charge1, charge2, current_direction):
                charge1.set_data([-1, 0])
                charge1.set_3d_properties(charge_positions[num])
                charge2.set_data([1, 0])
                charge2.set_3d_properties(charge_positions[num] * current_direction)
                return charge1, charge2,

            charge1, = self.ax.plot([-1], [0], [0], 'o', markersize=8, color='orange', label='Carga en movimiento (Cable 1)')
            charge2, = self.ax.plot([1], [0], [0], 'o', markersize=8, color='orange', label='Carga en movimiento (Cable 2)')

            self.ani = FuncAnimation(self.fig, update_charge_position, len(charge_positions), fargs=(charge1, charge2, current_direction), interval=50, blit=True)

            #ani = animation.FuncAnimation(fig, update_charge_position, len(charge_positions), fargs=(charge1, current_direction), interval=50, blit=True)

            # Ajustar la leyenda para incluir la carga en movimiento
            handles, labels = self.ax.get_legend_handles_labels()
            self.ax.legend(handles[:3], labels[:3])

        current_direction = 1  # 1 para la misma dirección, -1 para direcciones opuestas
        plot_magnetic_field(current_direction)
        plt.tight_layout()

    #------------ Grafica (muestra) (FIN) -------------------------------
    def cerrarGraf(self):
	    plt.close(self.fig)