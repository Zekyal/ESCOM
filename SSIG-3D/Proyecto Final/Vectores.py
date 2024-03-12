## Archivo para el módulo de "Vectores"

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from mpl_toolkits import mplot3d
import numpy as np
import Vector as v  # Nuestra biblioteca de Vectores

#*************************** Clase de Vectores ***********************************************************************************************************************#
class Vectores(FigureCanvas):
    #------------------ Función Inicial -------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Simulando Vector ------------------------------------------------------------------------------------------------------------------------------------
    def graficar_vector(self, rx, ry, rz,val_magnitud, val_alpha, val_beta, val_gamma, val_alpha_g, val_beta_g, val_gamma_g, usuario):   

        # Cosenos Directores y Magnitud 
        magnitud = np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2))
        alpha = np.arccos(np.absolute(rx) / magnitud)
        beta = np.arccos(np.absolute(ry) / magnitud)
        gamma = np.arccos(np.absolute(rz) / magnitud)
        alphaDeg = np.degrees(alpha)
        betaDeg = np.degrees(beta)
        gammaDeg = np.degrees(gamma)

        val_magnitud.display(magnitud)
        val_alpha.display(alpha)
        val_beta.display(beta)
        val_gamma.display(gamma)
        val_alpha_g.display(alphaDeg)
        val_beta_g.display(betaDeg)
        val_gamma_g.display(gammaDeg)

        self.ax.set_title("Hecho por: " + usuario , loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Ejemplo de vector")  
        self.ax.xaxis.set_label_text('Posición_X', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.yaxis.set_label_text('Posición_Y', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.zaxis.set_label_text('Posición_Z', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        if rx == 0 or ry ==0 or rz ==0: 

            self.ax.quiver(0,0,0, rx, ry, rz, arrow_length_ratio=0.1, color = 'black' )

            #========================================================================
            # nombre del vector
            self.ax.text(rx, ry, rz, f"({rx}, {ry}, {rz})", style='italic', fontweight='bold', color = 'blue', fontsize=12)

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
            if (rx > 0):
                self.ax.text(1.25*rx, 0, 0, "X", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.text(-0.2*rx, 0, 0, "-X", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.plot((rx, 0), (0, 0), (0, 0), color = "orange", label='X')
                self.ax.plot((0, -0.2*rx), (0, 0), (0, 0), color = "red", label='-X')
            else:
                self.ax.text(-0.2*rx, 0, 0, "X", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.text(1.25*rx, 0, 0, "-X", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.plot((-0.2*rx, 0), (0, 0), (0, 0), color = "orange", label='X')
                self.ax.plot((0, rx), (0, 0), (0, 0), color = "red", label='-X')
            if (ry > 0):
                self.ax.text(0, 1.25*ry, 0, "Y", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.text(0, -0.2*ry, 0, "-Y", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.plot((0, 0), (ry, 0), (0, 0), color = "green", label='Y')
                self.ax.plot((0, 0), (0, -0.2*ry), (0, 0), color = "blue", label='-Y')
            else:
                self.ax.text(0, -0.2*ry, 0, "Y", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.text(0, 1.25*ry, 0, "-Y", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.plot((0, 0), (-0.2*ry, 0), (0, 0), color = "green", label='Y')
                self.ax.plot((0, 0), (0, ry), (0, 0), color = "blue", label='-Y')
            if (rz > 0):
                self.ax.text(0, 0, 1.25*rz, "Z", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.text(0, 0, -0.2*rz, "-Z", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.plot((0, 0), (0, 0), (rz, 0), color = "slateblue", label='Z')
                self.ax.plot((0, 0), (0, 0), (0, -0.2*rz), color = "brown", label='-Z')  
            else:
                self.ax.text(0, 0, -0.2*rz, "Z", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.text(0, 0, 1.25*rz, "-Z", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.plot((0, 0), (0, 0), (-0.2*rz, 0), color = "slateblue", label='Z')
                self.ax.plot((0, 0), (0, 0), (0, rz), color = "brown", label='-Z')  

            plt.legend(ncol = 3, loc = 8, draggable = True)

        else:

            # Definicion de los ejes x, y, z que se marcaran para definir la grafica
            if (rx >= 0 ):
                self.ax.plot((0, 1.25*rx), (0, 0), (0, 0), color = "orange", label='X')
                self.ax.text(1.25*rx, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
            else:
                self.ax.plot((1.25*rx, 0), (0, 0), (0, 0), color = "red", label='-X')
                self.ax.text(1.25*rx, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
            
            if (ry >= 0 ):
                self.ax.plot((0, 0), (0, 1.25*ry), (0, 0), color = "green", label='Y')
                self.ax.text(0, 1.25*ry, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
            else:
                self.ax.plot((0, 0), (1.25*ry, 0), (0, 0), color = "blue", label='-Y')
                self.ax.text(0, 1.25*ry, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)

            if (rz >= 0):
                self.ax.plot((0, 0), (0, 0), (0, 1.25*rz), color = "slateblue", label='Z')
                self.ax.text(0, 0, 1.25*rz, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
            else:
                self.ax.plot((0, 0), (0, 0), (1.25*rz, 0), color = "brown", label='-Z')
                self.ax.text(0, 0, 1.25*rz, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)

            self.ax.quiver(0,0,0, rx, ry, rz, arrow_length_ratio=0.1, color = 'black', label="-> Vector")

            #========================================================================
            # nombre del vector
            self.ax.text(rx, ry, rz, f"({rx}, {ry}, {rz})", style='italic', fontweight='bold', color = 'blue', fontsize=12)

            #=============recupera sus valores==========

            # ----------    Componentes i, j y k   ----------
            self.ax.quiver(0, 0, 0, rx, 0, 0, arrow_length_ratio=0.1, color = "black",  alpha = 0.7, linestyle = '--' )
            self.ax.quiver(0, 0, 0, 0, ry, 0, arrow_length_ratio=0.1, color = "black", alpha = 0.7, linestyle = '--' )
            self.ax.quiver(0, 0, 0, 0, 0, rz, arrow_length_ratio=0.1, color = "black", alpha = 0.7, linestyle = '--' )
            # nombres de los ejes
            self.ax.text(rx/2, 0, 0, 'î', style='italic', fontweight='bold', fontsize=12, color = "black")
            self.ax.text(0, ry/2, 0, 'ĵ', style='italic', fontweight='bold', fontsize=12,  color = "black")
            self.ax.text(0, 0, rz/2, 'k̂', style='italic', fontweight='bold', fontsize=12, color = "black")

            # ----------    Componentes i, j y k traslapados   ----------
            self.ax.plot((0, rx), (ry, ry), (0, 0), color = "black", linestyle = "dotted")
            self.ax.plot((rx, rx), (0, ry), (0, 0), color = "black", linestyle = "dotted")
            self.ax.plot((rx, rx), (ry, ry), (0, rz), color = "black", linestyle = "dotted")

            # ----------    Efecto del "librito"    ----------
            self.ax.plot((0, rx), (0, ry), (0, 0), color = "gray", linestyle = "dotted")
            self.ax.plot((0, rx), (0, ry), (rz, rz), color = "green", linestyle = "dotted")

            #-----Efecto planos inclinados ---------
            self.ax.plot((0, rx), (ry, ry), (0, rz), color = "blue", linestyle = "dotted")
            self.ax.plot((rx, rx), (0, ry), (0, rz), color = "red", linestyle = "dotted")

            # ----------    Curvas de los angulos   ----------
            sgnRx = rx/np.absolute(rx)
            sgnRy = ry/np.absolute(ry)
            sgnRz = rz/np.absolute(rz)

            # ->    Curva con respecto al eje x (angulo α)
            # generacion de todos los valores de x
            x = np.linspace(0, (0.5 * ry * rx)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 1000) 

            # formulas
            X = sgnRx * np.sqrt((pow(rx, 2)/4) - pow(x, 2) * ((pow(ry, 2) + pow(rz, 2))/pow(ry, 2)))
            Y = np.absolute(x) * sgnRy
            Z = np.absolute((rz / ry) * x) * sgnRz
            self.ax.plot(X, Y, Z, color = "red", label = 'α')
            self.ax.text(X[500], Y[500], Z[500], 'α', style='italic', fontweight='bold', color = "black", fontsize=12)
            
            # ->    Curva con respecto al eje y (angulo β)
            # generacion de todos los valores de y
            y = np.linspace(0, (0.5 * rz * ry)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 1000)

            # formulas
            X = np.absolute((rx / rz) * y) * sgnRx
            Y = sgnRy * np.sqrt((pow(ry, 2)/4) - pow(y, 2) * ((pow(rx, 2) + pow(rz, 2))/pow(rz, 2)))
            Z = np.absolute(y) * sgnRz 
            self.ax.plot(X, Y, Z, color = "blue", label = 'β')
            self.ax.text(X[500], Y[500], Z[500], 'β', style='italic', fontweight='bold', color = "black", fontsize=12)

            # ->    Curva con respecto al eje z (angulo ɣ)
            # generacion de todos los valores de z 
            z = np.linspace(0, (0.5 * rx * rz)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 1000) 

            # formulas
            X = np.absolute(z) * sgnRx
            Y = np.absolute((ry / rx) * z) * sgnRy
            Z = sgnRz * np.sqrt((pow(rz, 2)/4) - pow(z, 2) * ((pow(rx, 2) + pow(ry, 2))/pow(rx, 2)))
            self.ax.plot(X, Y, Z, color = "green", label = 'ɣ')
            self.ax.text(X[500], Y[500], Z[500], 'ɣ', style='italic', fontweight='bold', color = "black", fontsize=12)

            plt.legend(ncol = 4, loc = 8, draggable = True)
    
        plt.tight_layout()
    #------------ Guardar la gráfica ---------------------------------------------------------------------------------------------------------------------------------
    def guardar_graf(self, direccion):
        plt.savefig(direccion + "/Vector.jpg")
    #------------ Borrar la gráfica ----------------------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

#*************************** Clase de Vectores (FIN) ****************************************************************************************************************#

#*************************** Clase de Vectores de Suma **************************************************************************************************************#
class Vectores_Suma_Vect(FigureCanvas):
    #------------------ Función Inicial ------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)
    
    #------------ Suma de 2 vectores ---------------------------------------------------------------------------------------------------------------------------------
    def graficar_vectores_suma_2v(self, x1, y1, z1, x2, y2, z2, usuario):    

        self.ax.set_title("Hecho por: " + usuario , loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Ejemplo de la suma de dos vectores.")  
        self.ax.xaxis.set_label_text('Posición_X', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.yaxis.set_label_text('Posición_Y', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.zaxis.set_label_text('Posición_Z', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        a = np.array([x1, y1, z1])
        b = np.array([x2, y2, z2])

        colors = ['red', 'green', 'blue', 'orange', 'violet']

        vectorList = {
            "a" : a,
            "b" : b
        }

        vector = list(vectorList.values())

        resultado = vector[0]

        for x in range(1, len(vectorList)):
            resultado = v.Add(resultado, vector[x])
            
        vectorList["Resultante"] = resultado
        
        vector = list(vectorList.values())
        labels = list(vectorList.keys())

        # Mostrando los valores de los vectores en los labels
        labels[0] = "-> " + str(labels[0]) 
        labels[1] = "-> " + str(labels[1]) 
        labels[2] = "-> " + str(labels[2]) 

        # Se establece como valor inicial de los limites de cada eje, el primer punto de cada eje
        # de la Grafica, enlistado en la lista de Vectores
        max_axis_x = min_axis_x = vector[0][0]
        max_axis_y = min_axis_y = vector[0][1]
        max_axis_z = min_axis_z = vector[0][2]
        
        # Se obtienen los puntos maximos y minimos de cada eje de la Grafica, recorriendo cada uno
        # de los ejes enlistados en la lista de Vectores
        for x in range(1, len(vector)):
            max_axis_x = max(max_axis_x, vector[x][0])
            max_axis_y = max(max_axis_y, vector[x][1])
            max_axis_z = max(max_axis_z, vector[x][2])
            min_axis_x = min(min_axis_x, vector[x][0])
            min_axis_y = min(min_axis_y, vector[x][1])
            min_axis_z = min(min_axis_z, vector[x][2])
        
        # En caso de que el minimo sea un num positivo, se reduce a 0, para que asi las lineas siempre
        # se grafiquen desde el eje 0
        min_axis_x = min(min_axis_x, 0)
        min_axis_y = min(min_axis_y, 0)
        min_axis_z = min(min_axis_z, 0)
        
        # Definicion de los ejes x, y, z que se marcaran para definir la grafica
        if ((max_axis_x >= 0 ) and (min_axis_x >= 0)):
            self.ax.plot((0, 1.25*max_axis_x), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.text(1.25*max_axis_x, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_x >= 0 ) and (min_axis_x < 0)):
            self.ax.plot((0, 1.25*max_axis_x), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.plot((1.25*min_axis_x, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*max_axis_x, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(1.25*min_axis_x, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((1.25*min_axis_x, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*min_axis_x, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        
        if ((max_axis_y >= 0 ) and (min_axis_y >= 0)):
            self.ax.plot((0, 0), (0, 1.25*max_axis_y), (0, 0), color = "green", label='Y')
            self.ax.text(0, 1.25*max_axis_y, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_y >= 0 ) and (min_axis_y < 0)):
            self.ax.plot((0, 0), (0, 1.25*max_axis_y), (0, 0), color = "green", label='Y')
            self.ax.plot((0, 0), (1.25*min_axis_y, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*max_axis_y, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(0, 1.25*min_axis_y, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (1.25*min_axis_y, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*min_axis_y, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)

        if ((max_axis_z >= 0 ) and (min_axis_z >= 0)):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*max_axis_z), color = "slateblue", label='Z')
            self.ax.text(0, 0, 1.25*max_axis_z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_z >= 0 ) and (min_axis_z < 0)):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*max_axis_z), color = "slateblue", label='Z')
            self.ax.plot((0, 0), (0, 0), (1.25*min_axis_z, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*max_axis_z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(0, 0, 1.25*min_axis_z, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (0, 0), (1.25*min_axis_z, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*min_axis_z, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)

        # Letras en los vectores
        self.ax.text(3*a[0]/4, 3*a[1]/4, 3*a[2]/4, 'a', style='italic', fontweight='bold', color = str(colors[0]), fontsize=12)
        self.ax.text(3*b[0]/4, 3*b[1]/4, 3*b[2]/4, 'b', style='italic', fontweight='bold', color = str(colors[1]), fontsize=12)
        self.ax.text(3*resultado[0]/4, 3*resultado[1]/4, 3*resultado[2]/4, 'Resultante', style='italic', fontweight='bold', color = str(colors[2]), fontsize=12)
        self.ax.text(a[0], a[1], a[2], '(' + str(a[0]) + ', ' + str(a[1]) + ', '+ str(a[2]) + ')', 
                     style='italic', fontweight='bold', color = str(colors[0]), fontsize=12)
        self.ax.text(b[0], b[1], b[2], '(' + str(b[0]) + ', ' + str(b[1]) + ', '+ str(b[2]) + ')', 
                     style='italic', fontweight='bold', color = str(colors[1]), fontsize=12)
        self.ax.text(resultado[0], resultado[1], resultado[2], '(' + str(round(resultado[0],2)) + ', ' + str(round(resultado[1],2)) + ', '+ str(round(resultado[2],2)) + ')', 
                     style='italic', fontweight='bold', color = str(colors[2]), fontsize=12)

        for x in range(len(vector)):
            self.ax.quiver(0, 0, 0, vector[x][0], vector[x][1], vector[x][2], color = colors[x], label = labels[x], arrow_length_ratio=0.1)
    
        ## GRAFICACION DE VECTORES COMPLEMENTARIOS PARA LA SUMA DE VECTORES
        init_x = vector[0][0]
        init_y = vector[0][1]
        init_z = vector[0][2]
            
        for x in range(len(vector) - 2):
            end_x = vector[x + 1][0]
            end_y = vector[x + 1][1]
            end_z = vector[x + 1][2]
                
            self.ax.quiver(init_x, init_y, init_z, end_x, end_y, end_z, color = colors[x+1], label = labels[x+1] + "*", arrow_length_ratio=0.1, linestyle = '--')
                
            init_x = init_x + end_x
            init_y = init_y + end_y
            init_z = init_z + end_z
        
        # Impresion de la Leyenda
        plt.tight_layout()
        plt.legend(ncol = 4, loc = 8, draggable = True)

    #------------ Suma de 3 vectores ----------------------------------------------------------------------------------------------------------------------------------
    def graficar_vectores_suma_3v(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, usuario):    

        self.ax.set_title("Hecho por: " + usuario , loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Ejemplo de la suma de tres vectores.")  
        self.ax.xaxis.set_label_text('Posición_X', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.yaxis.set_label_text('Posición_Y', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.zaxis.set_label_text('Posición_Z', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        a = np.array([x1, y1, z1])
        b = np.array([x2, y2, z2])
        c = np.array([x3, y3, z3])

        colors = ['red', 'green', 'blue', 'orange', 'violet']

        vectorList = {
            "a" : a,
            "b" : b,
            "c" : c
        }

        vector = list(vectorList.values())

        resultado = vector[0]

        for x in range(1, len(vectorList)):
            resultado = v.Add(resultado, vector[x])
            
        vectorList["Resultante"] = resultado
        
        vector = list(vectorList.values())
        labels = list(vectorList.keys())

        # Mostrando los valores de los vectores en los labels
        labels[0] = "-> " + str(labels[0]) 
        labels[1] = "-> " + str(labels[1]) 
        labels[2] = "-> " + str(labels[2]) 
        labels[3] = "-> " + str(labels[3]) 

        # Se establece como valor inicial de los limites de cada eje, el primer punto de cada eje
        # de la Grafica, enlistado en la lista de Vectores
        max_axis_x = min_axis_x = vector[0][0]
        max_axis_y = min_axis_y = vector[0][1]
        max_axis_z = min_axis_z = vector[0][2]
        
        # Se obtienen los puntos maximos y minimos de cada eje de la Grafica, recorriendo cada uno
        # de los ejes enlistados en la lista de Vectores
        for x in range(1, len(vector)):
            max_axis_x = max(max_axis_x, vector[x][0])
            max_axis_y = max(max_axis_y, vector[x][1])
            max_axis_z = max(max_axis_z, vector[x][2])
            min_axis_x = min(min_axis_x, vector[x][0])
            min_axis_y = min(min_axis_y, vector[x][1])
            min_axis_z = min(min_axis_z, vector[x][2])
        
        # En caso de que el minimo sea un num positivo, se reduce a 0, para que asi las lineas siempre
        # se grafiquen desde el eje 0
        min_axis_x = min(min_axis_x, 0)
        min_axis_y = min(min_axis_y, 0)
        min_axis_z = min(min_axis_z, 0)
        
        # Definicion de los ejes x, y, z que se marcaran para definir la grafica
        if ((max_axis_x >= 0 ) and (min_axis_x >= 0)):
            self.ax.plot((0, 1.25*max_axis_x), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.text(1.25*max_axis_x, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_x >= 0 ) and (min_axis_x < 0)):
            self.ax.plot((0, 1.25*max_axis_x), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.plot((1.25*min_axis_x, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*max_axis_x, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(1.25*min_axis_x, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((1.25*min_axis_x, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*min_axis_x, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        
        if ((max_axis_y >= 0 ) and (min_axis_y >= 0)):
            self.ax.plot((0, 0), (0, 1.25*max_axis_y), (0, 0), color = "green", label='Y')
            self.ax.text(0, 1.25*max_axis_y, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_y >= 0 ) and (min_axis_y < 0)):
            self.ax.plot((0, 0), (0, 1.25*max_axis_y), (0, 0), color = "green", label='Y')
            self.ax.plot((0, 0), (1.25*min_axis_y, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*max_axis_y, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(0, 1.25*min_axis_y, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (1.25*min_axis_y, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*min_axis_y, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)

        if ((max_axis_z >= 0 ) and (min_axis_z >= 0)):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*max_axis_z), color = "slateblue", label='Z')
            self.ax.text(0, 0, 1.25*max_axis_z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_z >= 0 ) and (min_axis_z < 0)):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*max_axis_z), color = "slateblue", label='Z')
            self.ax.plot((0, 0), (0, 0), (1.25*min_axis_z, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*max_axis_z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(0, 0, 1.25*min_axis_z, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (0, 0), (1.25*min_axis_z, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*min_axis_z, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)

        # Letras en los vectores
        self.ax.text(3*a[0]/4, 3*a[1]/4, 3*a[2]/4, 'a', style='italic', fontweight='bold', color = str(colors[0]), fontsize=12)
        self.ax.text(3*b[0]/4, 3*b[1]/4, 3*b[2]/4, 'b', style='italic', fontweight='bold', color = str(colors[1]), fontsize=12)
        self.ax.text(3*c[0]/4, 3*c[1]/4, 3*c[2]/4, 'c', style='italic', fontweight='bold', color = str(colors[2]), fontsize=12)
        self.ax.text(3*resultado[0]/4, 3*resultado[1]/4, 3*resultado[2]/4, 'Resultante', style='italic', fontweight='bold', color = str(colors[3]), fontsize=12)
        self.ax.text(a[0], a[1], a[2], '(' + str(a[0]) + ', ' + str(a[1]) + ', '+ str(a[2]) + ')', 
                     style='italic', fontweight='bold', color = str(colors[0]), fontsize=12)
        self.ax.text(b[0], b[1], b[2], '(' + str(b[0]) + ', ' + str(b[1]) + ', '+ str(b[2]) + ')', 
                     style='italic', fontweight='bold', color = str(colors[1]), fontsize=12)
        self.ax.text(c[0], c[1], c[2], '(' + str(c[0]) + ', ' + str(c[1]) + ', '+ str(c[2]) + ')', 
                     style='italic', fontweight='bold', color = str(colors[2]), fontsize=12)
        self.ax.text(resultado[0], resultado[1], resultado[2], '(' + str(round(resultado[0],2)) + ', ' + str(round(resultado[1],2)) + ', '+ str(round(resultado[2],2)) + ')', 
                     style='italic', fontweight='bold', color = str(colors[3]), fontsize=12)

        for x in range(len(vector)):
            self.ax.quiver(0, 0, 0, vector[x][0], vector[x][1], vector[x][2], color = colors[x], label = labels[x], arrow_length_ratio=0.1)
    
        ## GRAFICACION DE VECTORES COMPLEMENTARIOS PARA LA SUMA DE VECTORES
        init_x = vector[0][0]
        init_y = vector[0][1]
        init_z = vector[0][2]
            
        for x in range(len(vector) - 2):
            end_x = vector[x + 1][0]
            end_y = vector[x + 1][1]
            end_z = vector[x + 1][2]
                
            self.ax.quiver(init_x, init_y, init_z, end_x, end_y, end_z, color = colors[x+1], label = labels[x+1] + "*", arrow_length_ratio=0.1, linestyle = '--')
                
            init_x = init_x + end_x
            init_y = init_y + end_y
            init_z = init_z + end_z
        
        # Impresion de la Leyenda
        plt.tight_layout()
        plt.legend(ncol = 6, loc = 8, draggable = True)

    #------------ Guardar gráfica -------------------------------------------------------------------------------------------------------------------------------------
    def guardar_graf(self, direccion):
        plt.savefig(direccion + "/SumaVectores.jpg")
    #------------ Borrar la gráfica -----------------------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

#*************************** Clase de Vectores de Suma (FIN) *********************************************************************************************************#

#*************************** Clase de Vectores de Producto Punto *****************************************************************************************************#
class Vectores_Punto_Vect(FigureCanvas):
    #------------------ Función Inicial -------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)
    
    #------------------ Producto Punto de Vector y escalar ------------------------------------------------------------------------------------------------------------
    def graficar_vector_punto(self, x1, y1, z1, x2, y2, z2, usuario):    
        self.ax.set_title("Hecho por: " + usuario , loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Ejemplo del producto punto entre dos vectores.")  
        self.ax.xaxis.set_label_text('Posición_X', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.yaxis.set_label_text('Posición_Y', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.zaxis.set_label_text('Posición_Z', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        a = np.array([x1, y1, z1])
        b = np.array([x2, y2, z2])

        colors = ['red', 'green', 'blue', 'orange', 'violet']

        vectorList = {
            "a" : a,
            "b" : b
        }

        resultado = v.DotProduct(a,b)
            
        vector = list(vectorList.values())
        labels = list(vectorList.keys())

        # Mostrando los valores de los vectores en los labels
        labels[0] = "-> " + str(labels[0]) 
        labels[1] = "-> " + str(labels[1]) 

        # Se establece como valor inicial de los limites de cada eje, el primer punto de cada eje
        # de la Grafica, enlistado en la lista de Vectores
        max_axis_x = min_axis_x = vector[0][0]
        max_axis_y = min_axis_y = vector[0][1]
        max_axis_z = min_axis_z = vector[0][2]
        
        # Se obtienen los puntos maximos y minimos de cada eje de la Grafica, recorriendo cada uno
        # de los ejes enlistados en la lista de Vectores
        for x in range(1, len(vector)):
            max_axis_x = max(max_axis_x, vector[x][0])
            max_axis_y = max(max_axis_y, vector[x][1])
            max_axis_z = max(max_axis_z, vector[x][2])
            min_axis_x = min(min_axis_x, vector[x][0])
            min_axis_y = min(min_axis_y, vector[x][1])
            min_axis_z = min(min_axis_z, vector[x][2])
        
        # En caso de que el minimo sea un num positivo, se reduce a 0, para que asi las lineas siempre
        # se grafiquen desde el eje 0
        min_axis_x = min(min_axis_x, 0)
        min_axis_y = min(min_axis_y, 0)
        min_axis_z = min(min_axis_z, 0)
        
        # Definicion de los ejes x, y, z que se marcaran para definir la grafica
        if ((max_axis_x >= 0 ) and (min_axis_x >= 0)):
            self.ax.plot((0, 1.25*max_axis_x), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.text(1.25*max_axis_x, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_x >= 0 ) and (min_axis_x < 0)):
            self.ax.plot((0, 1.25*max_axis_x), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.plot((1.25*min_axis_x, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*max_axis_x, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(1.25*min_axis_x, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((1.25*min_axis_x, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*min_axis_x, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        
        if ((max_axis_y >= 0 ) and (min_axis_y >= 0)):
            self.ax.plot((0, 0), (0, 1.25*max_axis_y), (0, 0), color = "green", label='Y')
            self.ax.text(0, 1.25*max_axis_y, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_y >= 0 ) and (min_axis_y < 0)):
            self.ax.plot((0, 0), (0, 1.25*max_axis_y), (0, 0), color = "green", label='Y')
            self.ax.plot((0, 0), (1.25*min_axis_y, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*max_axis_y, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(0, 1.25*min_axis_y, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (1.25*min_axis_y, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*min_axis_y, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)

        if ((max_axis_z >= 0 ) and (min_axis_z >= 0)):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*max_axis_z), color = "slateblue", label='Z')
            self.ax.text(0, 0, 1.25*max_axis_z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_z >= 0 ) and (min_axis_z < 0)):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*max_axis_z), color = "slateblue", label='Z')
            self.ax.plot((0, 0), (0, 0), (1.25*min_axis_z, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*max_axis_z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(0, 0, 1.25*min_axis_z, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (0, 0), (1.25*min_axis_z, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*min_axis_z, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)

        # Letras en los vectores
        self.ax.text(3*a[0]/4, 3*a[1]/4, 3*a[2]/4, 'a', style='italic', fontweight='bold', color = str(colors[0]), fontsize=12)
        self.ax.text(3*b[0]/4, 3*b[1]/4, 3*b[2]/4, 'b', style='italic', fontweight='bold', color = str(colors[1]), fontsize=12)
        self.ax.text(a[0], a[1], a[2], '(' + str(a[0]) + ', ' + str(a[1]) + ', '+ str(a[2]) + ')', 
                     style='italic', fontweight='bold', color = str(colors[0]), fontsize=12)
        self.ax.text(b[0], b[1], b[2], '(' + str(b[0]) + ', ' + str(b[1]) + ', '+ str(b[2]) + ')', 
                     style='italic', fontweight='bold', color = str(colors[1]), fontsize=12)
        self.ax.text(1.25*max_axis_x, 1.25*max_axis_y, 1.25*max_axis_z, "Producto Punto (a,b) = " + str(round(resultado,2)), color='black', style='italic', fontweight='bold', fontsize=12)

        for x in range(len(vector)):
            self.ax.quiver(0, 0, 0, vector[x][0], vector[x][1], vector[x][2], color = colors[x], label = labels[x], arrow_length_ratio=0.1)

        # Impresion de la Leyenda
        plt.tight_layout()
        plt.legend(ncol = 4, loc = 8, draggable = True)

    #------------ Guardar la gráfica ----------------------------------------------------------------------------------------------------------------------------------
    def guardar_graf(self, direccion):
        plt.savefig(direccion + "/ProductoPuntoVectores.jpg")
    #------------ Borrar la gráfica -----------------------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

#*************************** Clase de Vectores de Producto Punto (FIN) ***********************************************************************************************#

#*************************** Clase de Vectores de Producto Cruz ******************************************************************************************************#
class Vectores_Cruz_Vect(FigureCanvas):
    #------------------ Función Inicial -------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)
    
    #------------------ Producto cruz de dos vectores -----------------------------------------------------------------------------------------------------------------
    def graficar_vector_cruz(self, x1, y1, z1, x2, y2, z2, usuario):    
        self.ax.set_title("Hecho por: " + usuario , loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Ejemplo de un producto cruz de dos vectores.")  
        self.ax.xaxis.set_label_text('Posición_X', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.yaxis.set_label_text('Posición_Y', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.zaxis.set_label_text('Posición_Z', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        a = np.array([x1, y1, z1])
        b = np.array([x2, y2, z2])

        colors = ['red', 'green', 'blue', 'orange', 'violet']

        vectorList = {
            "a" : a,
            "b" : b
        }

        vector = list(vectorList.values())

        resultado = vector[0]

        for x in range(1, len(vectorList)):
            resultado = v.CrossProduct(resultado, vector[x])
            
        vectorList["Resultante"] = resultado
                
        vector = list(vectorList.values())
        labels = list(vectorList.keys())

        # Mostrando los valores de los vectores en los labels
        labels[0] = "-> " + str(labels[0]) 
        labels[1] = "-> " + str(labels[1]) 
        labels[2] = "-> " + str(labels[2]) 

        # Se establece como valor inicial de los limites de cada eje, el primer punto de cada eje
        # de la Grafica, enlistado en la lista de Vectores
        max_axis_x = min_axis_x = vector[0][0]
        max_axis_y = min_axis_y = vector[0][1]
        max_axis_z = min_axis_z = vector[0][2]
        
        # Se obtienen los puntos maximos y minimos de cada eje de la Grafica, recorriendo cada uno
        # de los ejes enlistados en la lista de Vectores
        for x in range(1, len(vector)):
            max_axis_x = max(max_axis_x, vector[x][0])
            max_axis_y = max(max_axis_y, vector[x][1])
            max_axis_z = max(max_axis_z, vector[x][2])
            min_axis_x = min(min_axis_x, vector[x][0])
            min_axis_y = min(min_axis_y, vector[x][1])
            min_axis_z = min(min_axis_z, vector[x][2])
        
        # En caso de que el minimo sea un num positivo, se reduce a 0, para que asi las lineas siempre
        # se grafiquen desde el eje 0
        min_axis_x = min(min_axis_x, 0)
        min_axis_y = min(min_axis_y, 0)
        min_axis_z = min(min_axis_z, 0)
        
        # Definicion de los ejes x, y, z que se marcaran para definir la grafica
        if ((max_axis_x >= 0 ) and (min_axis_x >= 0)):
            self.ax.plot((0, 1.25*max_axis_x), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.text(1.25*max_axis_x, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_x >= 0 ) and (min_axis_x < 0)):
            self.ax.plot((0, 1.25*max_axis_x), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.plot((1.25*min_axis_x, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*max_axis_x, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(1.25*min_axis_x, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((1.25*min_axis_x, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*min_axis_x, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        
        if ((max_axis_y >= 0 ) and (min_axis_y >= 0)):
            self.ax.plot((0, 0), (0, 1.25*max_axis_y), (0, 0), color = "green", label='Y')
            self.ax.text(0, 1.25*max_axis_y, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_y >= 0 ) and (min_axis_y < 0)):
            self.ax.plot((0, 0), (0, 1.25*max_axis_y), (0, 0), color = "green", label='Y')
            self.ax.plot((0, 0), (1.25*min_axis_y, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*max_axis_y, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(0, 1.25*min_axis_y, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (1.25*min_axis_y, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*min_axis_y, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)

        if ((max_axis_z >= 0 ) and (min_axis_z >= 0)):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*max_axis_z), color = "slateblue", label='Z')
            self.ax.text(0, 0, 1.25*max_axis_z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_z >= 0 ) and (min_axis_z < 0)):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*max_axis_z), color = "slateblue", label='Z')
            self.ax.plot((0, 0), (0, 0), (1.25*min_axis_z, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*max_axis_z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(0, 0, 1.25*min_axis_z, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (0, 0), (1.25*min_axis_z, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*min_axis_z, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)

        # Letras en los vectores
        self.ax.text(3*a[0]/4, 3*a[1]/4, 3*a[2]/4, 'a', style='italic', fontweight='bold', color = str(colors[0]), fontsize=12)
        self.ax.text(3*b[0]/4, 3*b[1]/4, 3*b[2]/4, 'b', style='italic', fontweight='bold', color = str(colors[1]), fontsize=12)
        self.ax.text(3*resultado[0]/4, 3*resultado[1]/4, 3*resultado[2]/4, 'Resultante', style='italic', fontweight='bold', color = str(colors[2]), fontsize=12)
        self.ax.text(a[0], a[1], a[2], '(' + str(a[0]) + ', ' + str(a[1]) + ', '+ str(a[2]) + ')', 
                     style='italic', fontweight='bold', color = str(colors[0]), fontsize=12)
        self.ax.text(b[0], b[1], b[2], '(' + str(b[0]) + ', ' + str(b[1]) + ', '+ str(b[2]) + ')', 
                     style='italic', fontweight='bold', color = str(colors[1]), fontsize=12)
        self.ax.text(resultado[0], resultado[1], resultado[2], '(' + str(round(resultado[0],2)) + ', ' + str(round(resultado[1],2)) + ', '+ str(round(resultado[2],2)) + ')', 
                     style='italic', fontweight='bold', color = str(colors[2]), fontsize=12)

        for x in range(len(vector)):
            self.ax.quiver(0, 0, 0, vector[x][0], vector[x][1], vector[x][2], color = colors[x], label = labels[x], arrow_length_ratio=0.1)
    
        # Impresion de la Leyenda
        plt.tight_layout()
        plt.legend(ncol = 4, loc = 8, draggable = True)

    #------------ Guardar la gráfica ----------------------------------------------------------------------------------------------------------------------------------
    def guardar_graf(self, direccion):
        plt.savefig(direccion + "/ProductoCruzVectores.jpg")
    #------------ Borrar la gráfica -----------------------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

#*************************** Clase de Vectores de Producto Cruz (FIN) ************************************************************************************************#