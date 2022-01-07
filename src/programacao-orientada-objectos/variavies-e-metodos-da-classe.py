'''
Aqui nos deparamos com dos argumentos de class o self e o cls,
nao apavora complica no inicio mas e muito facil, so peco pra que partique muito pra nao mesturar as coisas.


self = e o contexto do objecto da class ele pega o contexto quando e estaciando.

cls =  o o contexto da class em si ele pega a class toda e modifica os methodos ou variavis da class diretamente.

@classmethod = e um decorador que motra que a funcao esta a usar o contexto da class.
'''
class MyClass:
    estado = True;

    def __init__(self) -> None:


    @classmethod
    def pay(cls) -> None:
        if cls.estado:
            print(f'comprado com sucesso { cls.estado }');
        else:
            print(f'indisponivel { cls.estado }');


    def closeOrOpen(cls, novoEstado) -> None:
        cls.estado = novoEstado;

minha = MyClass();
minha2 = MyClass();

minha.pay();
minha2.pay();

MyClass.estado = False;
minha2.estado = False;

minha.closeOrOpen(False);
minha2.closeOrOpen(True);

minha.closeOrOpen(False);
minha2.closeOrOpen(True);
