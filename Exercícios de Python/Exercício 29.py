vel = int(input('Digite a velocidade do carro: '))

if (vel >= 80):
    velv = vel
    velnovo = velv - 80
    val = velnovo * 7
    print(f'Você estava {velnovo} Kms/h acima da velocidade permitida, o valor da multa é R${val}')

else: 
    print('Você está dirigindo na velocidade certa! ')
input("PRESSIONE ENTER PARA FINALIZAR ;)")