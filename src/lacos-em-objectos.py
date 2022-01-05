objecto = { 'pt': 'portugues', 'en':'engles', 'es':'espanhol' }

# assim ele so ve as chaves
for chave in objecto.key:
    print(chave);

# assim ele so ve as chaves
for chave in objecto:
    print(chave);

# assim ele so ve os valores
for valor in objecto.values:
    print(valor);

for valor, chave in objecto:
    print(valor);
    print(chave);
