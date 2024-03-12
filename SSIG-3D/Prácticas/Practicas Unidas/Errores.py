# Archivo con las funciones de mensajes de Error de todas las prácticas.

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

# Función para el caso de cancelar al seleccionar dirección.
def Error_Direccion(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error al seleccionar destino de su gráfica.")     # Inserta título a la ventana
    msg_box.setText("Favor de seleccionar una carpeta válida.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para el caso de no seleccionar el tipo de los Cosenos.
def Error_Tipo(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error de selección de tipo de α, β y ɣ.")     # Inserta título a la ventana
    msg_box.setText("Favor de seleccionar el tipo de valor de los cosenos.")     # Texto de la ventana
    msg_box.setInformativeText("Seleccione el botón de 'Grados' o 'Radianes' para todos los Cosenos.")
    msg_box.setIcon(QMessageBox.Information)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para el caso de insertar un valor de 0 a la MAgnitud.
def Error_Magnitud(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error en valor de la MAgnitud")     # Inserta título a la ventana
    msg_box.setText("Insertar un valor a 'Magnitud |v|' mayor de 0.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Information)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función de error en caso de que la magnitud del vector |v| = 0.
def Error_Vector_magnitud(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error al simular vector.")     # Inserta título a la ventana
    msg_box.setText("No es posible simular un vector con magnitud |v| = 0.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función de error en caso de que la carga sea igual a 0.
def Error_Carga(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error al insertar valor de carga.")     # Inserta título a la ventana
    msg_box.setText("Inserte valores mayores o menores a 0.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error
