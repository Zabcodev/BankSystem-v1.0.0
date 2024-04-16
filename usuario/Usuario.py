from usuario.Persona import Persona
from cuenta.Cuenta import Cuenta

class Usuario(Persona):

    ''' CLASE USUARIO '''


    def __init__(self, 
                 nombre: str, apellido: str, cedula: int, username: str, password: str, cuentas: list[Cuenta] = []):
        
        ''' CONSTRUCTOR DE CLASE '''

        super().__init__(nombre, apellido, cedula)
        self.__username = username
        self.__password = password
        self.__cuentas = cuentas


    def set_username(self, username: str):

        ''' METODO SETTER PARA USERNAME '''

        self.__username = username


    def get_username(self):

        ''' METODO GETTER PARA USERNAME '''

        return self.__username


    def set_password(self, password: str):

        ''' METODO SETTER PARA CONTRASEÑA '''

        self.__password = password


    def get_password(self):

        ''' METODO GETTER PARA CONTRASEÑA '''

        return self.__password
    

    def set_cuentas(self, cuenta: Cuenta):

        ''' METODO SETTER PARA AÑADIR CUENTAS '''

        self.__cuentas.append(cuenta)


    def get_cuentas(self):

        ''' METODO GETTER PARA CUENTAS '''

        return self.__cuentas
    
