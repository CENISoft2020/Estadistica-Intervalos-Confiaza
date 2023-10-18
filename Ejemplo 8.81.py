import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Datos
media_muestra = 60.8
desviacion_estandar_muestra = 8
tamaño_muestra = 10

# Valor crítico de t para un intervalo de confianza del 95%
valor_critico_t = stats.t.ppf(0.975, df=tamaño_muestra - 1)  # Para un intervalo de confianza del 95%

# Calcula el margen de error
margen_error = valor_critico_t * (desviacion_estandar_muestra / np.sqrt(tamaño_muestra))

# Calcula el intervalo de confianza
intervalo_confianza = (media_muestra - margen_error, media_muestra + margen_error)

# Datos para la campana de Gauss
x = np.linspace(media_muestra - 4 * margen_error, media_muestra + 4 * margen_error, 1000)
y = stats.norm.pdf(x, loc=media_muestra, scale=margen_error)

# Gráfico
plt.figure(figsize=(10, 6))

# Curva de la campana de Gauss
plt.plot(x, y, label='Campana de Gauss', color='black')

# Relleno para el intervalo de confianza
plt.fill_between(x, y, where=[(xi >= intervalo_confianza[0]) and (xi <= intervalo_confianza[1]) for xi in x], color='red', alpha=0.5, label='Intervalo de Confianza')

# Etiquetas y leyendas
plt.title('Intervalo de Confianza del 95% para la Longitud Media de Caparazón de Langostas T. orientalis')
plt.xlabel('Longitud Media de Caparazón (mm)')
plt.ylabel('Densidad de Probabilidad')
plt.legend()

# Muestra el gráfico
plt.show()
