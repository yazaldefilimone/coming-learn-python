class MinhaClasse:
    def __init__(self, nome):
        self.nome = nome;

    def acessarONome(self):
        print(self.nome)


    def deletarONome(self):
        self.nome = '';
        print(self.nome)



InstanciaDaClasse = MinhaClasse('yazalde');

print(InstanciaDaClasse.nome);

InstanciaDaClasse.acessarONome();

InstanciaDaClasse.deletarONome()
