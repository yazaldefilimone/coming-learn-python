class Person:
    def __init__(self, nome, idade, cpf):
        self.nome = nome;
        self.idade = idade;
        self.__cpf = cpf;

    def seEMaiorDeIdade(self):
        
        if self.idade > 17:
            print('voce e maior de idade');
            return True;

        elif self.idade <= 12:
            print('voce e pree-adolecente');
            return False;

        elif self.idade > 12 and self.idade < 17:
            print('voce e adolecente!!!')
            return False;

    def MostrarOCpf(self):
        eValido = self.seEMaiorDeIdade();

        if eValido:
            print(f'o cpf e: {self.__cpf}');

        else:
            print('idade invalida!!!');

person = Person('yazalde', 17, 8256991064416791);

person.MostrarOCpf()
