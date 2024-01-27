import matplotlib.pyplot as plt
import numpy as np

# Definir las funciones
def f1(x):
    return x**2

def f2(x):
    return -x**2 + 4

# Crear valores de x
x_values = np.linspace(-2, 2, 100)

# Calcular los valores de y para cada función
y1_values = f1(x_values)
y2_values = f2(x_values)

# Graficar las funciones
plt.plot(x_values, y1_values, label='y = x^2')
plt.plot(x_values, y2_values, label='y = -x^2 + 4')

# Marcar el punto de intersección
intersection_x = np.sqrt(2)
intersection_y = 2
plt.scatter([intersection_x], [intersection_y], color='red', label='Intersección')

# Configuración del gráfico
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Intersección de dos funciones cuadráticas')
plt.xlabel('x')
plt.ylabel('y')

# Mostrar el gráfico
plt.show()
