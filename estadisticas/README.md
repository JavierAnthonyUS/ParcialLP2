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

### Ejemplo 2: Análisis de Datos Cualitativos
```python
from core import AnalizadorCualitativo

# Datos de ejemplo: medios de transporte preferidos
transportes = ['auto', 'bus', 'bicicleta', 'bus', 'auto', 'metro', 
               'bus', 'bicicleta', 'auto', 'bus', 'metro', 'bus']

# Crear el analizador
analizador = AnalizadorCualitativo(transportes)

# Obtener la moda
print(f"Transporte más usado: {analizador.moda()}")

# Tabla de frecuencias
print("\nTabla de Frecuencias:")
tabla = analizador.tabla_frecuencias()
for categoria, valores in tabla.items():
    print(f"{categoria}: {valores['frecuencia_absoluta']} "
          f"({valores['frecuencia_porcentual']}%)")

# Medidas de diversidad
print(f"\nEntropía: {analizador.entropia():.4f}")
print(f"Índice de Simpson: {analizador.indice_diversidad_simpson():.4f}")
```

**Salida esperada:**
```
Transporte más usado: bus

Tabla de Frecuencias:
bus: 5 (41.67%)
auto: 3 (25.0%)
bicicleta: 2 (16.67%)
metro: 2 (16.67%)

Entropía: 1.8828
Índice de Simpson: 0.7361
```

### Ejemplo 3: Análisis Bivariado (Correlación y Regresión)
```python
from core import AnalizadorBivariado

# Datos de ejemplo: horas de estudio vs calificación
horas_estudio = [2, 3, 4, 5, 6, 7, 8, 9, 10]
calificaciones = [55, 60, 68, 72, 78, 83, 88, 92, 95]

# Crear el analizador bivariado
analizador = AnalizadorBivariado(horas_estudio, calificaciones)

# Correlación
correlacion = analizador.correlacion_pearson()
print(f"Correlación de Pearson: {correlacion:.4f}")
print(f"Coeficiente de Determinación (R²): {analizador.coeficiente_determinacion():.4f}")

# Regresión lineal
regresion = analizador.regresion_lineal_simple()
print(f"\nEcuación de regresión: {regresion['ecuacion']}")
print(f"Intercepto: {regresion['intercepto']}")
print(f"Pendiente: {regresion['pendiente']}")

# Hacer una predicción
horas_nuevas = 12
prediccion = regresion['intercepto'] + regresion['pendiente'] * horas_nuevas
print(f"\nPredicción para {horas_nuevas} horas: {prediccion:.2f} puntos")
```

**Salida esperada:**
```
Correlación de Pearson: 0.9954
Coeficiente de Determinación (R²): 0.9908

Ecuación de regresión: Y = 41.6667 + 5.3333*X
Intercepto: 41.6667
Pendiente: 5.3333

Predicción para 12 horas: 105.67 puntos
```

## 🎓 Conceptos de POO Implementados

### 1. **Abstracción**
```python
class AnalizadorBase(ABC):
    @abstractmethod
    def resumen(self) -> Dict:
        pass
```
- Clase abstracta `AnalizadorBase` define la interfaz común
- Método abstracto `resumen()` debe ser implementado por todas las subclases

### 2. **Encapsulamiento**
```python
self._datos = datos        # Atributo privado
self._n = len(datos)       # Atributo privado
self._datos_ordenados = None  # Caché privado
```
- Atributos privados con prefijo `_`
- Acceso controlado mediante propiedades `@property`
- Métodos privados para operaciones internas

### 3. **Herencia**
```python
class AnalizadorCuantitativo(AnalizadorBase):
    def __init__(self, datos):
        super().__init__(datos)  # Llama al constructor padre
```
- Todas las clases heredan de `AnalizadorBase`
- Reutilizan funcionalidad común (validación, almacenamiento)

### 4. **Polimorfismo**
```python
# Cada clase implementa su propia versión de resumen()
analizador_cuant.resumen()  # Retorna estadísticas cuantitativas
analizador_cual.resumen()   # Retorna estadísticas cualitativas
```

## 🙏 Agradecimientos

- Profesora Ana Vargar por la guía y enseñanza de POO
- Compañeros de clase por el feedback
- Comunidad de Python por la documentación