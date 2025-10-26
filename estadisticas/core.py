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