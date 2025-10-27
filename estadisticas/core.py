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