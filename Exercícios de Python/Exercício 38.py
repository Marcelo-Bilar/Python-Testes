print('-='*30)
print('COMPARADOR DE NÚMEROS')
print('-='*30)
num1 = int(input('DIGITE UM NÚMERO: '))
num2 = int(input('DIGITE OUTRO NÚMERO: '))
print('-='*30)
if (num1 > num2):
      print(f'O NÚMERO {num1} É MAIOR QUE {num2}')
      print('-='*30)
elif (num2 > num1):
      print(f'O NÚMERO {num2} É MAIOR QUE {num1}')
      print('-='*30)
else:
    print(f'O NÚMERO {num1} É IGUAL A {num2}')
    print('-='*30)
input("PRESSIONE ENTER PARA FINALIZAR ;)")