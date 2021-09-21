print('-='*30)
print('TA NA HORA DE SE ALISTAR? ')
print('-='*30)
ano = int(input('DIGITE O SEU ANO DE NASCIMENTO: '))
idade = 2021-ano
print('-='*30)
if (idade == 18):
    print(f'SE FUFU, TA COM {idade} E VAI SE ALISTAR')
    print('-='*30)
elif(idade < 18):
    tempo = 18 - idade
    print(f'TA LIVRE POR ENQUANTO VAGABUNDO, FALTA {tempo} ANOS AINDA')
    print('-='*30)
else:
    print(f'SE TA COM {idade} ANIMAL, PASSO DA HORA')
    print('-='*30)
input("PRESSIONE ENTER PARA FINALIZAR ;)")