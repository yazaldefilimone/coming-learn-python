# uma funcao pode ser feita pra armazebar codigo reutilizaveil.

#uma funcao pode receber quantos parametrod forem.
def verificaAIdadeDoUsuario(idade3, nome):
  #normalmente uma funcao sempre retirna alguma coisa mas isso nao te impede  de mudar o return pelo print
    if idade3 < 18:
        return f'voce se chama { nome } e é menor de idade { idade3 }'

    elif idade3 >= 60:
        return f'voce se chama { nome } e é idosa: { idade3 }'

    else:
        return f'voce se chama { nome  } e é maior de idade { idade3 }'

#aqui eu chamo a funcao com os paamentros esperandos a idade3, e o nome
print(verificaAIdadeDoUsuario(18, 'yazalde'));

