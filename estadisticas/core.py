"""
EstadisticaPy - Librería de Análisis Estadístico
Autor: 
Fiorella Fuentes
Javier Anthony Uraco
Sebastian Fernandez
Versión: 1.0

Una librería orientada a objetos para realizar análisis estadístico
descriptivo de datos cuantitativos y cualitativos.
"""
from abc import ABC, abstractmethod
from typing import List, Union, Dict, Tuple
import math
from collections import Counter


class AnalizadorBase(ABC):
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
    
    def __repr__(self):
        return f"{self.__class__.__name__}(n={self._n})"
    
class AnalizadorCuantitativo(AnalizadorBase):
    """Analizador para datos numéricos continuos o discretos."""

    def __init__(self, datos: List[Union[int, float]]):
        # Validar que todos los datos sean numéricos
        try:
            self._validar_datos_numericos(datos)
        except (ValueError, TypeError) as e:
            raise TypeError("Todos los datos deben ser numéricos") from e
        
        super().__init__(datos)
        self._datos_ordenados = None

    def _validar_datos_numericos(self, datos):
        """Valida que todos los elementos sean numéricos."""
        return [float(x) for x in datos]
    
    def _ordenar_datos(self):
        """Ordena los datos si aún no están ordenados."""
        if self._datos_ordenados is None:
            self._datos_ordenados = sorted(self._datos)
        return self._datos_ordenados
    
    def media(self) -> float:
        """Calcula la media aritmética (promedio)."""
        return sum(self._datos) / self._n
    
    def mediana(self) -> float:
        """Calcula la mediana (percentil 50)."""
        datos_ord = self._ordenar_datos()
        mitad = self._n // 2
        
        if self._n % 2 == 0:
            return (datos_ord[mitad - 1] + datos_ord[mitad]) / 2
        else:
            return datos_ord[mitad]
        
    def moda(self) -> Union[List[float], str]:
        """Calcula la moda (valor más frecuente)."""
        frecuencias = Counter(self._datos)
        max_freq = max(frecuencias.values())
        
        modas = [valor for valor, freq in frecuencias.items() if freq == max_freq]
        
        if len(modas) == self._n:
            return "No hay moda (todos los valores son únicos)"
        elif len(modas) == 1:
            return modas[0]
        else:
            return modas  # Distribución multimodal
        
    def varianza(self, muestral: bool = True) -> float:
        """
        Calcula la varianza
        
        Args:
            muestral: Si True, usa n-1 (varianza muestral), si False usa n (poblacional)
        """
        media = self.media()
        suma_cuadrados = sum((x - media) ** 2 for x in self._datos)
        divisor = self._n - 1 if muestral else self._n
        return suma_cuadrados / divisor
    
    def desviacion_estandar(self, muestral: bool = True) -> float:
        """Calcula la desviación estándar"""
        return math.sqrt(self.varianza(muestral))
    
    def coeficiente_variacion(self) -> float:
        """
        Calcula el coeficiente de variación (CV)
        Mide la dispersión relativa de los datos
        """
        media = self.media()
        if media == 0:
            raise ValueError("No se puede calcular CV cuando la media es 0")
        return (self.desviacion_estandar() / abs(media)) * 100
    
    def percentil(self, p: float) -> float:
        """
        Calcula el percentil p-ésimo usando interpolación lineal
        
        Args:
            p: Percentil a calcular (0-100)
        """
        if not 0 <= p <= 100:
            raise ValueError("El percentil debe estar entre 0 y 100")
        
        datos_ord = self._ordenar_datos()
        
        if p == 0:
            return datos_ord[0]
        if p == 100:
            return datos_ord[-1]
        
        # Método de interpolación lineal
        indice = (p / 100) * (self._n - 1)
        indice_inferior = int(indice)
        indice_superior = indice_inferior + 1
        fraccion = indice - indice_inferior
        
        return datos_ord[indice_inferior] + fraccion * (
            datos_ord[indice_superior] - datos_ord[indice_inferior])
    
    def cuartiles(self) -> Tuple[float, float, float]:
        """Retorna los cuartiles Q1, Q2, Q3"""
        return (self.percentil(25), self.percentil(50), self.percentil(75))
    
    def rango_intercuartilico(self) -> float:
        """Calcula el rango intercuartílico (IQR)"""
        q1, _, q3 = self.cuartiles()
        return q3 - q1
    def asimetria(self) -> float:
        """
        Calcula el coeficiente de asimetría de Fisher (sesgo)
        > 0: asimétrica a la derecha
        < 0: asimétrica a la izquierda
        ≈ 0: simétrica
        """
        media = self.media()
        desv_std = self.desviacion_estandar(muestral=False)
        
        if desv_std == 0:
            return 0.0
        
        suma_cubos = sum(((x - media) / desv_std) ** 3 for x in self._datos)
        return suma_cubos / self._n
    def curtosis(self) -> float:
        """
        Calcula el coeficiente de curtosis (exceso de curtosis)
        > 0: leptocúrtica (colas pesadas)
        < 0: platicúrtica (colas ligeras)
        ≈ 0: mesocúrtica (similar a normal)
        """
        media = self.media()
        desv_std = self.desviacion_estandar(muestral=False)
        
        if desv_std == 0:
            return 0.0
        
        suma_cuartos = sum(((x - media) / desv_std) ** 4 for x in self._datos)
        return (suma_cuartos / self._n) - 3
    def minimo(self) -> float:
        """Retorna el valor mínimo"""
        return min(self._datos)
    def maximo(self) -> float:
        """Retorna el valor máximo"""
        return max(self._datos)
    def rango(self) -> float:
        """Calcula el rango (máximo - mínimo)"""
        return self.maximo() - self.minimo()
    def resumen(self) -> Dict:
        """Genera un resumen estadístico completo"""
        q1, q2, q3 = self.cuartiles()
        
        return {
            'n': self._n,
            'media': round(self.media(), 4),
            'mediana': round(self.mediana(), 4),
            'moda': self.moda(),
            'desviacion_estandar': round(self.desviacion_estandar(), 4),
            'varianza': round(self.varianza(), 4),
            'coeficiente_variacion': round(self.coeficiente_variacion(), 2),
            'minimo': round(self.minimo(), 4),
            'maximo': round(self.maximo(), 4),
            'rango': round(self.rango(), 4),
            'Q1': round(q1, 4),
            'Q2': round(q2, 4),
            'Q3': round(q3, 4),
            'IQR': round(self.rango_intercuartilico(), 4),
            'asimetria': round(self.asimetria(), 4),
            'curtosis': round(self.curtosis(), 4)}
    def resumen_cinco_numeros(self) -> Dict:
        """Retorna el resumen de cinco números de Tukey"""
        q1, q2, q3 = self.cuartiles()
        return {
            'minimo': self.minimo(),
            'Q1': q1,
            'mediana': q2,
            'Q3': q3,
            'maximo': self.maximo()}

class AnalizadorBivariado(AnalizadorBase):
    """Analizador para relaciones entre dos variables cuantitativas"""
    
    def __init__(self, datos_x: List[Union[int, float]], 
                 datos_y: List[Union[int, float]]):
        if len(datos_x) != len(datos_y):
            raise ValueError("Las dos variables deben tener el mismo tamaño")
         
        super().__init__(list(zip(datos_x, datos_y)))
        self._x = datos_x
        self._y = datos_y

    def covarianza(self, muestral: bool = True) -> float:
        """Calcula la covarianza entre X e Y"""
        media_x = sum(self._x) / self._n
        media_y = sum(self._y) / self._n
        
        suma_productos = sum((x - media_x) * (y - media_y) 
                            for x, y in zip(self._x, self._y))
        
        divisor = self._n - 1 if muestral else self._n
        return suma_productos / divisor  
    
    def correlacion_pearson(self) -> float:
        """
        Calcula el coeficiente de correlación de Pearson
        Mide la relación lineal entre X e Y (-1 a 1)
        """
        # Calcular desviaciones estándar
        analizador_x = AnalizadorCuantitativo(self._x)
        analizador_y = AnalizadorCuantitativo(self._y)
        
        desv_x = analizador_x.desviacion_estandar()
        desv_y = analizador_y.desviacion_estandar()
        
        if desv_x == 0 or desv_y == 0:
            raise ValueError("No se puede calcular correlación con d.s 0")
        
        return self.covarianza() / (desv_x * desv_y)   
      
    def coeficiente_determinacion(self) -> float:
        return self.correlacion_pearson() ** 2          

    def regresion_lineal_simple(self) -> Dict[str, float]:
        """
        Calcula los parámetros de la regresión lineal simple
        Y = β0 + β1*X
        """
        media_x = sum(self._x) / self._n
        media_y = sum(self._y) / self._n
        
        # Calcular la pendiente (β1)
        numerador = sum((x - media_x) * (y - media_y) 
                       for x, y in zip(self._x, self._y))
        denominador = sum((x - media_x) ** 2 for x in self._x)    

        if denominador == 0:
            raise ValueError("No se puede calcular regresión: varianza de X es 0")
        
        beta1 = numerador / denominador
        beta0 = media_y - beta1 * media_x
        
        return {
            'intercepto': round(beta0, 4),
            'pendiente': round(beta1, 4),
            'ecuacion': f"Y = {beta0:.4f} + {beta1:.4f}*X"
        }
    
    def resumen(self) -> Dict:
        """Genera un resumen del análisis bivariado"""
        try:
            regresion = self.regresion_lineal_simple()
            correlacion = self.correlacion_pearson()
            r2 = self.coeficiente_determinacion()
        except ValueError as e:
            return {'error': str(e)}
        
        return {
            'n': self._n,
            'covarianza': round(self.covarianza(), 4),
            'correlacion_pearson': round(correlacion, 4),
            'r_cuadrado': round(r2, 4),
            'regresion_lineal': regresion
        }
    
# Función auxiliar para determinar el tipo de datos automáticamente
def analizar(datos: List, tipo: str = 'auto'):
    """
    Función helper para crear el analizador apropiado
    
    Args:
        datos: Lista de datos a analizar
        tipo: 'cuantitativo', 'cualitativo' o 'auto' (detecta automáticamente)
    """
    if tipo == 'auto':
        # Intentar detectar el tipo de datos
        try:
            [float(x) for x in datos]
            tipo = 'cuantitativo'
        except (ValueError, TypeError):
            tipo = 'cualitativo'
    
    if tipo == 'cuantitativo':
        return AnalizadorCuantitativo(datos)
    elif tipo == 'cualitativo':
        return AnalizadorCualitativo(datos)
    else:
        raise ValueError("Tipo debe ser 'cuantitativo', 'cualitativo' o 'auto'")


# Ejemplo de uso
if __name__ == "__main__":
    print("=" * 60)
    print("EJEMPLO 1: ANÁLISIS DE DATOS CUANTITATIVOS")
    print("=" * 60)
    
    # Datos de ejemplo: edades de estudiantes
    edades = [22, 23, 21, 25, 24, 23, 22, 26, 24, 23, 21, 27, 25, 24, 23]
    
    analizador_cuant = AnalizadorCuantitativo(edades)
    
    print(f"\nDatos: {edades}")
    print(f"\nResumen estadístico:")
    print("-" * 60)
    
    resumen = analizador_cuant.resumen()
    for clave, valor in resumen.items():
        print(f"{clave:.<30} {valor}")
    
    print("\n" + "=" * 60)
    print("EJEMPLO 2: ANÁLISIS DE DATOS CUALITATIVOS")
    print("=" * 60)



    # Datos de ejemplo: preferencias de color
    colores = ['rojo', 'azul', 'verde', 'azul', 'rojo', 'azul', 
               'amarillo', 'verde', 'azul', 'rojo', 'azul', 'verde']
    
    analizador_cual = AnalizadorCualitativo(colores)
    
    print(f"\nDatos: {colores}")
    print(f"\nTabla de frecuencias:")
    print("-" * 60)
    
    tabla = analizador_cual.tabla_frecuencias()
    print(f"{'Categoría':<15} {'Frec.Abs':<10} {'Frec.Rel':<10} {'Frec.%':<10}")
    print("-" * 60)
    for cat, valores in tabla.items():
        print(f"{cat:<15} {valores['frecuencia_absoluta']:<10} "
              f"{valores['frecuencia_relativa']:<10.4f} "
              f"{valores['frecuencia_porcentual']:<10.2f}")
    
    print("\n" + "=" * 60)
    print("EJEMPLO 3: ANÁLISIS BIVARIADO (CORRELACIÓN Y REGRESIÓN)")
    print("=" * 60)


    # Datos de ejemplo: horas de estudio vs calificación
    horas_estudio = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    calificaciones = [55, 60, 68, 72, 78, 83, 88, 92, 95]
    
    analizador_biv = AnalizadorBivariado(horas_estudio, calificaciones)
    
    print(f"\nHoras de estudio: {horas_estudio}")
    print(f"Calificaciones: {calificaciones}")
    print(f"\nAnálisis de relación:")
    print("-" * 60)
    
    resumen_biv = analizador_biv.resumen()
    for clave, valor in resumen_biv.items():
        if isinstance(valor, dict):
            print(f"\n{clave}:")
            for k, v in valor.items():
                print(f"  {k}: {v}")
        else:
            print(f"{clave}: {valor}")