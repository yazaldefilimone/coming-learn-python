class Person:
    def __init__(self, nome:str, idade:int, cpf:str) -> None:
        self.nome = nome;
        self.idade = idade;
        self.__cpf = cpf;

    def seEMaiorDeIdade(self) -> bool:
        
        if self.idade > 17:
            print('voce e maior de idade');
            return True;

        elif self.idade <= 12:
            print('voce e pree-adolecente');
            return False;

        elif self.idade > 12 and self.idade < 17:
            print('voce e adolecente!!!')
            return False;

    def MostrarOCpf(self) -> None:
        eValido = self.seEMaiorDeIdade();

        if eValido:
            print(f'o cpf e: {self.__cpf}');

        else:
            print('idade invalida!!!');

person = Person('yazalde', 17, 8256991064416791);

person.MostrarOCpf()
