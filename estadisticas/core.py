class AnalizadorBivariado(AnalizadorBase):
    """Analizador para relaciones entre dos variables cuantitativas"""
    
    def __init__(self, datos_x: List[Union[int, float]], 
                 datos_y: List[Union[int, float]]):
        if len(datos_x) != len(datos_y):
            raise ValueError("Las dos variables deben tener el mismo tamaño")
         
        super().__init__(list(zip(datos_x, datos_y)))
        self._x = datos_x
        self._y = datos_y
        