import math
ang = float(input('Digite um angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print(f'O seno de {ang} é {sen:.2f}')
print(f'O cosseno de {ang} é {cos:.2f}')
print(f'A tangente de {ang} é {tang:.2f}')
input("PRESSIONE ENTER PARA FINALIZAR ;)")