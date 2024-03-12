# Práctica 08. Caida Libre. (SSIS-3D)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import win32com.client as win32

from Graficas_Practica08 import Caida_libre, Caida_libre2

class Prac08(QMainWindow):
    def __init__(self, parent=None):
        super(Prac08, self).__init__(parent)
        loadUi('Interfaces\Practica08.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_graficar.clicked.connect(self.graficarCaidaLibre)      
        self.button_tabla.clicked.connect(self.guardar_tabla)      
        
    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        if hasattr(self, 'graficaCaida'):
            self.graficaCaida.cerrarGraf()
            self.graficaCaida2.cerrarGraf()
        self.parent().show()
        self.close()
    #-------- Función de cerrar (FIN) ---------------------------------------

    #-------- Función para la graficación ------------------------------------
    def graficarCaidaLibre(self):

        self.button_graficar.setEnabled(False)
        self.button_tabla.setEnabled(True)

        # Tomamos valores de las constantes en los spinbox
        Yo = float(self.sBox_Yo.text())    
        Voy = float(self.sBox_Voy.text())    
        tiempo = float(self.sBox_tiempo.text())
        g = 9.81 

        pos = []
        tempo = []
        vel = []        

        self.tabla_libre.setRowCount(int(tiempo)*10+1)

        for t in range(0, int(tiempo)*10 + 1, 1):    # Hacemos las 20 repeticiones para guardar los valores en la tabla
            tempo.append(t/10)
            self.tabla_libre.setItem(t, 0, QtWidgets.QTableWidgetItem(str(tempo[t])))    # Mete los valores a la tabla llamada "tabla_vel" en la columna Tiempo
            pos.append(Yo + Voy*(t/10) - 1/2*g*float(pow(t/10, 2)))   # Ingresa los valores a la lista "pos", haciendo las sustituciones en el polinomio de X
            self.tabla_libre.setItem(t, 1, QtWidgets.QTableWidgetItem(str(pos[t])))   # Mete los valores a la tabla llamada "tabla_pos" en la columna Posición
            vel.append(Voy - g*(t/10))   # Ingresa los valores a la lista "vel", haciendo las sustituciones en el polinomio
            self.tabla_libre.setItem(t, 2, QtWidgets.QTableWidgetItem(str(vel[t])))   # Mete los valores a la tabla llamada "tabla_vel" en la columna Posición

        self.graficaCaida = Caida_libre()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_pos.addWidget(self.graficaCaida)     #Agregamos la gráfica al widget.
        self.graficaCaida.graficarPosicionY(pos, tempo)   # Trabajamos con la gráfica

        self.graficaCaida2 = Caida_libre2()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_vel.addWidget(self.graficaCaida2)     #Agregamos la gráfica al widget.
        self.graficaCaida2.graficarVelocidadY(pos, vel, tempo)   # Trabajamos con la gráfica

    #-------- Función para la graficación (FIN) -----------------------------------

    def guardar_tabla(self):
        xlApp = win32.Dispatch('Excel.Application')
        xlApp.Visible = True

        # create a new excel workbook
        wb = xlApp.Workbooks.Add()

        # create a new excel worksheet
        ws = wb.worksheets.add
        ws.name = 'Caida Libre (Datos)'

        rows = []
        columnHeaders = []

        # retrieve columns label
        for j in range(self.tabla_libre.model().columnCount()):
            columnHeaders.append(self.tabla_libre.horizontalHeaderItem(j).text())

        # retrieve table content
        for row in range(self.tabla_libre.rowCount()):
            record = []
            for col in range(self.tabla_libre.columnCount()):
                record.append(self.tabla_libre.item(row, col).text())
            rows.append(record)

        # insert table content to Excel
        ws.Range(
            ws.cells(2, 1),
            ws.cells(len(rows)+1, len(columnHeaders))
        ).value = rows

        # insert column labels To Excel
        ws.Range(
            ws.cells(1, 1),
            ws.cells(1, len(columnHeaders))
        ).value = columnHeaders


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac08()
    window.show()
    sys.exit(app.exec_())