from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para analisar ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano {ano} é bisexto')

else:
    print(f'O ano {ano} não é bisexto')
input("PRESSIONE ENTER PARA FINALIZAR ;)")