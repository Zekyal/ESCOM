# Archivo de Mensajes de Error y Advertencias de SSIG-3D

from PyQt5.QtWidgets import QMessageBox ## Para las ventanas de errores

# Función para el caso de no insertar un usuario.
def Error_Usuario(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error de Nombre de Usuario.")     # Inserta título a la ventana
    msg_box.setText("Favor de insertar un nombre de usuario.")     # Texto de la ventana
    msg_box.setInformativeText("Todos los módulos han sido bloqueados.")
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para el caso de cerrar sesión.
def Informacion_Cerrar_Sesion(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Cerrando sesión.")     # Inserta título a la ventana
    msg_box.setText("Se ha cerrado la sesión con exito. Insertar un nuevo usuario.")     # Texto de la ventana
    msg_box.setInformativeText("Todos los módulos han sido bloqueados.")
    msg_box.setIcon(QMessageBox.Information)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para el caso de cancelar al seleccionar dirección.
def Error_Direccion(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error al seleccionar destino de su gráfica.")     # Inserta título a la ventana
    msg_box.setText("Favor de seleccionar una carpeta válida.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para informar de la posición en que será guardada una simulación.
def Advertencia_PosicionSimulacion(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Posición de Guardado.")     # Inserta título a la ventana
    msg_box.setText("Tome en consideración que la posición actual de su simulación será como se muestre al guardar su archivo.")     # Texto de la ventana
    msg_box.setInformativeText("Coloque su simulación en una posición en la que se logren apreciar los valores que usted considere reelevantes.")
    msg_box.setIcon(QMessageBox.Information)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para advertir el caso de seleccionar la misma carpeta de guardado de una gráfica.
def Advertencia_Direccion(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Advertencia de selección de carpeta.")     # Inserta título a la ventana
    msg_box.setText("En caso de seleccionar una carpeta donde ya existe una gráfica de este módulo, la gráfica será sobreescrita.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Warning)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para advertir el caso de seleccionar la misma carpeta de guardado de una gráfica.
def Advertencia_ResultadosVector(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Observación de Resultados.")     # Inserta título a la ventana
    msg_box.setText("Se han obtenido algunos resultados reelevantes para este módulo.")     # Texto de la ventana
    msg_box.setInformativeText("Puede observarlos en la pestaña que lleva por nombre 'Resultados Obtenidos'.")
    msg_box.setIcon(QMessageBox.Information)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para advertir el caso de seleccionar la misma carpeta de guardado de una gráfica.
def Advertencia_TablaResultados(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Observación de Resultados.")     # Inserta título a la ventana
    msg_box.setText("Se ha llenado una tabla con los resultados de este ejemplo.")     # Texto de la ventana
    msg_box.setInformativeText("Puede observarlo en la pestaña que lleva por nombre 'Tabla de Resultados'.")
    msg_box.setIcon(QMessageBox.Information)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para el módulo de un vector, error en caso de que la magnitud del vector |v| = 0.
def Error_Vector_magnitud(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error al simular vector.")     # Inserta título a la ventana
    msg_box.setText("No es posible simular un vector con magnitud |v| = 0.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para el módulo de un vector, error en caso de insertar 0 como valores.
def Error_Coordenadas_valores(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error al simular vector.")     # Inserta título a la ventana
    msg_box.setText("Inserte valores diferentes de 0.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

#############################################  Errores de las Prácticas  #############################################################################################

# Función para el caso de no insertar un usuario.
def Error_Usuario_Pracs(self):    
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

# Función para el caso de insertar un valor de 0 a la MAgnitud.
def Error_Magnitud(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error en valor de la MAgnitud")     # Inserta título a la ventana
    msg_box.setText("Insertar un valor a 'Magnitud |v|' mayor de 0.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Information)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función de error en caso de que la carga sea igual a 0.
def Error_Carga(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error al insertar valor de carga.")     # Inserta título a la ventana
    msg_box.setText("Inserte valores mayores o menores a 0.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

def Error_Tipo(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error al seleccionar valores.")     # Inserta título a la ventana
    msg_box.setText("Selecciona un tipo de valor (Radianes o Grados).")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

def Error_Velocidades_Tiro_Par(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error al insertar Valores de Velocidades Iniciales.")     # Inserta título a la ventana
    msg_box.setText("Inserta Valores diferentes de 0 a las Velocidades Iniciales.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error