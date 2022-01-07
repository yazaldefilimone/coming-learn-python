class MinhaClasse:
    def __init__(self, nome): # o __init__ e o contructor da class.
        self.nome = nome; # o self representa a class MinhaClasse

    def acessarONome(self):
        print(self.nome)


    def deletarONome(self):# e obrigatorio que passe o paramentro self em cada funcoa criada.
        self.nome = '';
        print(self.nome)



InstanciaDaClasse = MinhaClasse('yazalde');

print(InstanciaDaClasse.nome);

InstanciaDaClasse.acessarONome();

InstanciaDaClasse.deletarONome()
