print('-='*30)
print('CONVERSOR DE BASES NÚMERICAS')
print('-='*30)
num = int(input('DIGITE UM NÚMERO PARA CONVERTER-LO: '))
print('-='*30)
print('DIGITE 1 PARA CONVERTER PARA BÍNARIO')
print('DIGITE 2 PARA CONVERTER PARA OCTAL')
print('DIGITE 3 PARA CONVERTER PARA HEXADECIMAL')
cont = int(input('-> '))
print('-='*30)
if(cont == 1):
    print(f'O NÚMERO {num} CONVERTIDO PARA BÍNARIO É {bin(num)[2:]}')

elif(cont ==2):
    print(f'O NÚMERO {num} CONVERTIDO PARA OCTAL É {oct(num)[2:]}')

elif(cont ==3):
    print(f'O NÚMERO {num} CONVERTIDO PARA HEXADECIMAL É {hex(num)[2:]}')
else:
    print('OPÇÃO INVÁLIDA, TENTA DENOVO CORNO')
input("PRESSIONE ENTER PARA FINALIZAR ;)")