# 📊 ParcialLP2: Librería de Análisis Estadístico

Este repositorio contiene una librería desarrollada en Python para realizar cálculos de estadística descriptiva, utilizando los principios de la Programación Orientada a Objetos (POO).

## 📝 Descripción

La librería permite analizar de forma sencilla conjuntos de datos, tanto cuantitativos como cualitativos. Su diseño modular facilita la obtención de un resumen completo de las métricas estadísticas más importantes para cada tipo de dato.

## 🚀 Características Implementadas

La librería se estructura en torno a las siguientes clases de análisis:

- **`AnalizadorCuantitativo`**:
  - Cálculo de media, mediana, moda, varianza, desviación estándar, percentiles, cuartiles y más.

- **`AnalizadorCualitativo`**:
  - Generación de tablas de frecuencia (absoluta, relativa y porcentual).
  - Cálculo de la moda y métricas de diversidad como la entropía.

- **`AnalizadorBivariado`**:
  - Cálculo de covarianza, correlación de Pearson y regresión lineal simple.

## 🧑‍💻 Integrantes del Equipo

- **Javier Anthony Uraco Silva**
- **Sebastian Fernandez**
- **Fiorella Fuentes**

## 💡 Ejemplo de Uso

Para utilizar la librería, simplemente importa la clase que necesites y pásale tu lista de datos.

```python
# Importa la clase desde el módulo
from estadisticas.core import AnalizadorCuantitativo

# 1. Define tu conjunto de datos
edades =

# 2. Crea una instancia del analizador
analizador = AnalizadorCuantitativo(edades)

# 3. Obtén los resultados
print("Media de edades:", analizador.media())
print("Desviación Estándar:", analizador.desviacion_estandar())

# O un resumen completo
print("\nResumen completo:")
print(analizador.resumen())