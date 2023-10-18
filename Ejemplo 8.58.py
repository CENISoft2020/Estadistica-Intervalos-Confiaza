import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Datos
media_muestral = 5.4
desviacion_estandar_muestral = 3.1
tamaño_muestra = 500
nivel_confianza = 0.95

# Valor crítico de Z para un intervalo de confianza del 95%
valor_critico_z = 1.96

# Calcula el margen de error
margen_error = valor_critico_z * (desviacion_estandar_muestral / np.sqrt(tamaño_muestra))

# Calcula el intervalo de confianza
intervalo_confianza = (media_muestral - margen_error, media_muestral + margen_error)

# Datos para la campana de Gauss
x = np.linspace(media_muestral - 4 * desviacion_estandar_muestral, media_muestral + 4 * desviacion_estandar_muestral, 1000)
y = stats.norm.pdf(x, loc=media_muestral, scale=desviacion_estandar_muestral)

# Gráfico
plt.figure(figsize=(10, 6))

# Curva de la campana de Gauss
plt.plot(x, y, label='Campana de Gauss', color='black')

# Relleno para el intervalo de confianza
plt.fill_between(x, y, where=[(xi >= intervalo_confianza[0]) and (xi <= intervalo_confianza[1]) for xi in x], color='red', alpha=0.5, label='Intervalo de Confianza')

# Etiquetas y leyendas
plt.title('Intervalo de Confianza del 95% para la Duración Media de Permanencia')
plt.xlabel('Duración Media de Permanencia (días)')
plt.ylabel('Densidad de Probabilidad')
plt.legend()

# Muestra el gráfico
plt.show()
