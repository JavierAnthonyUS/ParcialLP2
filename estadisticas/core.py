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