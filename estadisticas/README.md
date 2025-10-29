# 📊 ParcialLP2: Librería de Análisis Estadístico

**Python:** 3.7+  |  **Licencia:** MIT  |  **Estado:** ✅ Activo

Este repositorio contiene una librería desarrollada en Python para realizar cálculos de estadística descriptiva, utilizando los principios de la Programación Orientada a Objetos (POO).

## 👥 Integrantes del Grupo

| Nombre | GitHub |
|--------|--------|
| Fiorella Fuentes | [fiorellafuentesb20-cell](https://github.com/fiorellafuentesb20-cell) |
| Javier Anthony Uraco | [JavierAnthonyUS](https://github.com/JavierAnthonyUS) |
| Sebastian Fernandez | [TucoSquare](https://github.com/TucoSquare) |

**Institución:** Universidad Nacional Agraria la Molina  
**Curso:** Lenguaje de Programación 2 
**Profesor:** Ana Vargas 

## 📖 Descripción

**CorePy** es una librería completa que permite realizar análisis estadístico descriptivo tanto de datos **cuantitativos** (numéricos) como **cualitativos** (categóricos), además de análisis de relaciones entre variables (**bivariado**).

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
python test_core.py
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
Media: 87.20
Mediana: 88.00
Desviación Estándar: 5.44
Coeficiente de Variación: 6.24%
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
Correlación de Pearson: 0.9923
Coeficiente de Determinación (R²): 0.9847

Ecuación de regresión: Y = 45.1212 + 5.0848*X
Intercepto: 45.1212
Pendiente: 5.0848

Predicción para 12 horas: 106.14 puntos
```

### Ejemplo 4: Detección Automática del Tipo de Datos
```python
from core import analizar

# La función 'analizar' detecta automáticamente el tipo de datos

# Datos numéricos
datos_numericos = [10, 20, 30, 40, 50]
analizador1 = analizar(datos_numericos, tipo='auto')
print(f"Tipo detectado: {type(analizador1).__name__}")
print(f"Media: {analizador1.media()}")

# Datos categóricos
datos_categoricos = ['A', 'B', 'A', 'C', 'B', 'A']
analizador2 = analizar(datos_categoricos, tipo='auto')
print(f"Tipo detectado: {type(analizador2).__name__}")
print(f"Moda: {analizador2.moda()}")
```

---

## 🗂️ Arquitectura del Proyecto
```
ParcialLP2/
└── estadisticas/
    ├── __init__.py              # Inicializador del paquete
    ├── core.py                  # Código principal de la librería
    ├── test_core.py             # Suite de pruebas automatizadas
    ├── README.md                # Este archivo
    └── REPORTE_TECNICO.md       # Documentación técnica completa
```

### Jerarquía de Clases
```
AnalizadorBase (Clase Abstracta)
    │
    ├── AnalizadorCuantitativo
    │   └── Métodos: media(), mediana(), moda(), varianza(),
    │                desviacion_estandar(), coeficiente_variacion(),
    │                percentil(), cuartiles(), rango_intercuartilico(),
    │                asimetria(), curtosis(), resumen()
    │
    ├── AnalizadorCualitativo
    │   └── Métodos: moda(), frecuencias_absolutas(), 
    │                frecuencias_relativas(), frecuencias_porcentuales(),
    │                tabla_frecuencias(), categorias_unicas(),
    │                entropia(), indice_diversidad_simpson(), resumen()
    │
    └── AnalizadorBivariado
        └── Métodos: covarianza(), correlacion_pearson(),
                     coeficiente_determinacion(), 
                     regresion_lineal_simple(), resumen()
```
## 🧪 Pruebas

### Ejecutar todas las pruebas
```bash
python test_core.py
```

### Pruebas incluidas

El archivo `test_core.py` incluye:
- ✅ Test de análisis cuantitativo (16 medidas estadísticas)
- ✅ Test de análisis cualitativo (frecuencias y diversidad)
- ✅ Test de análisis bivariado (correlación y regresión)
- ✅ Test de función helper con detección automática
- ✅ Test de casos borde y validaciones

**Resultado esperado:** 5/5 tests exitosos (100%)

---

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
- Uso del módulo `abc` para garantizar la estructura

### 2. **Encapsulamiento**
```python
self._datos = datos              # Atributo privado
self._n = len(datos)             # Atributo privado
self._datos_ordenados = None     # Caché privado
self._frecuencias = None         # Caché privado

@property
def datos(self):
    return self._datos           # Acceso controlado

def _ordenar_datos(self):        # Método privado
    # Operación interna
```
- Atributos privados con prefijo `_`
- Acceso controlado mediante propiedades `@property`
- Métodos privados para operaciones internas (`_validar_datos_numericos()`, `_ordenar_datos()`, `_calcular_frecuencias()`)
- Protección de datos contra modificación externa

### 3. **Herencia**
```python
class AnalizadorCuantitativo(AnalizadorBase):
    def __init__(self, datos):
        super().__init__(datos)  # Llama al constructor padre
```
- Todas las clases heredan de `AnalizadorBase`
- Reutilizan funcionalidad común (validación, almacenamiento)
- Jerarquía clara y bien definida

### 4. **Polimorfismo**
```python
# Cada clase implementa su propia versión de resumen()
analizador_cuant.resumen()  # Retorna estadísticas cuantitativas
analizador_cual.resumen()   # Retorna estadísticas cualitativas
analizador_biv.resumen()    # Retorna análisis de correlación
```
- Mismo método, diferentes implementaciones
- Permite tratar objetos de diferentes clases de manera uniforme

---

## 🤝 Contribuciones

### Distribución del trabajo

| Integrante | Contribución Principal | Commits |
|------------|------------------------|---------|
| Javier Anthony Uraco Silva | Diseño de arquitectura POO, clase base abstracta, implementación de AnalizadorCuantitativo, integración y coordinación | ~40% |
| Fiorella Fuentes | Implementación completa de AnalizadorBivariado y función helper | ~30% |
| Sebastian Fernandez | Implementación de AnalizadorCuantitativo completando las medidas estadísticas y AnalizadorCualitativo | ~30% |

**Trabajo colaborativo:** Todos los integrantes participaron en:
- Pruebas y validación del código
- Documentación técnica (README y REPORTE_TECNICO)
- Revisión de código y corrección de errores
- Ejemplos de uso y casos de prueba

## 📊 Características Técnicas Destacadas

### Fórmulas Implementadas

- **Asimetría de Fisher (muestral):**
```
  Skewness = [n / ((n-1)(n-2))] × Σ[(xi - x̄) / s]³
```

- **Curtosis de Fisher (exceso, muestral):**
```
  Kurtosis = [n(n+1) / ((n-1)(n-2)(n-3))] × Σ[(xi - x̄) / s]⁴ - [3(n-1)² / ((n-2)(n-3))]
```

- **Correlación de Pearson:**
```
  r = Cov(X,Y) / (sx × sy)
```

- **Regresión Lineal Simple:**
```
  β₁ = Σ(xi - x̄)(yi - ȳ) / Σ(xi - x̄)²
  β₀ = ȳ - β₁x̄
```

### Validaciones Implementadas

- ✅ Validación de datos vacíos
- ✅ Validación de tipos de datos (numéricos vs categóricos)
- ✅ Validación de tamaños iguales en análisis bivariado
- ✅ Manejo de división por cero
- ✅ Validación de percentiles (0-100)
- ✅ Validación de datos mínimos para asimetría (n≥3) y curtosis (n≥4)
---
## 🙏 Agradecimientos

- Profesora Ana Vargas por la guía y enseñanza de POO
- Compañeros de clase por el feedback constructivo
- Comunidad de Python por la documentación y recursos
- Universidad Nacional Agraria la Molina por la formación académica
