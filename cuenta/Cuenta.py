class Cuenta:

    ''' CLASE CUENTA '''

    def __init__(self, numero_cuenta: str, saldo: float):
        ''' CONSTRUCTOR DE CLASE '''
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo

    def set_numero_cuenta(self, numero_cuenta: str):
        ''' METODO SETTER PARA NUMERO DE CUENTA '''
        self.__numero_cuenta = numero_cuenta

    def get_numero_cuenta(self):
        ''' METODO GETTER PARA NUMERO DE CUENTA '''
        return self.__numero_cuenta
    
    def set_saldo(self, saldo: float):
        ''' METODO SETTER PARA SALDO '''
        self.__saldo = saldo

    def get_saldo(self):
        ''' METODO GETTER PARA SALDO '''
        return self.__saldo

    def depositar(self, monto):
        ''' METODO DEPOSITAR PARA CUENTA '''
        if isinstance(monto, (int, float)) and monto >= 0:
            self.__saldo += monto

    def retirar(self, monto):
        ''' METODO RETIRAR PARA CUENTA '''
        if isinstance(monto, (int,float)) and monto >= 0:
            self.__saldo -= monto