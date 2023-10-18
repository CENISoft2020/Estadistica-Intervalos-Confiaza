import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Datos
proporcion_muestra = 0.78
nivel_confianza = 0.90
tamaño_muestra = 1030

# Valor crítico de Z para un intervalo de confianza del 90%
valor_critico_z = 1.645

# Calcula el margen de error
margen_error = valor_critico_z * np.sqrt((proporcion_muestra * (1 - proporcion_muestra)) / tamaño_muestra)

# Calcula el intervalo de confianza
intervalo_confianza = (proporcion_muestra - margen_error, proporcion_muestra + margen_error)

# Datos para la campana de Gauss
x = np.linspace(proporcion_muestra - 4 * margen_error, proporcion_muestra + 4 * margen_error, 1000)
y = stats.norm.pdf(x, loc=proporcion_muestra, scale=margen_error)

# Gráfico
plt.figure(figsize=(10, 6))

# Curva de la campana de Gauss
plt.plot(x, y, label='Campana de Gauss', color='black')

# Relleno para el intervalo de confianza
plt.fill_between(x, y, where=[(xi >= intervalo_confianza[0]) and (xi <= intervalo_confianza[1]) for xi in x], color='red', alpha=0.5, label='Intervalo de Confianza')

# Etiquetas y leyendas
plt.title('Intervalo de Confianza del 90% para la Proporción de "Preadolescentes"')
plt.xlabel('Proporción')
plt.ylabel('Densidad de Probabilidad')
plt.legend()

# Muestra el gráfico
plt.show()
