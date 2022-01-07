'''
Ao colocar o decorector @staticmethod a funcao se torna statica,
podendo ser acessada sem precisar estaciar a class.
'''

class Cantar:
   
    @staticmethod
    def cantar(self) -> None:
        print('la la la...');

    parar(self) -> None:
        print('stop...');


Cantar.cantar();

cantar = Cantar();
cantar.parar() # so posso chamar a funcao parar depis que estacio a class.
