class Vehiculo:
    def __init__(self, matricula, padron, dueno):
        self._matricula = matricula
        self._padron = padron
        self._dueno = dueno
        self._lista_multas = []
    
    @property
    def matricula(self):
        return self._matricula
    
    @property
    def padron(self):
        return self._padron
    
    @property
    def dueno(self):
        return self._dueno
    
    @property
    def lista_multas(self):
        return self._lista_multas
    
    @dueno.setter
    def dueno(self, nuevo_dueno):
        self._dueno = nuevo_dueno
    
    def agregar_multa(self, nueva_multa):
        self._lista_multas.append(nueva_multa)
    
    def multa_sin_pagar(self):
        for multa in self._lista_multas:
            if multa.esta_paga == False:
                return True
        
        return False
