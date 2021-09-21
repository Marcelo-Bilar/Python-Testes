import math
lado1 = float(input('Digite o tamanho do cateto oposto: '))
lado2 = float(input('Digite o tamanho do cateto adjacente: '))
hip = math.hypot(lado1, lado2)
print(f'A hipotenusa vai medir {hip:.2f}')
input("PRESSIONE ENTER PARA FINALIZAR ;)")