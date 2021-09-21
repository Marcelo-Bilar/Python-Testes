valorcasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
tempo = int(input('Em quantos anos você vai pagar a casa? '))
prestacao = (valorcasa/tempo)/12
if (prestacao > (0.3*salario)):
        print('Seu emprestimo foi negado')
else:
    print('Seu emprestimo foi aprovado')
input("PRESSIONE ENTER PARA FINALIZAR ;)")