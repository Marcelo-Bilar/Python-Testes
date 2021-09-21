ano = int(input('Digite o ano do seu nascimento'))
idade = 2021 - ano
if(idade<=9):
    print(f'Com {idade} anos a sua categoria é mirim')
elif(idade<=14):
    print(f'Com {idade} anos a sua categoria é infantil')
elif(idade<=19):
    print(f'Com {idade} anos a sua categoria é junior')
elif(idade<=24):
    print(f'Com {idade} anos a sua categoria é senior')
else:
    print(f'Com {idade} anos a sua categoria é master')
input("PRESSIONE ENTER PARA FINALIZAR ;)")