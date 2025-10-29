"""
CorePy - Librería de Análisis Estadístico
Autor: 
Fiorella Fuentes
Javier Anthony Uraco
Sebastian Fernandez
Versión: 1.0
"""

from .core import (
    AnalizadorBase,
    AnalizadorCuantitativo,
    AnalizadorCualitativo,
    AnalizadorBivariado,
    analizar
)

__version__ = '1.0'
__author__ = 'Fiorella Fuentes, Javier Anthony Uraco, Sebastian Fernandez'

__all__ = [
    'AnalizadorBase',
    'AnalizadorCuantitativo',
    'AnalizadorCualitativo',
    'AnalizadorBivariado',
    'analizar'
]
