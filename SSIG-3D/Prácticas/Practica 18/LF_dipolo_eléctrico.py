import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp

def electric_field(x, y, z, q1, q2, k, d):
    r1 = np.array([x - d/2, y, z])
    r2 = np.array([x + d/2, y, z])

    smoothing_factor = 1e-12
    r1_mag = np.sqrt(np.sum(r1**2) + smoothing_factor)
    r2_mag = np.sqrt(np.sum(r2**2) + smoothing_factor)

    E1 = k * q1 / r1_mag**3 * r1
    E2 = k * q2 / r2_mag**3 * r2

    E_total = E1 + E2
    return E_total[0], E_total[1], E_total[2]

def field_line(t, pos, q1, q2, k, d):
    x, y, z = pos
    Ex, Ey, Ez = electric_field(x, y, z, q1, q2, k, d)
    return [Ex, Ey, Ez]

def stop_event(t, y, q1, q2, k, d):
    return np.sqrt((y[0] - (-d/2))**2 + y[1]**2 + y[2]**2) - distance_threshold

stop_event.terminal = True

k = 8.9875517923e9
q1 = 25e-19
q2 = -25e-19
d = 1e-3
distance_threshold = 1e-3 * d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Líneas de flujo y campo eléctrico para dos cargas")

# condiciones iniciales

theta_divisions = 5  #numero de divisiones en theta (angulo en esféricas respecto al eje Z)
phi_divisions = 9    #número de divisiones en phi  (ángulo respecto al eje x)

event_positions = []
num_vectors_per_streamline = 8

for i in range(theta_divisions):
    for j in range(phi_divisions):
        theta = i * np.pi / theta_divisions
        phi = j * 2 * np.pi / phi_divisions

        x0 = d/2 + distance_threshold * np.sin(theta) * np.cos(phi)
        y0 = distance_threshold * np.sin(theta) * np.sin(phi)
        z0 = distance_threshold * np.cos(theta)

        sol = solve_ivp(field_line, [0, 12], [x0, y0, z0], args=(q1, q2, k, d), rtol=1e-8, atol=1e-8, events=stop_event)

        if sol.status == 1:  # Event was triggered, indicating close proximity to q2
            sol.t_events[0] = np.append(sol.t_events[0], sol.t[-1])
            #sol.y_events[0] = np.column_stack((sol.y_events[0], sol.y[:,-1]))
            event_positions.append(sol.y[:, -1].reshape(3, 1))
            #sol.y_events[0] = np.hstack((sol.y_events[0], sol.y[:, -1].reshape(3, 1)))


        ax.plot(sol.y[0], sol.y[1], sol.y[2], color='blue', linestyle='dashed')

        num_points = len(sol.y[0])
        vector_indices = np.linspace(0, num_points - 1, num_vectors_per_streamline, dtype=int)

        for idx in vector_indices:
            x, y, z = sol.y[0][idx], sol.y[1][idx], sol.y[2][idx]
            Ex, Ey, Ez = electric_field(x, y, z, q1, q2, k, d)
            E = np.sqrt(Ex**2 + Ey**2 + Ez**2)

            epsilon = 1e-9
            ax.quiver(x, y, z, Ex/(E + epsilon), Ey/(E + epsilon), Ez/(E + epsilon), length=0.3*d, color='red')
event_positions = np.hstack(event_positions)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim([-2*d, 2*d])
ax.set_ylim([-2*d, 2*d])
ax.set_zlim([-2*d, 2*d])


plt.show()
