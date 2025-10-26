"""
Módulo principal de la librería de análisis estadístico.

Este módulo contiene las clases base y las implementaciones para
realizar análisis estadísticos de diferentes tipos de datos.
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
        """Calcula la desviación estándar."""
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
    
