import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Solicitar al usuario los valores de las masas y la aceleración
m1 = 10
m2 = 5
m3 = 14
a = 5

# Calcular las fuerzas de acción y reacción
F12 = (m1 + m2) * a
F21 = -F12
F23 = (m2 + m3) * a
F32 = -F23

# Crear el gráfico
fig, ax = plt.subplots()

# Dibujar los cuadrados representando las masas
rec1 = Rectangle((0, 0), 1, 1, fill=True, edgecolor='black', facecolor='orange')
rec2 = Rectangle((1, 0), 1, 1, fill=True, edgecolor='black', facecolor='white')
rec3 = Rectangle((2, 0), 1, 1, fill=True, edgecolor='black', facecolor='turquoise')

ax.add_patch(rec1)
ax.add_patch(rec2)
ax.add_patch(rec3)

# Etiquetar las masas
plt.text(0.5, 0.5, f'm1 = {m1}', color='black', weight='bold', ha='center', va='center', fontsize=18)
plt.text(1.5, 0.5, f'm2 = {m2}', color='black', weight='bold', ha='center', va='center', fontsize=18)
plt.text(2.5, 0.5, f'm3 = {m3}', color='black', weight='bold', ha='center', va='center', fontsize=18)

# Etiquetar la aceleración en la parte inferior en formato LaTeX
plt.text(1.5, -0.1, r'$\vec{a} =' + str(a) + '\hat{i}$', color='black', ha='center', va='center', fontsize=18)


# Dibujar los vectores de fuerza
plt.arrow(0.6, 0.6, 0.4, 0, head_width=0.05, head_length=0.1, fc='red', ec='red')
plt.arrow(1.4, 0.4, -0.4, 0, head_width=0.05, head_length=0.1, fc='red', ec='red')
plt.arrow(1.6, 0.6, 0.4, 0, head_width=0.05, head_length=0.1, fc='red', ec='red')
plt.arrow(2.4, 0.4, -0.4, 0, head_width=0.05, head_length=0.1, fc='red', ec='red')

# Etiquetar las fuerzas
plt.text(0.85, 0.65, f'F12 = {F12}', color='black', ha='center', va='center', fontsize=12)
plt.text(1.15, 0.35, f'F21 = {F21}', color='black', ha='center', va='center', fontsize=12)
# Etiquetar las fuerzas
plt.text(1.85, 0.65, f'F23 = {F23}', color='black', ha='center', va='center', fontsize=12)
plt.text(2.15, 0.35, f'F32 = {F32}', color='black', ha='center', va='center', fontsize=12)

# Configurar los límites de los ejes y mostrar el gráfico
ax.set_xlim([0, 3])
ax.set_ylim([0, 1])

plt.title('TERCERA LEY DE NEWTON [MKS]', fontsize=20)

plt.axis('off')
plt.show()

