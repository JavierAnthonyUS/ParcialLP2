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