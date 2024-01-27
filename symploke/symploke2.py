import matplotlib.pyplot as plt
import numpy as np

# Definir las ecuaciones de los círculos
def circle1(x):
    return np.sqrt(1 - x**2)

def circle2(x):
    return -np.sqrt(1 - x**2)

# Crear valores de x
x_values = np.linspace(-1, 1, 100)

# Calcular los valores de y para cada círculo
y1_values = circle1(x_values)
y2_values = circle2(x_values)

# Graficar los círculos
plt.plot(x_values, y1_values, label='Círculo 1')
plt.plot(x_values, y2_values, label='Círculo 2')

# Marcar el punto de intersección (0, 1)
plt.scatter([0], [1], color='red', label='Intersección')

# Configuración del gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Intersección de dos círculos')
plt.xlabel('x')
plt.ylabel('y')

# Mostrar el gráfico
plt.show()
