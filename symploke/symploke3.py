import matplotlib.pyplot as plt
import numpy as np

# Definir el radio de los círculos
radio = 1

# Definir el centro del primer círculo
centro1 = (-radio, 0)

# Definir el centro del segundo círculo
centro2 = (radio, 0)

# Crear valores de theta para ambos círculos
theta = np.linspace(0, 2 * np.pi, 100)

# Coordenadas polares del primer círculo
x1_values = centro1[0] + radio * np.cos(theta)
y1_values = centro1[1] + radio * np.sin(theta)

# Coordenadas polares del segundo círculo
x2_values = centro2[0] + radio * np.cos(theta)
y2_values = centro2[1] + radio * np.sin(theta)

# Graficar los círculos
plt.plot(x1_values, y1_values, label='Círculo 1')
plt.plot(x2_values, y2_values, label='Círculo 2')

# Configuración del gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Symploke.Dos círculos adyacentes que se tocan')
plt.xlabel('x')
plt.ylabel('y')

# Mostrar el gráfico
plt.show()
