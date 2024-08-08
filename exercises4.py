# 1- Crie um dicionario representando informações sobre uma pessoa, como nome, idade e cidade.
pessoas = [{'nome': 'Lucas', 'idade': 27, 'cidade': 'São Paulo'}, 
          {'nome': 'João', 'idade': 30, 'cidade':'Rio de Janeiro'},
          {'nome': 'Alice', 'idade': 4, 'cidade': 'Brasília'}]

# 2- Utilizando o dicionario criado no item anterior: 
## -> Modifique o valor de um dos itens no dicionário(por exemplo, atualize a idade da pessoa);
pessoas[0]['idade'] = 28
#print(pessoa[0])
## -> Adicione um campo de profissão à pessoa;

#for i in range(len(pessoas)):
#    pessoas[i]['profissao'] = 'Desenvolvedor'
#    print(pessoas[i])

## -> Remova um item do dicionario;

#for i in range(len(pessoas)):
#    del pessoas[i]['idade']
#    print(pessoas[i])


# 3- Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

numeros = {x: x**2 for x in range(1, 6)}
print(numeros)

# 4- Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário. 
if 'nome' in pessoas:
    print('Chave encontrada')
else:
    print('Chave não encontrada')

# 5- Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionario. 