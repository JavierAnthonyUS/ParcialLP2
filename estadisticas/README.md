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

## 📦 Instalación

### Requisitos
- Python 3.7 o superior
- No requiere librerías externas (implementación pura en Python)

### Pasos de instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/JavierAnthonyUS/ParcialLP2.git
cd ParcialLP2/estadisticas
```

2. **Verificar la instalación:**
```bash
python test_estadisticas.py
```

## 🚀 Guía de Uso

### Ejemplo 1: Análisis de Datos Cuantitativos
```python
from core import AnalizadorCuantitativo

# Datos de ejemplo: calificaciones de estudiantes
calificaciones = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91, 87, 83, 94, 86, 90]

# Crear el analizador
analizador = AnalizadorCuantitativo(calificaciones)

# Obtener estadísticas
print(f"Media: {analizador.media():.2f}")
print(f"Mediana: {analizador.mediana():.2f}")
print(f"Desviación Estándar: {analizador.desviacion_estandar():.2f}")
print(f"Coeficiente de Variación: {analizador.coeficiente_variacion():.2f}%")

# Obtener cuartiles
q1, q2, q3 = analizador.cuartiles()
print(f"Q1: {q1:.2f}, Q2: {q2:.2f}, Q3: {q3:.2f}")

# Resumen completo
resumen = analizador.resumen()
for clave, valor in resumen.items():
    print(f"{clave}: {valor}")
```

**Salida esperada:**
```
Media: 87.33
Mediana: 88.00
Desviación Estándar: 5.42
Coeficiente de Variación: 6.21%
Q1: 84.00, Q2: 88.00, Q3: 91.00
```
