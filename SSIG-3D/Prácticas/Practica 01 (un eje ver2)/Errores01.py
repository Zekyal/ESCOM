# Práctica 01. Archivo con las funciones de mensajes de Error.

from PyQt5.QtWidgets import QMessageBox ## Para las ventanas de errores

# Función para el caso de no insertar un usuario.
def Error_Usuario(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error de Nombre de Usuario.")     # Inserta título a la ventana
    msg_box.setText("Favor de insertar un nombre de usuario.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Information)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para el caso de no insertar un polinomio de grado 2.
def Error_Grado2(self):
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Valores Erroneos.")     # Inserta título a la ventana
    msg_box.setText("Insertar un valor en la casilla c(2).")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para el caso de no insertar un polinomio de grado 3.
def Error_Grado3(self):
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Valores Erroneos.")     # Inserta título a la ventana
    msg_box.setText("Insertar un valor en la casilla c(3).")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para el caso de no insertar un polinomio de grado 4.
def Error_Grado4(self):
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Valores Erroneos.")     # Inserta título a la ventana
    msg_box.setText("Insertar un valor en la casilla c(4).")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para el caso de no insertar un polinomio de grado 5.
def Error_Grado5(self):
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Valores Erroneos.")     # Inserta título a la ventana
    msg_box.setText("Insertar un valor en la casilla c(5).")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error
