dist = float(input('Digite a distância da viagem: '))

if (dist <= 200):
    valor = dist * 0.5
    print(f'O valor da passagem de é R$ {valor}')
else: 
    valor = dist * 0.45
    print(f'O valor da passagem é R$ {valor}')
input("PRESSIONE ENTER PARA FINALIZAR ;)")