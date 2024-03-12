# Archivo con el proceso de graficación y animaciones. Practica 14

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
import numpy as np

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Tiro_Rifle(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica (muestra) -------------------------------------
    def graficar_muestra(self, v_vox, v_voy, v_voz, v_gamma, v_betha, v_alpha):    

        #self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Tiro Parabólico con un Rifle")  
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        def F(t, vo, xf, yf, zf, g):
            return vo * t - np.sqrt(xf**2 + yf**2 + (zf + 0.5 * g * t**2)**2)

        def dF(t, vo, xf, yf, zf, g):
            #numerator = g * t * (zf + 0.5 * g * t**2)
            #denominator = np.sqrt(xf**2 + yf**2 + (zf + 0.5 * g * t**2)**2)
            #return vo - numerator / denominator

            denominator = (zf + 0.5 * g * t**2)
            numerator = np.sqrt(pow(xf,2) + pow(yf,2) + pow((zf + 0.5 * g *pow(t,2)),2))
            return vo - numerator / denominator


        def newton_raphson(t0, vo, xf, yf, zf, g, tol=1e-10, max_iter=1000):
            t = t0
            for _ in range(max_iter):
                t_new = t - F(t, vo, xf, yf, zf, g) / dF(t, vo, xf, yf, zf, g)
                if abs(t_new - t) < tol:
                    return t_new
                t = t_new
            raise Exception("No se encontró una solución en las iteraciones máximas")


        zinit = 1.7
        # Cordenada objetivo en Z
        zobj = 50
        #coordenada objetivo en X
        xf = 0.0
        #Coordenada objetivo en Y
        yf= 2000
        #Corrección considerando la altura en Z, de quien dispara
        zf = zobj - zinit

        #print("zf =",  zf)

        # Datos de entrada
        rf = np.array([xf, yf, zf])
        #Magnitud de la velocidad inicial [m/s], la velocidad del rifle está entre (300 y 900)
        vo = 300.0
        #gravedad [m/s^2]
        g = 9.81
        #Es un parámetro de entrada para iniciar el método numérico
        t0 = 1.0  # Valor inicial para Newton-Raphson

        # Resolver para el tiempo t
        t = newton_raphson(t0, vo, *rf, g)

        #print(f"Tiempo: {t}")

        # Calcular componentes de velocidad inicial
        vox = rf[0] / t
        voy = rf[1] / t
        voz = (rf[2] + 0.5 * g * t**2) / t

        #print(f"Velocidad inicial en x: {vox}")
        #print(f"Velocidad inicial en y: {voy}")
        #print(f"Velocidad inicial en z: {voz}")
        v_vox.display(round(vox, 2))
        v_voy.display(round(voy, 2))
        v_voz.display(round(voz, 2))

        #print("angulo respecto al eje X, gamma =", np.rad2deg(np.arccos(vox/vo)))
        #print("angulo respecto al eje Y, beta =", np.rad2deg(np.arccos(voy/vo)))
        #print("angulo respecto al eje Z, alpha =", np.rad2deg(np.arccos(voz/vo)))
        v_gamma.display(round(np.rad2deg(np.arccos(vox/vo)), 2))
        v_betha.display(round(np.rad2deg(np.arccos(voy/vo)), 2))
        v_alpha.display(round(np.rad2deg(np.arccos(voz/vo)), 2))

        ###############################################
        tfi = t
        dist = np.sqrt(pow(vox,2)*tfi + pow(voy,2)*tfi + pow(voz,2)*tfi)
        # No se le pide posición inicial, por  default se tiene:
        Xo = 0
        Yo = 0
        Zo = zinit

        # Definimos las ecuaciones de movimiento
        def r_vec(t):
            x = vox * t + Xo
            y = voy * t + Yo
            z = -0.5 * g * t**2 + voz * t + Zo
            return np.array([x, y, z])

        def v_vec(t):
            vx = vox
            vy = voy
            vz = -g * t + voz
            return np.array([vx, vy, vz])

        # Definimos los límites del gráfico
        max_range = np.sqrt(xf*xf + yf*yf + zf*zf)
        self.ax.set_xlim([0, max_range])
        self.ax.set_ylim([0, max_range])
        self.ax.set_zlim([0, 2*max_range])

        #tmax = (2 * voz) / g  # Calcula el tiempo máximo
        num_frames = 100  # Número de frames para la animación
        time_interval = tfi / num_frames  # Calcula el intervalo de tiempo entre cada frame

        def update(frame):
            # Borramos los datos anteriores
            self.ax.clear()
            
            # Añadimos el plano XY en color 10
            X, Y = np.meshgrid(np.linspace(0, max_range, 2), np.linspace(0, max_range, 2))
            Z = np.zeros_like(X)
            self.ax.plot_surface(X, Y, Z, color='C1', alpha=0.3)
            
            # Añadimos la trayectoria hasta el tiempo actual
            current_time = frame * time_interval
            t = np.linspace(0, current_time, 100)
            r = np.array([r_vec(ti) for ti in t])
            self.ax.plot(r[:,0], r[:,1], r[:,2], 'b')
            
        # Calcular las posiciones finales xf y yf
            xf = vox * tfi
            yf = voy * tfi
            zf =  -0.5 * g * pow(tfi,2) + voz * tfi + Zo

            #print("xf,yf,zf voz=",xf,yf,zf,voz)

        
            self.ax.scatter(xf, yf, zf, color='g', marker='o')
            #ax.text(xf, yf, zf, f'posición_final = ({xf:+.2f}, {yf:.+2f}, {zf:+.2f})', color = 'blue')
            #ax.text(xf, yf, zf, f'posición_final = ({xf:+.2f}, {yf:+.2f}, {zf:+.2f})', color='blue')
            self.ax.text(xf, yf, zf, f"posición_final = ({'-' if xf < 0 else ''}{abs(xf):.2f},{'-' if yf < 0 else ''}{abs(yf):.2f},{'-' if zf < 0 else ''}{abs(zf):.2f})", color='blue')

            # Dibujar la línea roja en el plano XY
            self.ax.plot([Xo, xf], [Yo, yf], [0, 0], color='red')

            # Añadir etiqueta con la distancia de impacto
            d_final = np.sqrt(pow(xf,2) + pow(yf,2) + pow(zf,2))

            self.ax.text(xf / 4, yf / 4, 0, f'd_final = {d_final:.2f}', color='red')

            # Añadimos una etiqueta con el tiempo actual
            self.ax.text2D(0.05, 0.95, f'Tiempo: {current_time:.2f} s', transform=self.ax.transAxes)

            return self.ax

        self.ani = FuncAnimation(self.fig, update, frames=num_frames, interval=time_interval*1000, blit=False, repeat=False)
        plt.tight_layout()

    #------------ Grafica (muestra) (FIN) -------------------------------

    #------------ Grafica Ángulo Sólido --------------------------------
    def graficarTiroRifle(self, zinit, xf, yf, zobj, v_vox, v_voy, v_voz, v_gamma, v_betha, v_alpha):    # Se piden las variables de otra clase para poder trabajarlos.

        plt.suptitle("Tiro Parabólico con un Rifle")  
        self.ax.set_xlabel("Posición_X [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        def F(t, vo, xf, yf, zf, g):
            return vo * t - np.sqrt(xf**2 + yf**2 + (zf + 0.5 * g * t**2)**2)

        def dF(t, vo, xf, yf, zf, g):
            #numerator = g * t * (zf + 0.5 * g * t**2)
            #denominator = np.sqrt(xf**2 + yf**2 + (zf + 0.5 * g * t**2)**2)
            #return vo - numerator / denominator

            denominator = (zf + 0.5 * g * t**2)
            numerator = np.sqrt(pow(xf,2) + pow(yf,2) + pow((zf + 0.5 * g *pow(t,2)),2))
            return vo - numerator / denominator


        def newton_raphson(t0, vo, xf, yf, zf, g, tol=1e-10, max_iter=1000):
            t = t0
            for _ in range(max_iter):
                t_new = t - F(t, vo, xf, yf, zf, g) / dF(t, vo, xf, yf, zf, g)
                if abs(t_new - t) < tol:
                    return t_new
                t = t_new
            raise Exception("No se encontró una solución en las iteraciones máximas")


        #Corrección considerando la altura en Z, de quien dispara
        zf = zobj - zinit

        #print("zf =",  zf)

        # Datos de entrada
        rf = np.array([xf, yf, zf])
        #Magnitud de la velocidad inicial [m/s,], la velocidad del rifle está entre (300 y 900)
        vo = 300.0
        #gravedad [m/s^2]
        g = 9.81
        #Es un parámetro de entrada para iniciar el método numérico
        t0 = 1.0  # Valor inicial para Newton-Raphson

        # Resolver para el tiempo t
        t = newton_raphson(t0, vo, *rf, g)

        #print(f"Tiempo: {t}")

        # Calcular componentes de velocidad inicial
        vox = rf[0] / t
        voy = rf[1] / t
        voz = (rf[2] + 0.5 * g * t**2) / t

        v_vox.display(round(vox, 2))
        v_voy.display(round(voy, 2))
        v_voz.display(round(voz, 2))

        v_gamma.display(round(np.rad2deg(np.arccos(vox/vo)), 2))
        v_betha.display(round(np.rad2deg(np.arccos(voy/vo)), 2))
        v_alpha.display(round(np.rad2deg(np.arccos(voz/vo)), 2))

        ###############################################
        tfi = t
        dist = np.sqrt(pow(vox,2)*tfi + pow(voy,2)*tfi + pow(voz,2)*tfi)
        # No se le pide posición inicial, por  default se tiene:
        Xo = 0
        Yo = 0
        Zo = zinit

        # Definimos las ecuaciones de movimiento
        def r_vec(t):
            x = vox * t + Xo
            y = voy * t + Yo
            z = -0.5 * g * t**2 + voz * t + Zo
            return np.array([x, y, z])

        def v_vec(t):
            vx = vox
            vy = voy
            vz = -g * t + voz
            return np.array([vx, vy, vz])

        # Definimos los límites del gráfico
        max_range = np.sqrt(xf*xf + yf*yf + zf*zf)
        self.ax.set_xlim([0, max_range])
        self.ax.set_ylim([0, max_range])
        self.ax.set_zlim([0, 2*max_range])

        #tmax = (2 * voz) / g  # Calcula el tiempo máximo
        num_frames = 100  # Número de frames para la animación
        time_interval = tfi / num_frames  # Calcula el intervalo de tiempo entre cada frame

        def update(frame):
            # Borramos los datos anteriores
            self.ax.clear()
            
            # Añadimos el plano XY en color 10
            X, Y = np.meshgrid(np.linspace(0, max_range, 2), np.linspace(0, max_range, 2))
            Z = np.zeros_like(X)
            self.ax.plot_surface(X, Y, Z, color='C1', alpha=0.3)
            
            # Añadimos la trayectoria hasta el tiempo actual
            current_time = frame * time_interval
            t = np.linspace(0, current_time, 100)
            r = np.array([r_vec(ti) for ti in t])
            self.ax.plot(r[:,0], r[:,1], r[:,2], 'b')
            
        # Calcular las posiciones finales xf y yf
            xf = vox * tfi
            yf = voy * tfi
            zf =  -0.5 * g * pow(tfi,2) + voz * tfi + Zo

            #print("xf,yf,zf voz=",xf,yf,zf,voz)

        
            self.ax.scatter(xf, yf, zf, color='g', marker='o')
            #ax.text(xf, yf, zf, f'posición_final = ({xf:+.2f}, {yf:.+2f}, {zf:+.2f})', color = 'blue')
            #ax.text(xf, yf, zf, f'posición_final = ({xf:+.2f}, {yf:+.2f}, {zf:+.2f})', color='blue')
            self.ax.text(xf, yf, zf, f"posición_final = ({'-' if xf < 0 else ''}{abs(xf):.2f},{'-' if yf < 0 else ''}{abs(yf):.2f},{'-' if zf < 0 else ''}{abs(zf):.2f})", color='blue')

            # Dibujar la línea roja en el plano XY
            self.ax.plot([Xo, xf], [Yo, yf], [0, 0], color='red')

            # Añadir etiqueta con la distancia de impacto
            d_final = np.sqrt(pow(xf,2) + pow(yf,2) + pow(zf,2))

            self.ax.text(xf / 4, yf / 4, 0, f'd_final = {d_final:.2f}', color='red')

            # Añadimos una etiqueta con el tiempo actual
            self.ax.text2D(0.05, 0.95, f'Tiempo: {current_time:.2f} s', transform=self.ax.transAxes)

            return self.ax

        self.ani = FuncAnimation(self.fig, update, frames=num_frames, interval=time_interval*1000, blit=False, repeat=False)
        plt.tight_layout()

    #------------ Grafica Ángulo Sólido (FIN) -----------------------------------------

    #------------ Función para borrar la gráfica ---------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
        plt.clf()

    #------------ Función para borrar la gráfica (FIN) ---------------------------