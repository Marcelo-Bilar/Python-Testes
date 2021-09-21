from math import sqrt, ceil
import random
ale = random.randint(1, 10)
num = int(input('Digite um número: '))
numb = num * 2
numt = num * 3
numq= sqrt(num)
numq2 = ceil(numq)

print(f'O dobro de {num} é {numb}, o triplo é {numt} e a raiz quadrada é {numq2}')
print(f'o numero aleatorio escolhido foi {ale}')
input("PRESSIONE ENTER PARA FINALIZAR ;)")