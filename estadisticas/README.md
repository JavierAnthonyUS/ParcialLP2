# 📊 ParcialLP2: Librería de Análisis Estadístico

Este repositorio contiene una librería desarrollada en Python para realizar cálculos de estadística descriptiva, utilizando los principios de la Programación Orientada a Objetos (POO).

## 👥 Integrantes del Grupo

| Nombre | GitHub |
|--------|--------|
| Fiorella Fuentes | [@FiorellaFuentes] |
| Javier Anthony Uraco | [@JavierAnthonyUS] |
| Sebastian Fernandez | [@SebastianFernandez] |

**Institución:** Universidad Nacional Agraria la Molina  
**Curso:** Lenguaje de Programación 2 
**Profesor:** Ana Vargas 

## 📖 Descripción

Es una librería completa que permite realizar análisis estadístico descriptivo tanto de datos **cuantitativos** (numéricos) como **cualitativos** (categóricos), además de análisis de relaciones entre variables (**bivariado**).

La librería está completamente implementada usando los principios de **Programación Orientada a Objetos**, incluyendo:
- ✅ **Abstracción** mediante clases abstractas
- ✅ **Encapsulamiento** de datos y métodos privados
- ✅ **Herencia** con jerarquía de clases
- ✅ **Polimorfismo** con implementaciones específicas

## 🎯 Características Principales

### Análisis de Datos Cuantitativos
- Medidas de tendencia central (media, mediana, moda)
- Medidas de dispersión (varianza, desviación estándar, coeficiente de variación, rango, IQR)
- Medidas de posición (percentiles, cuartiles)
- Medidas de forma (asimetría, curtosis)
- Resumen de cinco números de Tukey

### Análisis de Datos Cualitativos
- Moda y distribución de frecuencias
- Tablas de frecuencia (absoluta, relativa, porcentual, acumulada)
- Medidas de diversidad (entropía de Shannon, índice de Simpson)

### Análisis Bivariado
- Covarianza entre variables
- Correlación de Pearson
- Coeficiente de determinación (R²)
- Regresión lineal simple

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