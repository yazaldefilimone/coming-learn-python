
'''
S do SOLID em poucas palavra quer dizer que uma class so pode ter um funcionalidade olhando o contexto claro.
nesta class Cadastro so tem uma funcao de login.
o resto de outras funcoes deveria estar em outra class,
entao considere que todas funcoes desta class execpto a login estao fira desta class.
''' 

class Cadastro:
    def __init__()self:
        self.__db = [];


    def login(self, email:str, password:str):
        if self.__isValid(email, password):
            return self.__userRepository(email, password);
        else:
            return self.__userError();



    def __isValid(self, email:str, password:str) -> bool:
        if isinstance(email, str) and isinstance(password, str):
            return True;
        else:
            return False;


    def __createuserRepository(self, email:str, password:str) -> dict:
        user = { 'email': email, 'password':password }
        self.__db.append(user);
        return user;

    def __findAllUserRepository(self) -> list:
        return self.__db()

    def __userError(self) -> str:
        error = 'internal server error!!';
        return error

cadastro = Cadastro();
print(cadastro.login('email@gmail.com', '123456'));
