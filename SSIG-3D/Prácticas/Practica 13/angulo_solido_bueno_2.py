import sys
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ángulo sólido')
        self.setGeometry(500, 500, 800, 800)

        vbox = QVBoxLayout()

        self.label = QLabel('Ingrese el ángulo θ en grados:')
        self.label.setStyleSheet('font-size: 24px; background-color: lightblue; color: darkred')  # Cambia el tamaño del texto en la etiqueta
        vbox.addWidget(self.label)

        self.line_edit = QLineEdit()
        self.line_edit.setStyleSheet('font-size: 24px; background-color: white; color: blue')  # Cambia el tamaño del texto en el campo de entrada
        self.line_edit.setFixedHeight(40)  # Cambia la altura del campo de entrada
        vbox.addWidget(self.line_edit)


        self.button = QPushButton('Calcular')
        self.button.setStyleSheet('font-size: 24px; background-color: lightblue; color: darkred')  # Cambia el tamaño del texto en la etiqueta

        self.button.clicked.connect(self.calculate)
        vbox.addWidget(self.button)

        self.figure = plt.figure(figsize=(10,10))
        self.canvas = FigureCanvas(self.figure)
        vbox.addWidget(self.canvas)

        self.setLayout(vbox)

    def calculate(self):
        theta_deg = float(self.line_edit.text())
        theta_cone = np.deg2rad(theta_deg)

        solid_angle = 2 * np.pi * (1 - np.cos(theta_cone))
        solid_angle_pi = solid_angle / np.pi
        fraction = sp.Rational(solid_angle_pi).limit_denominator(100)

        self.label.setText(f'Ángulo sólido subtendido por el cono: {fraction}π estereorradianes')

        self.plot_figure(theta_cone)

    def plot_figure(self, theta_cone):
        radius = 1
        phi = np.linspace(0, 2 * np.pi, 100)
        theta = np.linspace(0, np.pi, 100)
        phi, theta = np.meshgrid(phi, theta)

        x = radius * np.sin(theta) * np.cos(phi)
        y = radius * np.sin(theta) * np.sin(phi)
        z = radius * np.cos(theta)

        r_cone = np.linspace(0, radius, 100)
        cone_phi = np.linspace(0, 2 * np.pi, 100)
        r_cone, cone_phi = np.meshgrid(r_cone, cone_phi)

        cone_x = r_cone * np.sin(theta_cone) * np.cos(cone_phi)
        cone_y = r_cone * np.sin(theta_cone) * np.sin(cone_phi)
        cone_z = r_cone * np.cos(theta_cone)

        self.figure.clear()

        ax = self.figure.add_subplot(111, projection='3d')
        ax.set_box_aspect([1, 1, 1])

        ax.plot_surface(x, y, z, color='lightskyblue', alpha=0.6, rstride=1, cstride=1)
        ax.plot_surface(cone_x, cone_y, cone_z, color='gray', alpha=0.3, rstride=1, cstride=1)

        mask = theta <= theta_cone
        x_intersect = x[mask]
        y_intersect = y[mask]
        z_intersect = z[mask]

        ax.scatter(x_intersect, y_intersect, z_intersect, color='red', s=1, alpha=1)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
        ax.set_box_aspect([1, 1, 1])
        ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        ax.grid(False)
        
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
