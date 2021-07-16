print("Olá, Mundo! \n")
def calcular(n1, n2, o):
    if o == '+':
        return n1 + n2
    elif o == '-':
        return n1 - n2
    elif o == '*':
        return n1 * n2
    elif o == '/':
        return n1 / n2
    elif o == '%':
        return n1 % n2
    elif o == '**':
        return n1 ** n2

if __name__ == '__main__':
    n1 = int(input('Digite o primeiro num: '))
    o = input("digite a operação: ")
    n2 = int(input('Digite o segundo num: '))
    resultado = calcular(n1, n2, o)
    print(f'o resultado da operação é {resultado}')