import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Datos
diferencia_medias = 3.4
margen_error = 3.1848

# Calcula el intervalo de confianza
intervalo_confianza = (diferencia_medias - margen_error, diferencia_medias + margen_error)

# Datos para la campana de Gauss
x = np.linspace(diferencia_medias - 4 * margen_error, diferencia_medias + 4 * margen_error, 1000)
y = stats.norm.pdf(x, loc=diferencia_medias, scale=margen_error)

# Gráfico
plt.figure(figsize=(10, 6))

# Curva de la campana de Gauss
plt.plot(x, y, label='Campana de Gauss', color='black')

# Relleno para el intervalo de confianza
plt.fill_between(x, y, where=[(xi >= intervalo_confianza[0]) and (xi <= intervalo_confianza[1]) for xi in x], color='red', alpha=0.5, label='Intervalo de Confianza')

# Etiquetas y leyendas
plt.title('Intervalo de Confianza del 95% para la Diferencia en la Media de las Presiones en Reposo')
plt.xlabel('Diferencia en la Media de las Presiones en Reposo')
plt.ylabel('Densidad de Probabilidad')
plt.legend()

# Muestra el gráfico
plt.show()
