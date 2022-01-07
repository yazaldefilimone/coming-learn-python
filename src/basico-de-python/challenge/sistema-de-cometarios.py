print('Sistema de Cometários em python \n \n');

nome = input('Entre com o teu nome: \n');
senha = input('Entre com um senha com caracteres maiores do que 3: \n');
user = [];
userDB = [];

def create(user):
    userDB.append(user);
    return userDB;

def findAll:
    return userDB;

def findOne(id):
    for user in userDB:
        if user['id'] == id:
            return user['id']

def delete(id):
    for user in userDB:
        if user['id'] == id:
    ##        user.pop()



def login(nome, senha):
    if nome and senha:
        if len(senha) > 3:
          user = create({'id': len(user),'nome':nome, 'senha':senha});
     
          nome_login = input('entre o o teu nome: \n');
          senha_login = input('entre com o tua senha:\n ');
          senha_test = len(user) - 1;
          id = user[len(user) -1]['id'];
          
          if id == senha_test:
          

            if senha_login == senha and nome_login == nome:

                 print('login feito com sucesso!!! \n \n ');
                 print(f'Os seus dados são: {user[len(user)-1]}')
