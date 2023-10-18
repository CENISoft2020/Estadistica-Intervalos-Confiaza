import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import norm

# Datos
p_hat = 0.45
n = 800
z_value = 2.33  # Valor z para un intervalo de confianza del 98%

# Calcula el intervalo de confianza
margin_of_error = z_value * np.sqrt((p_hat * (1 - p_hat)) / n)
confidence_interval = (p_hat - margin_of_error, p_hat + margin_of_error)

# Crear un rango de valores para la curva de la campana de Gauss
x = np.linspace(0, 1, 1000)

# Calcula la función de densidad de probabilidad de la distribución normal
y = norm.pdf(x, p_hat, np.sqrt((p_hat * (1 - p_hat)) / n))

# Visualización
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))

# Dibuja la campana de Gauss
plt.plot(x, y, color='black', label='Campana de Gauss')

# Rellena el área correspondiente al intervalo de confianza
plt.fill_betweenx(y, confidence_interval[0], confidence_interval[1], color='red', alpha=0.5, label='Intervalo de Confianza')

# Etiquetas y leyendas
plt.title('Intervalo de Confianza del 98% para la Proporción de Mejora del Cine (Campana de Gauss)')
plt.xlabel('Proporción')
plt.legend()
plt.show()
