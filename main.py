from banco.SistemaBancario import SistemaBancario
from usuario.Usuario import Usuario
from cuenta.Cuenta import Cuenta

def BankSystem():
    usuario1 = Usuario('John', 'Doe', 26275576, 'johndoe', '123456', [Cuenta(523658745214, 400.00)])
    usuario2 = Usuario('Ryan', 'Smith', 1234567, 'ryansmith', '123456', [Cuenta(365274581452, 400.00)])

    SistemaBancario([usuario1, usuario2]).main()

if __name__ == '__main__':
    BankSystem()