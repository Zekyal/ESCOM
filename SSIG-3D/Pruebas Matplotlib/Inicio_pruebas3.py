## Importando las clases de las gráficas de otro documento (Prueba Exitosa)

import sys
from PyQt5 import uic, QtWidgets
from Graficando import Canvas_grafica, Canvas_grafica2 ## Archivo del que obtenemos las clases de las gráficas.

qtCreatorFile = "graficas.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES --------------------------------

        x = [5, 10, 15, 20, 5, 25, 30, 15, 20, 40]
        y = [2, 4, 6, 1, 5, 8, 10, 12, 4, 14]

        self.grafica1 = Canvas_grafica()
        self.graf01.addWidget(self.grafica1)
        self.grafica1.test01(x, y)

        self.grafica2 = Canvas_grafica2()       
        self.graf02.addWidget(self.grafica2)        
        self.grafica2.test02(y, x)
        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())