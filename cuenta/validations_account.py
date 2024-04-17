from validations import validate_int, validate_float
from random import randint


def validate_account_number(input_text):

    ''' FUNCION PARA VALIDAR EL NUMERO DE CUENTA '''

    number_account = validate_int(input_text, 'El numero de cuenta debe estar contenido por numeros enteros.')
    return int(number_account)


def validate_saldo(input_text):

    ''' FUNCION PARA VALIDAR EL SALDO '''

    saldo = validate_float(input_text)
    return float(round(saldo, 2))


def generate_number_account():

    ''' FUNCION PARA GENERAR EL NUMERO DE CUENTA ALEATORIO '''

    number_account = randint(1, 999999999999)
    return number_account

