## Archivo para el módulo de "Campo Magnético"

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
from mpl_toolkits import mplot3d
from scipy.integrate import quad
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

#*************************** Clase de Campo Magnético ******************************************************************************************************************#
class Campo_Magnetico(FigureCanvas):
    #------------------ Función Inicial---------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Campos Eléctricos --------------------------------------------------------------------------------------------------------------
    def graficar_camp_magne(self):    
        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Campo Magnético de un Cable Infinito Transportando Corriente (I)")  

        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_zticks([])

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")
        
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
        charge, = self.ax.plot([], [], [], 'o', color='orange', markersize=6, label = "Carga en Movimiento")

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

        plt.legend(ncol = 2, loc = 8, draggable = True)
        plt.tight_layout()

    #------------ Grafica de Campo Magnético (FIN) ----------------------------------------------------------------------------------------------------------

    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------------------------------------------------------------------------

#*************************** Clase de Campo Magnético (FIN) ************************************************************************************************************#

#*************************** Clase de Campo Magnético Cables ***********************************************************************************************************#
class Camp_Magne_Cables_Par(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica cables -------------------------------------
    def graficar_cables(self):    
        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle('Campo Magnético de Cables Infinitos Paralelos Transportando Corriente (I)') 
        #self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        #self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        #elf.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        self.ax.grid(False)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_zticks([])

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

            def update_charge_position(num, charge1, charge2, current_direction):
                charge1.set_data([-1, 0])
                charge1.set_3d_properties(charge_positions[num])
                charge2.set_data([1, 0])
                charge2.set_3d_properties(charge_positions[num] * current_direction)
                return charge1, charge2,

            charge1, = self.ax.plot([-1], [0], [0], 'o', markersize=8, color='orange', label='Carga en movimiento (Cable 1)')
            charge2, = self.ax.plot([1], [0], [0], 'o', markersize=8, color='orange', label='Carga en movimiento (Cable 2)')

            self.ani = FuncAnimation(self.fig, update_charge_position, len(charge_positions), fargs=(charge1, charge2, current_direction), interval=50, blit=True)

            # Ajustar la leyenda para incluir la carga en movimiento
            handles, labels = self.ax.get_legend_handles_labels()
            self.ax.legend(ncol = 2, loc = 8, draggable = True)

        current_direction = 1  # 1 para la misma dirección, -1 para direcciones opuestas
        plot_magnetic_field(current_direction)
        plt.tight_layout()
    #------------ Grafica cables (FIN) -------------------------------

    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------------------------------------------------------------------------

#*************************** Clase de Campo Magnético Cables (FIN) *****************************************************************************************************#

#*************************** Clase de Espira Magnética *****************************************************************************************************************#
class Espira_Magne(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica Espira -------------------------------------
    def graficar_espira(self):    
        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        #self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        #self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        #self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")
        self.ax.grid(False)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_zticks([])

        # Datos de entrada
        I = 0.6  # Valor de la corriente en la espira [carga/tiempo]
        #c = 1.0  # c = 4 * pi * epsilon
        c = 1 / (4 * np.pi * 1e-7)  # c = 1 / (4 * pi * epsilon), con epsilon = 1e-7 (permeabilidad magnética del vacío)

        a = 1.5 # Radio de la espira
        pi = np.pi

        # Función a integrar
        def integrand(phi, r, theta):
            return (np.cos(phi)) / np.sqrt(a ** 2 + r ** 2 - 2 * a * r * np.sin(theta) * np.cos(phi))

        # Cálculo de I(r, theta, phi)
        def I_r_theta_phi(r, theta):
            integral, _ = quad(integrand, 0, 2 * pi, args=(r, theta))
            return integral

        # Calcular A_phi
        def A_phi(r, theta):
            return (I * a / c) * I_r_theta_phi(r, theta)

        # Calcular las derivadas parciales de A_phi
        def dA_dtheta(r, theta):
            delta_theta = 1e-6
            return (np.sin(theta + delta_theta)*A_phi(r, theta + delta_theta) - np.sin(theta -  delta_theta)*A_phi(r, theta - delta_theta)) / (2 * delta_theta)

        def dA_dr(r, theta):
            delta_r = 1e-6
            return ((r+ delta_r)*A_phi(r + delta_r, theta) - (r- delta_r)*A_phi(r - delta_r, theta)) / (2 * delta_r)

        # Calcular las componentes del campo magnético B
        eps = 1e-15
        def B_r(r, theta):
            return (1 / (r * np.sin(theta) + eps)) * dA_dtheta(r, theta)

        def B_theta(r, theta):
            return -(1 / r) * dA_dr(r, theta)

        def B_phi(r, theta):
            return 0

        # Crear una malla en coordenadas esféricas
        r_values = np.linspace(0.00001, 2 * a, 9)
        theta_values = np.linspace(0, np.pi, 8)
        phi_values = np.linspace(0, 2 * np.pi, 9)

        R, Theta, Phi = np.meshgrid(r_values, theta_values, phi_values, indexing='ij')

        # Calcular las componentes de B en cada punto de la malla
        B_r_values = np.vectorize(B_r)(R, Theta)
        B_theta_values = np.vectorize(B_theta)(R, Theta)
        B_phi_values = np.vectorize(B_phi)(R, Theta)

        # Crear matriz 3D para guardar los valores de B
        B_matrix = np.zeros((len(r_values), len(theta_values), len(phi_values), 3))

        # Guardar los valores de B en la matriz 3D
        B_matrix[:, :, :, 0] = B_r_values
        B_matrix[:, :, :, 1] = B_theta_values
        B_matrix[:, :, :, 2] = B_phi_values

        # Convertir coordenadas esféricas a cartesianas
        X = R * np.sin(Theta) * np.cos(Phi)
        Y = R * np.sin(Theta) * np.sin(Phi)
        Z = R * np.cos(Theta)

        # Convertir componentes de B en coordenadas esféricas a cartesianas
        B_x_values = np.sin(Theta) * np.cos(Phi) * B_r_values + np.cos(Theta) * np.cos(Phi) * B_theta_values - np.sin(Phi) * B_phi_values
        B_y_values = np.sin(Theta) * np.sin(Phi) * B_r_values + np.cos(Theta) * np.sin(Phi) * B_theta_values + np.cos(Phi) * B_phi_values
        B_z_values = np.cos(Theta) * B_r_values - np.sin(Theta) * B_theta_values

        # Crear máscara para vectores en el plano YZ (X = 0)
        mask = np.isclose(X, 0, atol=1e-8)

        # Dibujar los vectores en el plano YZ (X = 0) en negro
        self.ax.quiver(X[mask], Y[mask], Z[mask], B_x_values[mask], B_y_values[mask], B_z_values[mask], length=a/5, normalize=True, color='k', linewidth=0.5)

        # Dibujar los vectores que no están en el plano YZ en azul
        self.ax.quiver(X[~mask], Y[~mask], Z[~mask], B_x_values[~mask], B_y_values[~mask], B_z_values[~mask], length=a/5, normalize=True, color='b', linewidth=0.5)

        self.ax.quiver(X, Y, Z, B_x_values, B_y_values, B_z_values, length=a/5, normalize=True, color='b', linewidth=0.5)
        plt.suptitle('Campo magnético de una espira de corriente')

        # Graficar la espira en color rojo
        #print ('a   =', a)
        phi_spiral = np.linspace(0, 2 * np.pi, 70)
        x_spiral = a * np.cos(phi_spiral)
        y_spiral = a * np.sin(phi_spiral)
        z_spiral = np.zeros_like(phi_spiral)
        self.ax.plot(x_spiral, y_spiral, z_spiral, color='r', linewidth=2)

        # Agregar el plano YZ de color naranja con una transparencia de 0.5
        #yz_plane_vertices = np.array([[-2 * a, -2 * a, -2 * a], [-2 * a, 2 * a, -2 * a], [-2 * a, 2 * a, 2 * a], [-2 * a, -2 * a, 2 * a]])
        yz_plane_vertices = np.array([[0, -2 * a, -2 * a], [0, 2 * a, -2 * a], [0, 2 * a, 2 * a], [0, -2 * a, 2 * a]])
        yz_plane = Poly3DCollection([yz_plane_vertices], alpha=0.5, facecolor='orange')
        self.ax.add_collection3d(yz_plane)
        
        plt.tight_layout()
    #------------ Grafica Espira (FIN) -------------------------------

    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------------------------------------------------------------------------

#*************************** Clase de Espira Magnética (FIN) **********************************************************************************************************#

#*************************** Clase de Espiras Magnéticas **************************************************************************************************************#
class Espiras_Magnes(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica Espira -------------------------------------
    def graficar_espiras(self):    
        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        #self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        #self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        #self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")
        self.ax.grid(False)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_zticks([])

        def biot_savart_magnetic_field(X, Y, Z, I, a, zo):
            c = 1 / (4 * np.pi * 1e-7)
            pi = np.pi

            def integrand(phi, r, theta):
                return (np.cos(phi)) / np.sqrt(a ** 2 + r ** 2 - 2 * a * r * np.sin(theta) * np.cos(phi))

            def I_r_theta_phi(r, theta):
                integral, _ = quad(integrand, 0, 2 * pi, args=(r, theta))
                return integral

            def A_phi(r, theta):
                return (I * a / c) * I_r_theta_phi(r, theta)

            def dA_dtheta(r, theta):
                delta_theta = 1e-6
                return (np.sin(theta + delta_theta) * A_phi(r, theta + delta_theta) - np.sin(theta - delta_theta) * A_phi(r, theta - delta_theta)) / (2 * delta_theta)

            def dA_dr(r, theta):
                delta_r = 1e-6
                return ((r + delta_r) * A_phi(r + delta_r, theta) - (r - delta_r) * A_phi(r - delta_r, theta)) / (2 * delta_r)

            eps = 1e-15
            def B_r(r, theta):
                return (1 / (r * np.sin(theta) + eps)) * dA_dtheta(r, theta)

            def B_theta(r, theta):
                return -(1 / r) * dA_dr(r, theta)

            def B_phi(r, theta):
                return 0

            r = np.sqrt(X ** 2 + Y ** 2 + (Z - zo) ** 2)
            theta = np.arccos((Z - zo) / r)
            phi = np.arctan2(Y, X)

            # Vectorize the necessary functions
            I_r_theta_phi_vec = np.vectorize(I_r_theta_phi)
            dA_dtheta_vec = np.vectorize(dA_dtheta)
            dA_dr_vec = np.vectorize(dA_dr)
            B_r_vec = np.vectorize(B_r)
            B_theta_vec = np.vectorize(B_theta)
            B_phi_vec = np.vectorize(B_phi)

            # Calculate the components of B in spherical coordinates using the vectorized functions
            B_r_value = B_r_vec(r, theta)
            B_theta_value = B_theta_vec(r, theta)
            B_phi_value = B_phi_vec(r, theta)

            B_x_value = np.sin(theta) * np.cos(phi) * B_r_value + np.cos(theta) * np.cos(phi) * B_theta_value - np.sin(phi) * B_phi_value
            B_y_value = np.sin(theta) * np.sin(phi) * B_r_value + np.cos(theta) * np.sin(phi) * B_theta_value + np.cos(phi) * B_phi_value
            B_z_value = np.cos(theta) * B_r_value - np.sin(theta) * B_theta_value

            return np.array([B_x_value, B_y_value, B_z_value])

        I = 0.6
        a = 1.5
        zo1 = 1.0
        zo2 = 2.0

        x_values = np.linspace(-2 * a, 2 * a, 9)
        y_values = np.linspace(-2 * a, 2 * a, 9)
        z_values = np.linspace(-2 * a, 2 * a, 9)

        X, Y, Z = np.meshgrid(x_values, y_values, z_values, indexing='ij')

        B1 = biot_savart_magnetic_field(X, Y, Z, I, a, zo1)
        B2 = biot_savart_magnetic_field(X, Y, Z, I, a, zo2)
        B_total = B1 + B2

        def draw_spiral(ax, zo, a, color='red', num_points=100):
            phi = np.linspace(0, 2 * np.pi, num_points)
            x = a * np.cos(phi)
            y = a * np.sin(phi)
            z = np.ones_like(phi) * zo
            ax.plot(x, y, z, color=color)

        draw_spiral(self.ax, zo1, a)
        draw_spiral(self.ax, zo2, a)

        self.ax.quiver(X, Y, Z, B_total[0], B_total[1], B_total[2], length=a/5, normalize=True, color='b', linewidth=0.5)

        plt.suptitle('Campo magnético total debido a dos espiras de corriente')
        
        plt.tight_layout()
    #------------ Grafica Espira (FIN) -------------------------------

    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------------------------------------------------------------------------

#*************************** Clase de Espira Magnética (FIN) **********************************************************************************************************#

#*************************** Clase de Dipolo Magnético 2D *************************************************************************************************************#
class Dipolo_Magne_2d(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    #------------ Grafica Dipolo Magnético 2D -------------------------------------
    def graficar_dipolo_2d(self):    
        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica

        def magnetic_dipole_field(x, y, m):
            mu_0 = 4 * np.pi * 10 ** -7
            r = np.sqrt(x ** 2 + y ** 2)
            r_cubed = r ** 3
            factor = (mu_0 / (4 * np.pi * r_cubed))

            B_x = 3 * x * y * factor
            B_y = (3 * y ** 2 - r ** 2) * factor

            return B_x, B_y

        # Parámetros del dipolo magnético
        m = 1e-6  # Momento magnético en Am²

        # Calcular el campo magnético en un plano XY
        grid_size = 20
        x_values = np.linspace(-1, 1, grid_size)
        y_values = np.linspace(-1, 1, grid_size)
        X, Y = np.meshgrid(x_values, y_values)
        B_x_values = np.zeros((grid_size, grid_size))
        B_y_values = np.zeros((grid_size, grid_size))

        for i in range(grid_size):
            for j in range(grid_size):
                x, y = X[i, j], Y[i, j]
                B_x, B_y = magnetic_dipole_field(x, y, m)
                B_x_values[i, j] = B_x
                B_y_values[i, j] = B_y

        # Líneas de flujo
        self.ax.streamplot(X, Y, B_x_values, B_y_values, color='blue', linewidth=0.5, density=2, arrowstyle='->', arrowsize=1)

        # Configurar el gráfico
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        plt.suptitle("Líneas de campo magnético de un dipolo magnético")
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)
        self.ax.set_aspect('equal', 'box')
        self.ax.grid()

    #------------ Grafica Dipolo Magnético 2D (FIN) -------------------------------

    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------------------------------------------------------------------------

#*************************** Clase de Dipolo Magnético 2D (FIN) *******************************************************************************************************#

#*************************** Clase de Dipolo Magnético 3D *************************************************************************************************************#
class Dipolo_Magne_3d(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica Dipolo Magnético 3D -------------------------------------
    def graficar_dipolo_3d(self):    
        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica

        def magnetic_dipole_field(x, y, z, m_x, m_y, m_z):
            mu_0 = 4 * np.pi * 1e-7  # Permeabilidad magnética del vacío
            r = np.sqrt(x**2 + y**2 + z**2)
            r_cubed = r**3

            # Calcular las componentes del campo magnético
            B_x = (3 * x * (x * m_x + y * m_y + z * m_z) - r**2 * m_x) / r_cubed
            B_y = (3 * y * (x * m_x + y * m_y + z * m_z) - r**2 * m_y) / r_cubed
            B_z = (3 * z * (x * m_x + y * m_y + z * m_z) - r**2 * m_z) / r_cubed

            B_x *= mu_0 / (4 * np.pi)
            B_y *= mu_0 / (4 * np.pi)
            B_z *= mu_0 / (4 * np.pi)

            return B_x, B_y, B_z

        # Parámetros del dipolo magnético
        m_x, m_y, m_z = 0, 0, 1e-6

        # Calcular el campo magnético en un espacio 3D
        grid_size = 10
        x_values = np.linspace(-1, 1, grid_size)
        y_values = np.linspace(-1, 1, grid_size)
        z_values = np.linspace(-1, 1, grid_size)
        X, Y, Z = np.meshgrid(x_values, y_values, z_values)
        B_x_values, B_y_values, B_z_values = magnetic_dipole_field(X, Y, Z, m_x, m_y, m_z)

        # Normalizar vectores para que las flechas tengan la misma longitud
        magnitude = np.sqrt(B_x_values**2 + B_y_values**2 + B_z_values**2)
        B_x_norm = B_x_values / magnitude
        B_y_norm = B_y_values / magnitude
        B_z_norm = B_z_values / magnitude

        self.ax.quiver(X, Y, Z, B_x_norm, B_y_norm, B_z_norm, length=0.1, color='b', linewidth=0.5)

        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        plt.suptitle('Líneas de campo magnético de un Dipolo')

    #------------ Grafica Dipolo Magnético 3D (FIN) -------------------------------

    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------------------------------------------------------------------------

#*************************** Clase de Dipolo Magnético 3D (FIN) *******************************************************************************************************#