def validate_not_empty(input_text: str) -> str:
    value = input(input_text)

    while value.strip() == '' or value == '':
        print('El valor no puede ser vacio')
        value = input(input_text)
    
    return value

def validate_int(input_text, message_error):
    while True:
        number = validate_not_empty(input_text)
        try:
            number = int(number)
            if number > 0:
                return number
            else:
                print('El numero debe ser mayor que 0')
        except ValueError:
            print(message_error)

def validate_float(input_text):
    while True:
        number_float = validate_not_empty(input_text)
        try:
            number_float = float(number_float)
            if number_float > 0.00:
                return format(float(number_float), '.2f')
            else:
                print('El numero debe ser mayor que 0')
        except ValueError:
            print('El valor debe ser un numero flotante')