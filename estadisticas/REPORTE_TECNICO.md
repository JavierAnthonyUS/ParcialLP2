# 📑 REPORTE TÉCNICO
## CorePy: Librería de Análisis Estadístico con POO

---

### INFORMACIÓN DEL PROYECTO

**Institución:** Universidad Nacional Agraria la Molina  
**Curso:** Lenguaje de Programación 2  
**Profesor:** Ana Vargas 

**Integrantes:**
1. Javier Anthony Uraco Silva 
2. Fiorella Fuentes
3. Sebastian Fernandez

---

## 📋 TABLA DE CONTENIDOS

1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Marco Teórico](#3-marco-teórico)
4. [Diseño y Arquitectura](#4-diseño-y-arquitectura)
5. [Implementación](#5-implementación)
---

## 1. INTRODUCCIÓN

### 1.1 Contexto

El análisis estadístico es fundamental en diversos campos como la ciencia de datos, investigación, negocios y educación. Sin embargo, las herramientas existentes como NumPy o pandas pueden ser complejas para usuarios principiantes o para fines educativos.

### 1.2 Problemática

Se requiere una herramienta que:
- Sea fácil de entender y usar
- Esté implementada con principios de POO claros
- No dependa de librerías externas complejas
- Permita realizar análisis estadísticos básicos y avanzados
- Sirva como material educativo para aprender POO

### 1.3 Propuesta de Solución

**CorePy** es una librería de análisis estadístico desarrollada completamente en Python, utilizando Programación Orientada a Objetos como paradigma principal. La librería implementa estadísticas descriptivas para datos cuantitativos y cualitativos, además de análisis de relaciones bivariadas.

---

## 2. OBJETIVOS

### 2.1 Objetivo General

Desarrollar una librería de análisis estadístico en Python que implemente los principios de Programación Orientada a Objetos para realizar cálculos de estadística descriptiva de manera eficiente y educativa.

### 2.2 Objetivos Específicos

1. **Diseñar** una arquitectura de clases que demuestre los conceptos de POO (abstracción, encapsulamiento, herencia, polimorfismo)

2. **Implementar** métodos estadísticos para datos cuantitativos:
   - Medidas de tendencia central (media, mediana, moda)
   - Medidas de dispersión (varianza, desviación estándar, CV, rango, IQR)
   - Medidas de posición (percentiles, cuartiles)
   - Medidas de forma (asimetría, curtosis)

3. **Implementar** métodos estadísticos para datos cualitativos:
   - Moda(s)
   - Tablas de frecuencia (absoluta, relativa, porcentual, acumulada)
   - Medidas de diversidad (entropía, índice de Simpson)

4. **Implementar** análisis bivariado:
   - Covarianza y correlación
   - Regresión lineal simple
   - Coeficiente de determinación

5. **Validar** el funcionamiento mediante pruebas automatizadas y casos de uso reales

---

## 3. MARCO TEÓRICO

### 3.1 Programación Orientada a Objetos

La POO es un paradigma de programación que organiza el código en objetos que contienen datos (atributos) y comportamientos (métodos). Los pilares fundamentales son:

#### **Abstracción**
Permite definir interfaces comunes sin especificar la implementación. En Python se implementa mediante clases abstractas y el módulo `abc`.

#### **Encapsulamiento**
Oculta los detalles internos de implementación y expone solo lo necesario. En Python se usa el prefijo `_` para indicar atributos/métodos privados.

#### **Herencia**
Permite que una clase hija herede atributos y métodos de una clase padre, promoviendo la reutilización de código.

#### **Polimorfismo**
Permite que diferentes clases implementen el mismo método de diferentes maneras.

### 3.2 Estadística Descriptiva

#### **Medidas de Tendencia Central**
- **Media (μ o x̄):** Promedio aritmético de los datos
  ```
  x̄ = (Σxi) / n
  ```

- **Mediana:** Valor central cuando los datos están ordenados
  ```
  Mediana = {
    x[(n+1)/2]           si n es impar
    (x[n/2] + x[n/2+1])/2  si n es par
  }
  ```

- **Moda:** Valor(es) más frecuente(s) en el conjunto de datos

#### **Medidas de Dispersión**
- **Varianza (σ² o s²):** Promedio de las desviaciones cuadráticas
  ```
  s² = Σ(xi - x̄)² / (n-1)  (muestral)
  σ² = Σ(xi - μ)² / n       (poblacional)
  ```

- **Desviación Estándar (σ o s):** Raíz cuadrada de la varianza
  ```
  s = √[Σ(xi - x̄)² / (n-1)]
  ```

- **Coeficiente de Variación (CV):** Dispersión relativa
  ```
  CV = (s / x̄) × 100%
  ```

- **Rango Intercuartílico (IQR):** Diferencia entre Q3 y Q1
  ```
  IQR = Q3 - Q1
  ```

#### **Medidas de Posición**
- **Percentil k:** Valor que deja k% de los datos por debajo
- **Cuartiles:** Dividen los datos en 4 partes iguales (Q1, Q2, Q3)

#### **Medidas de Forma**
- **Asimetría (Skewness):** Mide la simetría de la distribución (Fisher)
```
  Skewness = [n / ((n-1)(n-2))] × Σ[(xi - x̄) / s]³
  Donde s es la desviación estándar muestral
```

- **Curtosis (Exceso):** Mide el "apuntamiento" de la distribución (Fisher)
```
  Kurtosis = [n(n+1) / ((n-1)(n-2)(n-3))] × Σ[(xi - x̄) / s]⁴ - [3(n-1)² / ((n-2)(n-3))]
  Donde s es la desviación estándar muestral
```

#### **Análisis Bivariado**
- **Covarianza:** Medida de variación conjunta
  ```
  Cov(X,Y) = Σ(xi - x̄)(yi - ȳ) / (n-1)
  ```

- **Correlación de Pearson (r):** Covarianza estandarizada
  ```
  r = Cov(X,Y) / (sx × sy)
  ```
  Valores: -1 (correlación negativa perfecta) a +1 (correlación positiva perfecta)

- **Regresión Lineal:** Y = β₀ + β₁X
  ```
  β₁ = Σ(xi - x̄)(yi - ȳ) / Σ(xi - x̄)²
  β₀ = ȳ - β₁x̄
  ```

#### **Medidas para Datos Cualitativos**
- **Entropía de Shannon:** Mide la incertidumbre
  ```
  H = -Σ(pi × log₂(pi))
  ```

- **Índice de Simpson:** Mide la diversidad
  ```
  D = 1 - Σ(pi²)
  ```

---

## 4. DISEÑO Y ARQUITECTURA

### 4.1 Diagrama de Clases (UML)

```
┌──────────────────────────────────────┐
│     <<abstract>>                      │
│     AnalizadorBase                    │
├──────────────────────────────────────┤
│ - _datos: List                        │
│ - _n: int                             │
├──────────────────────────────────────┤
│ + __init__(datos: List)               │
│ + datos: List {property}              │
│ + n: int {property}                   │
│ + resumen(): Dict {abstract}          │
└──────────────────────────────────────┘
           ▲
           │
           │ (herencia)
           │
    ┌──────┴──────┬──────────────────┬──────────────────┐
    │             │                  │                  │
┌───┴─────────────┴───┐  ┌──────────┴──────────┐  ┌───┴──────────────────┐
│ AnalizadorCuantitativo│  │ AnalizadorCualitativo│  │ AnalizadorBivariado  │
├──────────────────────┤  ├─────────────────────┤  ├──────────────────────┤
│ - _datos_ordenados    │  │ - _frecuencias      │  │ - _x: List           │
├──────────────────────┤  ├─────────────────────┤  │ - _y: List           │
│ + media(): float      │  │ + moda()            │  ├──────────────────────┤
│ + mediana(): float    │  │ + frecuencias_      │  │ + covarianza()       │
│ + desviacion_estandar │  │   absolutas()       │  │ + correlacion_       │
│ + percentil(p)        │  │ + frecuencias_      │  │   pearson()          │
│ + cuartiles()         │  │   relativas()       │  │ + regresion_lineal_  │
│ + asimetria()         │  │ + tabla_frecuencias │  │   simple()           │
│ + curtosis()          │  │ + entropia()        │  │ + coeficiente_       │
│ + resumen()           │  │ + indice_simpson()  │  │   determinacion()    │
└──────────────────────┘  │ + resumen()         │  │ + resumen()          │
                           └─────────────────────┘  └──────────────────────┘
```

### 4.2 Patrones de Diseño Utilizados

#### **Template Method Pattern**
La clase base `AnalizadorBase` define el esqueleto del método `resumen()`, y cada subclase proporciona su implementación específica.

#### **Strategy Pattern**
Diferentes estrategias de cálculo según el tipo de datos (cuantitativo vs cualitativo).

#### **Factory Pattern** (función `analizar()`)
Detecta automáticamente el tipo de datos y crea el analizador apropiado.

### 4.3 Estructura del Proyecto

```
ParcialLP2/
└── estadisticas/
    ├── __init__.py
    │   └── Exporta las clases principales
    │
    ├── core.py
    │   ├── AnalizadorBase (clase abstracta)
    │   ├── AnalizadorCuantitativo
    │   ├── AnalizadorCualitativo
    │   ├── AnalizadorBivariado
    │   └── analizar() (función helper)
    │
    ├── test_core.py
    │   └── Suite completa de pruebas
    │
    └── README.md
        └── Documentación del usuario
```

---

## 5. IMPLEMENTACIÓN

### 5.1 Clase Base: AnalizadorBase

```python
from abc import ABC, abstractmethod
"""Clase abstracta base para todos los analizadores estadísticos."""
    
    def __init__(self, datos: List):
        if not datos:
            raise ValueError("El conjunto de datos no puede estar vacío")
        self._datos = datos
        self._n = len(datos)
    
    @property
    def datos(self):
        """Retorna los datos almacenados."""
        return self._datos
    
    @property
    def n(self):
        """Retorna el tamaño de la muestra."""
        return self._n
    
    @abstractmethod
    def resumen(self) -> Dict:
        """Método abstracto para generar resumen estadístico."""
        pass
class AnalizadorBase(ABC):

**Características implementadas:**
- Constructor que valida datos no vacíos
- Atributos privados `_datos` y `_n` (encapsulamiento)
- Propiedades de solo lectura usando `@property`
- Método abstracto `resumen()` que obliga a las subclases a implementarlo

### 5.2 Clase AnalizadorCuantitativo

Esta clase hereda de `AnalizadorBase` e implementa todos los métodos estadísticos para datos numéricos.
```python
class AnalizadorCuantitativo(AnalizadorBase):
    """Analizador para datos numéricos continuos o discretos."""
    
    def __init__(self, datos: List[Union[int, float]]):
        # Validación de datos numéricos
        try:
            self._validar_datos_numericos(datos)
        except (ValueError, TypeError) as e:
            raise TypeError("Todos los datos deben ser numéricos") from e
        
        super().__init__(datos)
        self._datos_ordenados = None  # Caché para optimización
```

**Métodos principales implementados:**
- Media, mediana, moda
- Varianza y desviación estándar (muestral y poblacional)
- Coeficiente de variación
- Percentiles y cuartiles
- Asimetría y curtosis (fórmulas de Fisher)
- Resumen estadístico completo

### 5.3 Clase AnalizadorCualitativo

Especializada en el análisis de datos categóricos.
```python
class AnalizadorCualitativo(AnalizadorBase):
    """Analizador para datos categóricos o nominales"""
    
    def __init__(self, datos: List):
        super().__init__(datos)
        self._frecuencias = None  # Caché
```

**Funcionalidades:**
- Frecuencias absolutas, relativas y porcentuales
- Tabla de frecuencias completa con acumuladas
- Moda para datos categóricos
- Entropía de Shannon
- Índice de diversidad de Simpson

### 5.4 Clase AnalizadorBivariado

Permite analizar la relación entre dos variables cuantitativas.
```python
class AnalizadorBivariado(AnalizadorBase):
    """Analizador para relaciones entre dos variables cuantitativas"""
    
    def __init__(self, datos_x: List[Union[int, float]], 
                 datos_y: List[Union[int, float]]):
        if len(datos_x) != len(datos_y):
            raise ValueError("Las dos variables deben tener el mismo tamaño")
        
        super().__init__(list(zip(datos_x, datos_y)))
        self._x = datos_x
        self._y = datos_y
```

**Capacidades:**
- Covarianza
- Correlación de Pearson
- Coeficiente de determinación (R²)
- Regresión lineal simple

---

## 6. PRUEBAS Y VALIDACIÓN

Se implementó un conjunto completo de pruebas en `test_core.py` que verifica:

1. ✅ Funcionamiento correcto de AnalizadorCuantitativo
2. ✅ Funcionamiento correcto de AnalizadorCualitativo
3. ✅ Funcionamiento correcto de AnalizadorBivariado
4. ✅ Función helper con detección automática
5. ✅ Manejo de casos borde y validaciones

**Resultados:** Todos los tests pasan exitosamente, validando la correcta implementación de la librería.

---

## 7. CONCLUSIONES

CorePy es una librería educativa y funcional que:

- ✅ Implementa correctamente los 4 pilares de POO
- ✅ Proporciona análisis estadístico completo
- ✅ Está bien documentada y probada
- ✅ No depende de librerías externas
- ✅ Es fácil de usar y entender

La librería cumple con todos los objetivos propuestos y sirve tanto para análisis real como para aprendizaje de POO en Python.

---
