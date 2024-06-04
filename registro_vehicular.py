from entities.exceso_velocidad import ExcesoVelocidad
from entities.multa import Multa
from entities.persona import Persona
from entities.vehiculo import Vehiculo
from exceptions.entidad_no_existe import EntidadNoExiste
from exceptions.entidad_ya_existe import EntidadYaExiste
from exceptions.informacion_invalida import InformacionInvalida


class RegistroVehicular:
    def __init__(self):
        self._lista_personas = []
        self._lista_vehiculos = []

    def buscar_persona(self, cedula):
        persona_encontrada = None
        for persona in self._lista_personas:
            if persona.cedula == cedula:
                persona_encontrada = persona
        
        return persona_encontrada

    def buscar_vehiculo(self, matricula):
        vehiculo_encontrado = None
        for vehiculo in self._lista_vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo_encontrado = vehiculo
        
        return vehiculo_encontrado
    
    def verificar_libreta_suspendida(self, persona):
        if persona.verificar_cantidad_multas_exceso_velocidad() >= 3:
            persona.libreta_suspendida = True
    
    def registrar_vehiculo(self, matricula, nro_padron, cedula_titular):
        if matricula == None or nro_padron == None or cedula_titular == None:
            raise InformacionInvalida("La informacion es inválida")
        
        vehiculo = self.buscar_vehiculo(matricula)
        if vehiculo != None:
            raise EntidadYaExiste("El vehiculo ya está registrado")

        persona = self.buscar_persona(cedula_titular)
        if persona == None:
            persona = Persona(cedula_titular, False)
            self._lista_personas.append(persona)
        if persona.libreta_suspendida == True:
            raise InformacionInvalida("La libreta está suspendida.")

        vehiculo = Vehiculo(matricula, nro_padron, persona)
        persona.agregar_vehiculo(vehiculo)
        self._lista_vehiculos.append(vehiculo)
    
    def registrar_multa_vehiculo(self, matricula, concepto, importe, es_exceso_velocidad, 
                                 velocidad_vehiculo = None, velocidad_limite = None):
        if matricula == None or concepto == None or importe == None or es_exceso_velocidad == None:
            raise InformacionInvalida("La información es inválida")

        if es_exceso_velocidad == True:
            if velocidad_vehiculo == None or velocidad_limite == None:
                raise InformacionInvalida("La información es inválida")
        
        vehiculo = self.buscar_vehiculo(matricula)
        if vehiculo == None:
            raise EntidadNoExiste("El vehiculo no existe")
        
        nueva_multa = None
        if es_exceso_velocidad == True:
            nueva_multa = ExcesoVelocidad(concepto, importe, False, velocidad_vehiculo, velocidad_limite)
        else:
            nueva_multa = Multa(concepto, importe, False)
        
        vehiculo.agregar_multa(nueva_multa)
        self.verificar_libreta_suspendida(vehiculo.dueno)
    

    def pagar_multa_vehiculo(self,matricula, concepto, importe):
        vehiculo = self.buscar_vehiculo(matricula)
        if vehiculo == None:
            raise EntidadNoExiste("Vehiculo no existe")
        
        multa_encontrada = None
        for multa in vehiculo.lista_multas:
            if multa.concepto == concepto and multa.importe == importe and multa.esta_paga == False:
                multa_encontrada = multa
                break
        
        if multa_encontrada == None:
            raise EntidadNoExiste("No se encontró la multa")
        
        multa_encontrada.esta_paga = True
    
    def traspaso_vehiculo(self, cedula_titular, matricula, cedula_nuevo_titular):
        vehiculo = self.buscar_vehiculo(matricula)
        nuevo_dueno = self.buscar_persona(cedula_nuevo_titular)
        dueno_anterior = self.buscar_persona(cedula_titular)

        if vehiculo == None or nuevo_dueno == None or dueno_anterior == None:
            raise EntidadNoExiste("Alguna de las entidades no existe")
        
        if vehiculo.multa_sin_pagar() == True:
            raise InformacionInvalida("Tiene multas sin pagar")
        
        if nuevo_dueno.libreta_suspendida == True:
            raise InformacionInvalida("Tiene la libreta suspendida")
        
        dueno_anterior.eliminar_vehiculo(matricula)
        vehiculo.dueno = nuevo_dueno
        nuevo_dueno.agregar_vehiculo(vehiculo)

if __name__ == "__main__":
    registro_vehicular = RegistroVehicular()
    registro_vehicular.registrar_vehiculo("ABC1234", 2, 12345678)
    try: 
        registro_vehicular.registrar_vehiculo("ABC1234", 2, 12345678)
    except Exception as e:
        print(e)
    registro_vehicular.registrar_vehiculo("CBA1234", 3, 12345678)
    registro_vehicular.registrar_vehiculo("CBY1234", 3, 12348278)

    registro_vehicular.registrar_multa_vehiculo("ABC1234", "Exceso de velocidad", 1234, True, 65, 60)
    registro_vehicular.registrar_multa_vehiculo("ABC1234", "Exceso de velocidad", 1234, True, 65, 60)
    registro_vehicular.registrar_multa_vehiculo("ABC1234", "Exceso de velocidad", 1234, True, 65, 60)
    registro_vehicular.registrar_multa_vehiculo("ABC1234", "Mal estacionamiento", 12334, False, None, None)
    registro_vehicular.pagar_multa_vehiculo("ABC1234", "Exceso de velocidad", 1234)

    registro_vehicular.traspaso_vehiculo(12345678, "CBA1234", 12348278)
    

        


        


