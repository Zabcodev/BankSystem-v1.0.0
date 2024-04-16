from validations import validate_not_empty

def validate_account_number(input_text) -> str:
    value = validate_not_empty(input_text)

    while not value.isdigit():
        print('El numero de cuenta debe ser un entero de 12 digitos.')
        value = input(input_text)

    return int(value)

def validate_saldo():
    pass
