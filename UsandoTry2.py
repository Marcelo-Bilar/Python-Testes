if __name__ == '__main__':
    try:
        pessoas = []
        nome = ''

        while True:
            nome = input("Digite um nome para adicionar na lista (Digite 'sair' para encerrar): ")

            if nome == "sair":
                break

            pessoas.append(nome)

        print('Pessoas na lista:')
        print(pessoas)

        pessoas.sort()
        print(pessoas)

    except Exception as e:
        print ("Ocorreu um erro ao receber informações")