# Aula 02 Módulos e funções
# 1- Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.


numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')


# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições: 
# -> criança (0-12 anos)
# -> adolescente (13-18 anos)
# -> adulto (+18 anos)

idade = int(input('Digite sua idade: '))
if idade <= 12:
    print('Você é uma criança')
elif idade <= 18:
    print('Você é um adolescente')
else:
    print('Você é um adulto')


# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.


login = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')
if login == 'lukasz' and senha == 'senha123@':
    print('Acesso concedido')
else:
    print('Senha ou usuário incorretos')



# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano esse ponto se encontra. 
# -> quadrante 1: os valores de x e y devem ser maiores que zero;
# -> quadrante 2: o valor de x é menor que zero e o valor de y é maior que zero;
# -> quadrante 3: os valores de x e y devem ser menores que zero;
# -> quadrante 4: o valor de x é maior que zero e o valor de y é menor que zero;
# -> origem: o ponto (0, 0).

def coordenadas(x, y):
    if x > 0 and y > 0:
        print('O ponto está no quadrante 1')
    elif x < 0 and y > 0:
        print('O ponto está no quadrante 2')
    elif x < 0 and y < 0:
        print('O ponto está no quadrante 3')
    elif x > 0 and y < 0:
        print('O ponto está no quadrante 4')
    else:
        print('O ponto está na origem')


x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

coordenadas(x, y)