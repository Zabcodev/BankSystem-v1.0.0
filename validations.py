def validate_not_empty(input_text: str) -> str:
    value = input(input_text)

    while value.strip() == '' or value == '':
        print('El valor no puede ser vacio')
        value = input(input_text)
    
    return value

def validate_int():
    pass

def validate_float():
    pass