from validations import validate_not_empty, validate_int


def validate_name(input_text, message_error):

    ''' FUNCION PARA VALIDAR EL NOMBRE '''
    
    nombre = validate_not_empty(input_text)
    while not nombre.isalpha():
        print(message_error)
        nombre = validate_not_empty(input_text)
    return nombre.capitalize()

def validate_lastname(input_text, message_error):
    
    ''' FUNCION PARA VALIDAR EL APELLIDO '''

    lastname = validate_not_empty(input_text)
    while not lastname.isalpha():
        print(message_error)
        lastname = validate_not_empty(input_text)
    return lastname.capitalize()


def validate_cedula(input_text):

    ''' FUNCION PARA VALIDAR CEDULA '''

    cedula = validate_int(input_text, 'La cedula solo debe contener numeros.')
    return cedula

def validate_username(input_text, message_error):

    ''' FUNCION PARA VALIDAR NOMBRE DE USUARIO '''

    username = validate_not_empty(input_text)
    while not username.isalpha():
        print(message_error)
        username = validate_not_empty(input_text)
    return username

def validate_password(input_text):

    ''' FUNCION PARA VALIDAR CONTRASEÑA '''

    password = validate_not_empty(input_text)

    return password