class Persona:

    ''' CLASE PERSONA '''

    def __init__(self, nombre: str, apellido: str, cedula: int):
        ''' CONSTRUCTOR DE CLASE '''
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula

    def set_nombre(self, nombre: str):
        ''' METODO SETTER PARA NOMBRE '''
        self.__nombre = nombre

    def get_nombre(self):
        ''' METODO GETTER PARA NOMBRE '''
        return self.__nombre
    
    def set_apellido(self, apellido: str):
        ''' METODO SETTER PARA APELLIDO '''
        self.__apellido = apellido

    def get_apellido(self):
        ''' METODO GETTER PARA APELLIDO '''
        return self.__apellido
    
    def set_cedula(self, cedula: int):
        ''' METODO SETTER PARA CEDULA '''
        self.__cedula = cedula

    def get_cedula(self):
        ''' METODO GETTER PARA CEDULA '''
        return self.__cedula