import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Datos
p_hat = 0.45
n = 800
z_value = 2.33  # Valor z para un intervalo de confianza del 98%

# Calcula el intervalo de confianza
margin_of_error = z_value * np.sqrt((p_hat * (1 - p_hat)) / n)
confidence_interval = (p_hat - margin_of_error, p_hat + margin_of_error)

# Visualización
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))

# Dibuja una línea vertical para la proporción muestral
plt.axvline(p_hat, color='blue', linestyle='dashed', linewidth=2, label='Proporción Muestral')

# Dibuja el intervalo de confianza
plt.plot(confidence_interval, [0, 0], color='red', linewidth=2, marker='o', markersize=8, label='Intervalo de Confianza')

# Etiquetas y leyendas
plt.title('Intervalo de Confianza del 98% para la Proporción de Mejora del Cine')
plt.xlabel('Proporción')
plt.legend()
plt.show()
