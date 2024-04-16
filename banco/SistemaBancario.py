from usuario.Usuario import Usuario
from cuenta.Cuenta import Cuenta
from validations import validate_not_empty
from cuenta.validations_account import validate_account_number, validate_saldo, generate_number_account
from usuario.user_validations import validate_name, validate_lastname, validate_cedula, validate_username, validate_password

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
            print('2. Crear usuario.')
            print('3. Finalizar.')
            opcion = validate_not_empty('Selecciona una opcion: ')
            match(opcion):
                case '1': 
                    self.iniciar_sesion()
                    if self.sesion is not None:
                        self.menu_usuario()
                case '2': self.create_account()
                case '3': 
                    print('\nLa ejecucion ha finalizado')
                    break
                case _: print('\nOpcion no valida.')


    def create_account(self):

        ''' METODO PARA REGISTRARSE '''

        print('\n')
        print('---------- REGISTRARSE ----------')
        print('---------------------------------')

        nuevo_nombre = validate_name('Nombre: ', 'El nombre no puede contener numeros o caracteres especiales.')
        nuevo_apellido = validate_lastname('Apellido: ', 'El apellido no puede contener numeros o caracteres especiales')
        nueva_cedula = validate_cedula('Cedula: ')
        nuevo_username = validate_username('Nombre de usuario: ', 'El nombre de usuario no puede contener numeros.')
        nueva_contrasenia = validate_password('Contraseña: ')

        nuevo_usuario = Usuario(nuevo_nombre, nuevo_apellido, nueva_cedula, nuevo_username, nueva_contrasenia)
        
        verificar_usuario = [usuario for usuario in self.lista_usuarios if nuevo_usuario.get_username() == usuario.get_username() or nuevo_usuario.get_cedula() == usuario.get_cedula()]

        if len(verificar_usuario) > 0:
            print('\nUsuario registrado.')
        else:
            self.lista_usuarios.append(nuevo_usuario)
            print('\nUsuario registrado exitosamente')


    def iniciar_sesion(self):

        ''' METODO DE INICIO DE SESION '''
        
        print('\n')
        print('---------- INICIAR SESION ----------')
        print('------------------------------------')
        username: str = validate_username('Nombre de usuario: ', 'El nombre de usuario no puede contener numeros')
        password: str = validate_password('Contraseña: ')

        usuario: list[Usuario] = [usuario for usuario in self.lista_usuarios 
                                  if usuario.get_username() == username and usuario.get_password() == password]
        
        # Se verifica que el usuario este registrado
        if len(usuario) == 0:
            print('Nombre de usuario o contraseña invalida')
        else:
            self.sesion = usuario[0]


    def menu_usuario(self):

        ''' MENU DE USUARIO '''

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

        ''' METODO PARA CREAR CUENTA BANCARIA '''

        print('\n')
        print('---------- CREAR CUENTA BANCARIA ----------')
        print('-------------------------------------------')
        if len(self.sesion.get_cuentas()) > 0:
            print('\nYa posee cuenta bancaria.')
        else:
            numero_cuenta = generate_number_account()
            saldo_inicial = validate_saldo('Saldo inicial: ')
            self.sesion.set_cuentas(Cuenta(numero_cuenta, saldo_inicial))
            print('----------------------------------------------')
            print(f'Su nuevo numero de cuenta es: {numero_cuenta}')
            print(f'\nSaldo de la cuenta: {saldo_inicial}$')
            print('----------------------------------------------')


    def depositar(self):

        ''' METODO PARA DEPOSITAR DINERO '''

        print('\n')
        print('---------- DEPOSITAR DINERO ----------')
        print('--------------------------------------')
        if len(self.sesion.get_cuentas()) == 0:
            print('\nNo posee cuentas bancarias, debe crear una.')
        else:
            saldo_depositar = validate_saldo('Saldo a depositar: ')
            cuenta_origen = self.sesion.get_cuentas()
            cuenta_origen[0].depositar(float(saldo_depositar))
            print('\nDeposito realizado con exito')
            print(f'\nSaldo: {cuenta_origen[0].get_saldo()}')


    def retirar(self):

        ''' METODO PARA RETIRAR DINERO '''

        print('\n')
        print('---------- RETIRAR DINERO ----------')
        print('------------------------------------')
        if len(self.sesion.get_cuentas()) == 0:
            print('\nNo posee cuentas bancarias, debe crear una.')
        else:
            saldo_retirar = validate_saldo('Saldo a retirar: ')
            cuenta_origen = self.sesion.get_cuentas()
            if cuenta_origen[0].get_saldo() >= saldo_retirar:
                cuenta_origen[0].retirar(saldo_retirar)
                print('\nRetiro realizado con exito.')
                print(f'\nSaldo: {cuenta_origen[0].get_saldo()}')
            else:
                print('\nFondos insuficientes.')

    def transferir(self):

        ''' METODO PARA TRANSFERIR DINERO '''

        print('\n')
        print('---------- TRANSFERIR DINERO ----------')
        print('---------------------------------------')
        
        if len(self.sesion.get_cuentas()) == 0:
            print('\nNo posee cuentas bancarias, debe crear una.')
        else:
            cedula_usuario_destino = validate_cedula('\nCedula de la persona a transferir: ')
            while len([usuario for usuario in self.lista_usuarios if usuario.get_cedula() == cedula_usuario_destino]) == 0:
                print('\nLa cedula proporcionada no pertenece a ningun usuario. Intente nuevamente')
                cedula_usuario_destino = validate_cedula('Cedula de la persona a transferir: ')
            
            usuario_destino = [usuario for usuario in self.lista_usuarios if usuario.get_cedula() == cedula_usuario_destino]
            print('------------------------------------------------------------------------------')
            print(f'Datos del usuario encontrado: ')
            print(f'\nCedula: {cedula_usuario_destino}')
            print(f'\nNumero de cuenta: {usuario_destino[0].get_cuentas()[0].get_numero_cuenta()}')
            print('------------------------------------------------------------------------------')

            print('------------------------------------------------------------------------------')
            cuenta_a_transferir = validate_account_number('Numero de cuenta del usuario: ')
            if cuenta_a_transferir != usuario_destino[0].get_cuentas()[0].get_numero_cuenta():
                print('Numero de cuenta incorrecto.')
            else:
                print('-----------------------------------------------------')
                print(f'Saldo actual: {self.sesion.get_cuentas()[0].get_saldo()}')
                saldo_a_transferir = validate_saldo('Saldo a transferir: ')
                print('-----------------------------------------------------')
                if saldo_a_transferir > self.sesion.get_cuentas()[0].get_saldo():
                    print('\nFondos insuficientes.')
                else:
                    print('-----------------------------------------------------')
                    usuario_destino[0].get_cuentas()[0].depositar(saldo_a_transferir)
                    self.sesion.get_cuentas()[0].retirar(saldo_a_transferir)
                    print('\nTransferencia realizada con exito.')
                    print(f'Saldo transferido: {saldo_a_transferir}')
                    print(f'Saldo restante: {self.sesion.get_cuentas()[0].get_saldo()}')
                    print('-----------------------------------------------------')

            
    def cerrar_sesion(self):

        ''' METODO PARA CERRAR SESION '''

        self.sesion = None
        return True
    
