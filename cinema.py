#importa biblioteca
import os   
# Entrade de dados
nome = input('Informe o seu nome: ')
idade = int(input('Informe a sua idade: '))

# limpa console
os.system('cls')

# inicia o loop
while True:
    # exibe a lista de filmes e suas salas
    print(f'{'-'*20}Filmes em cartaz{'-'*20}\n')
    print('Sala 1 - A Volta dos Que Não Foram. - 16 anos.')
    print('Sala 2 - A Roda Quadrada. - 12 anos.')
    print('Sala 3 - Poeira em Alto Mar. - 14 anos.')
    print('Sala 4 - As Tranças do Rei Careca. - Livre')
    print('Sala 5 - A Vingança do Peixe Frito. - 18 anos.')

    # recebe a sala escolhida
    sala = input('Informe a sala desejada: ')

    # limpa console
    os.system('cls')

    # verifica a sala e a idade
    match sala:
        case '1':
            idade_minima = 16
        case '2':
            idade_minima = 12
        case '3':
            idade_minima = 14
        case '4':
            idade_minima = 0
        case '5':
            idade_minima = 18
        case _:
            print('Sala inexistente.')
            continue
    
    if idade >= idade_minima:
        print(f'Retire o seu Ingresso {nome}. Bom filme!')
        break
    else:
        print(f'Entrada não permitida para {nome}. Favor escolher outro filme!')
        continue