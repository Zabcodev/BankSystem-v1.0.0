from usuario.Usuario import Usuario
from cuenta.Cuenta import Cuenta
from validations import validate_not_empty
from cuenta.validations_account import validate_account_number

class SistemaBancario:

    '''CLASE SISTEMA BANCARIO '''

    def __init__(self, lista_usuarios: list[Usuario], sesion: Usuario = None):
        self.lista_usuarios = lista_usuarios
        self.sesion = sesion

    def main(self):

        ''' FUNCION PRINCIPAL '''
        
        is_selected = False
        while not is_selected:
            print('\n')
            print('---------- BIENVENIDO AL SISTEMA BANCARIO ----------')
            print('1. Iniciar sesion.')
            print('2. Finalizar.')
            opcion = validate_not_empty('Selecciona una opcion: ')
            match(opcion):
                case '1': 
                    self.iniciar_sesion()
                    if self.sesion is not None:
                        self.menu_usuario()
                case '2': 
                    print('\nLa ejecucion ha finalizado')
                    break
                case _: print('\nOpcion no valida.')

    def iniciar_sesion(self):

        ''' METODO DE INICIO DE SESION '''
        
        print('\n')
        print('---------- INICIAR SESION ----------')
        print('------------------------------------')
        username: str = validate_not_empty('Nombre de usuario: ')
        password: str = validate_not_empty('Contraseña: ')

        usuario: list[Usuario] = [usuario for usuario in self.lista_usuarios 
                                  if usuario.get_username() == username and usuario.get_password() == password]
        
        # Se verifica que el usuario este registrado
        if len(usuario) == 0:
            print('Nombre de usuario o contraseña invalida')
        else:
            self.sesion = usuario[0]

    def menu_usuario(self):
        is_back = False

        while not is_back:
            print('\n')
            print('---------- MENU ----------')
            print('--------------------------')
            print('1. Crear cuenta bancaria.')
            print('2. Depositar.')
            print('3. Retirar.')
            print('4. Transferir.')
            print('5. Cerrar sesion.')
            opcion = validate_not_empty('Selecciona una opcion: ')

            match(opcion):
                case '1': self.crear_cuenta_bancaria()
                case '2': self.depositar()
                case '3': self.retirar()
                case '4': self.transferir()
                case '5': is_back = self.cerrar_sesion()
                case _: print('\nOpcion no valida.')

    def crear_cuenta_bancaria(self):
        print('\n')
        print('---------- CREAR CUENTA BANCARIA ----------')
        print('-------------------------------------------')
        usuario = self.sesion
        if usuario.get_cuentas() is not None:
            print('\nYa posee cuenta bancaria.')
        else:
            numero_cuenta = validate_account_number('Numero de cuenta: ')
            saldo_inicial = input('Saldo inicial: ')
            nueva_cuenta = Cuenta(numero_cuenta, saldo_inicial)
            usuario.set_cuentas(nueva_cuenta)
            print(f'Su nuevo numero de cuenta es: {numero_cuenta}')
            print(f'\nSaldo de la cuenta: {saldo_inicial}$')

    def depositar(self):
        print('\n')
        print('---------- DEPOSITAR DINERO ----------')
        print('--------------------------------------')
        usuario = self.sesion
        if usuario.get_cuentas() is None:
            print('\nNo posee cuentas bancarias, debe crear una.')
        else:
            saldo_depositar = input('Saldo a depositar: ')
            cuenta_origen = usuario.get_cuentas()
            cuenta_origen[0].depositar(float(saldo_depositar))
            print('\nDeposito realizado con exito')
            print(f'\nSaldo: {cuenta_origen[0].get_saldo()}')

    def retirar(self):
        print('\n')
        print('---------- RETIRAR DINERO ----------')
        print('------------------------------------')
        usuario = self.sesion
        if usuario.get_cuentas() is None:
            print('\nNo posee cuentas bancarias, debe crear una.')
        else:
            saldo_retirar = float(input('Saldo a retirar: '))
            cuenta_origen = usuario.get_cuentas()
            if cuenta_origen[0].get_saldo() >= saldo_retirar:
                cuenta_origen[0].retirar(saldo_retirar)
                print('\nRetiro realizado con exito.')
                print(f'\nSaldo: {cuenta_origen[0].get_saldo()}')
            else:
                print('\nFondos insuficientes.')

    def transferir(self):
        print('\n')
        print('---------- TRANSFERIR DINERO ----------')
        print('---------------------------------------')
        usuario = self.sesion
        if usuario.get_cuentas() is None:
            print('\nNo posee cuentas bancarias, debe crear una.')
        else:
            cedula_usuario_destino = int(input('Cedula de la persona a transferir: '))
            usuario_destino = [usuario for usuario in self.lista_usuarios if usuario.get_cedula() == cedula_usuario_destino]
            while usuario_destino is None:
                print('\nLa cedula proporcionada no pertenece a ningun usuario. Intente nuevamente')
                cedula_usuario_destino = int(input('Cedula de la persona a transferir: '))
            
            print('------------------------------------------------------------------------------')
            print(f'Datos del usuario encontrado: ')
            print(f'\nCedula: {cedula_usuario_destino}')
            print(f'\nNumero de cuenta: {usuario_destino[0].get_cuentas()[0].get_numero_cuenta()}')
            print('------------------------------------------------------------------------------')

            print('------------------------------------------------------------------------------')
            print(f'Saldo actual: {usuario.get_cuentas()[0].get_saldo()}')
            print('-----------------------------------------------------')
            saldo_a_transferir = float(input('Saldo a transferir: '))
            if saldo_a_transferir > usuario.get_cuentas()[0].get_saldo():
                print('\nFondos insuficientes.')
            else:
                usuario_destino[0].get_cuentas()[0].depositar(saldo_a_transferir)
                usuario.get_cuentas()[0].retirar(saldo_a_transferir)
                print('Transferencia realizada con exito.')
                print(f'Saldo transferido: {saldo_a_transferir}')
                print(f'Saldo restante: {usuario.get_cuentas()[0].get_saldo()}')

            
    def cerrar_sesion(self):
        self.sesion = None
        return True
    
