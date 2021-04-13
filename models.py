import bcrypt

def hash(password):
    '''returns bcrypt hashed password'''
    return bcrypt.hashpw(password.encode('ascii'), bcrypt.gensalt())

def checkpassword(password, original):
    ''' Returns true if unhashed password (1st argument) is hashed version of 2nd argument'''
    return bcrypt.checkpw(password.encode(), original.encode())