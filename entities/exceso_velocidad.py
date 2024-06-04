from entities.multa import Multa


class ExcesoVelocidad(Multa):
    def __init__(self, concepto, importe, esta_paga, velocidad, velocidad_limite):
        super().__init__(concepto, importe, esta_paga)
        self._velocidad = velocidad
        self._velocidad_limite = velocidad_limite

    
    @property
    def velocidad(self):
        return self._velocidad
    
    @property
    def velocidad_limite(self):
        return self._velocidad_limite
