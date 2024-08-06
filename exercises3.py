# 1- Crie uma lista para cada informação a seguir
## -> lista de números de 1 a 10
## -> lista com 4 nomes
## -> Lista com o ano que você nasceu e o ano que estamos

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Lucas', 'João', 'Maria', 'Ana']
anos = [1994, 2024]

# 2- Crie uma lista e utilize um loop para percorrer todos os elementos da lista

for nome in nomes:
    print(nome)


# 3- Utilize um loop para calcular a soma dos números ímpares de 1 a 10.

impares = []
for numero in numeros:
    if numero % 2 != 0:
        impares.append(numero)
        
print(sum(impares))

# 4- Utilize um loop para imprimir os números de 1 a 10 em ordem decrescente

for numero in range(10, 0, -1):
    print(numero)

# 5- Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero = int(input('Digite um número: '))
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')

# 6- Crie uma lista de números e utilize um loop para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções. 

soma = 0

for numero in numeros:
    try:
        soma += int(numero);
    except ValueError:
        print(f'Valor inválido encontrado: {numero}. Ignorando esse valor.') 

print(soma)

# 7- Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.  

try:
    soma = 0
    lista_vazia = []
    for numero in numeros: 
        soma += numero

    media = soma / len(lista_vazia)

    print(media)
except ZeroDivisionError:
    print('Não é possível calcular a média de uma lista vazia.')
