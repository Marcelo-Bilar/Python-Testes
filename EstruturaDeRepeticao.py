def lavarCarro(posicao):
    print(f"lavando carro na posição ...{posicao}")

def verificarTemCarroNaFila(posicao):
    if(posicao> 5):
        return False
    else:
        return True

if __name__ == '__main__':
    #Estrutura de repetição com intervalo de valores

    #For Crescente
    print("For Crescente")
    for n in range(0, 5):
        print(n)

    #For Decrescente
    print("For Decrescente")
    for n in range(5, 0, -1):
        print(n)

    #For percorrendo caracteres de uma string
    print("For in String")
    palavra = 'Devaria'
    for p in palavra:
        print(p)

    #While Crescente
    print("while Crescente")
    n = 0
    while n < 5:
        print(n)
        n += 1

    temCarroNaFila = True
    posicao = 1
    while temCarroNaFila:
        lavarCarro(posicao)
        posicao += 1
        temCarroNaFila = verificarTemCarroNaFila(posicao)
    else:
        print("Terminou de lavar os carros")