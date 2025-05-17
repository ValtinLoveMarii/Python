def login():
    user = str(input('User: ')).lower()
    password = str(input('Pass: ')).lower()
    return user, password
def cadastrar(users):
    user = str(input('User para cadastro: ')).lower()
    password = str(input('Pass para cadastro: ')).lower()
    users.update({user:password})