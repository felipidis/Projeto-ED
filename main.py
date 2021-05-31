# coding: utf-8
import csv
import os
import random
import pandas as pd

dados = []
dadosTemp = []


def openData():
    with open('dados-original.csv', newline='', errors="ignore") as arquivo:

        leitor = csv.DictReader(
            arquivo, fieldnames=["Num", "ID", "Name", "Age", "Photo", "Nationality"])

        csv.list_dialects()

        leitor.__next__()

        for linha in leitor:
            dadosTemp.append(linha)


def randomData():
    k = 0
    visitados = []
    while(k < 100):
        valorAleatorio = random.randint(1, 18000)
        if valorAleatorio not in visitados:
            visitados.append(valorAleatorio)
            dados.append(dadosTemp[valorAleatorio])
            k += 1


def showDados():
    jogadoresDF = pd.DataFrame(
        dados, columns=["Num", "ID", "Name", "Age", "Nationality"])
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(jogadoresDF)
    print('\n')


def editarNome():
    i = int(input("Qual o indice que você gostaria de editar "))
    dados[i]["Name"] = input("Qual o nome do jogador ? ")
    print('\n')


def editarNacionalidade():
    i = int(input("Qual o indice que você gostaria de editar "))
    dados[i]["Nationality"] = input("Qual a nacionalidade do jogador ? ")
    print('\n')


def editarIdade():
    i = int(input("Qual o indice que você gostaria de editar? "))
    dados[i]["Age"] = input("Qual a idade do jogador ? ")
    print('\n')


def editarDados():
    choose = int(input(
        'Oque deseja alterar? \n1 - Editar Nome\n2 - Editar Nacionalidade\n3 - Editar Idade\n '))
    if choose == 1:
        editarNome()
    elif choose == 2:
        editarNacionalidade()
    else:
        editarIdade()


def excluirJogador():
    i = int(input('Qual o entrada você gostaria de apagar? '))
    dados.pop(i)
    print('\n')


def verificar(jogadorID, jogadorNome):
    for i in range(len(dados)):
        if jogadorID in dados[i]['ID'] or jogadorNome.lower() in dados[i]['Name'].lower():
            return False
    print('Jogador ainda não cadastrado! Pode prosseguir\n ')
    return True


def adicionarJogador():
    jogadorID = input('Qual o ID do novo jogador? ')
    jogadorNome = input('Qual o nome do novo jogador? ')
    verificacao = verificar(jogadorID, jogadorNome)
    if verificacao == False:
        print('Inicie Novamente o cadastro por favor\n')
        adicionarJogador()
    else:
        dados.append({'Num': random.randint(1, 30000), 'ID': jogadorID, 'Name': jogadorNome,
                      'Age': input('Qual a idade do novo jogador? '), 'Nationality': input('Qual o país do novo jogador? ')})
    print('\n')


def cria_csv():
    jogadoresDF = pd.DataFrame(
        dados, columns=["Num", "ID", "Name", "Age", "Nationality"])
    jogadoresDF.to_csv(r'.\dados.csv', index=False)
    print('\n')


def start():
    print('Digite a opção desejada\n1-Criar\n2-Editar\n3-Mostrar Lista\n4-Deletar Item\n5-Exportar CSV\n0-Sair')
    choose = int(input())
    if choose == 1:
        adicionarJogador()
        start()
    if choose == 2:
        editarDados()
        start()
    if choose == 3:
        showDados()
        start()
    if choose == 4:
        excluirJogador()
        start()
    if choose == 5:
        cria_csv()
        start()
    if choose == 6:
        os.system('clear')
        start()
    if choose == 0:
        exit()
    else:
        print("Operação invalida!\n")
        start()


def main():
    openData()
    randomData()
    start()


if __name__ == "__main__":
    main()
