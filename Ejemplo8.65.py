import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Datos
media1 = 24.8
desviacion_estandar1 = np.sqrt(50.41)
tamaño_muestra1 = 34

media2 = 21.3
desviacion_estandar2 = np.sqrt(65.61)
tamaño_muestra2 = 41

nivel_confianza = 0.99

# Valor crítico de Z para un intervalo de confianza del 99%
valor_critico_z = 2.576

# Calcula el margen de error
margen_error = valor_critico_z * np.sqrt((desviacion_estandar1**2 / tamaño_muestra1) + (desviacion_estandar2**2 / tamaño_muestra2))

# Calcula el intervalo de confianza
intervalo_confianza = (media1 - media2 - margen_error, media1 - media2 + margen_error)

# Datos para la campana de Gauss
x = np.linspace((media1 - media2) - 4 * margen_error, (media1 - media2) + 4 * margen_error, 1000)
y = stats.norm.pdf(x, loc=(media1 - media2), scale=margen_error)

# Gráfico
plt.figure(figsize=(10, 6))

# Curva de la campana de Gauss
plt.plot(x, y, label='Campana de Gauss', color='black')

# Relleno para el intervalo de confianza
plt.fill_between(x, y, where=[(xi >= intervalo_confianza[0]) and (xi <= intervalo_confianza[1]) for xi in x], color='red', alpha=0.5, label='Intervalo de Confianza')

# Etiquetas y leyendas
plt.title('Intervalo de Confianza del 99% para la Diferencia en Tiempo Promedio de Muda')
plt.xlabel('Diferencia en Tiempo Promedio de Muda (días)')
plt.ylabel('Densidad de Probabilidad')
plt.legend()

# Muestra el gráfico
plt.show()
