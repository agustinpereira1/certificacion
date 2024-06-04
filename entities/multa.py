class Multa:
    def __init__(self, concepto, importe, esta_paga):
        self._concepto = concepto
        self._importe = importe
        self._esta_paga = esta_paga

    @property
    def concepto(self):
        return self._concepto

    @property
    def importe(self):
        return self._importe
    
    @property
    def esta_paga(self):
        return self._esta_paga

    @esta_paga.setter
    def esta_paga(self, nuevo_valor):
        self._esta_paga = nuevo_valor
