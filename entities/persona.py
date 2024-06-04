from entities.exceso_velocidad import ExcesoVelocidad


class Persona:
    def __init__(self, cedula, libreta_suspendida):
        self._cedula = cedula
        self._libreta_suspendida = libreta_suspendida
        self._lista_vehiculos = []
    
    @property
    def cedula(self):
        return self._cedula

    @property
    def libreta_suspendida(self):
        return self._libreta_suspendida
    
    @property
    def lista_vehiculos(self):
        return self._lista_vehiculos
    
    @libreta_suspendida.setter
    def libreta_suspendida(self, nuevo_valor):
        self._libreta_suspendida = nuevo_valor
    
    def agregar_vehiculo(self, nuevo_vehiculo):
        self._lista_vehiculos.append(nuevo_vehiculo)
    
    def verificar_cantidad_multas_exceso_velocidad(self):
        cantidad_multas = 0
        for vehiculo in self._lista_vehiculos:
            for multa in vehiculo.lista_multas:
                if isinstance(multa, ExcesoVelocidad):
                    cantidad_multas += 1
        
        return cantidad_multas

    def eliminar_vehiculo(self, matricula):
        nueva_lista = []
        for vehiculo in self._lista_vehiculos:
            if vehiculo.matricula != matricula:
                nueva_lista.append(vehiculo)
        
        self._lista_vehiculos = nueva_lista