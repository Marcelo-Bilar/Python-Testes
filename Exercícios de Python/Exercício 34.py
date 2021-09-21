salario = float(input('Digite o valor do salário atual: '))
if(salario>1250):
    salarionovo = salario+(salario*0.10)
    print(f'O novo salário é {salarionovo:.2f} Reais')
else:
    salarionovo = salario+(salario*0.15)
    print(f'O novo salário é {salarionovo:.2f} Reais')
input("PRESSIONE ENTER PARA FINALIZAR ;)")