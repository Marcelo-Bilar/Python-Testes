altura = float(input('Digite sua altura: '))
peso = float(input('Digite sua peso: '))
imc = peso/(altura*altura)
if(imc<18.5):
    print(f'Seu imc é igual a {imc:.2f} e você está abaixo do peso')
elif(imc>=18.5 and imc<25):
    print(f'Seu imc é igual a {imc:.2f} e você está no peso ideal')
elif(imc>=25 and imc<30):
    print(f'Seu imc é igual a {imc:.2f} e você está acima do peso')
elif(imc>=30 and imc<40):
    print(f'Seu imc é igual a {imc:.2f} e você está na obesidade')
else:
    print(f'Seu peso é igual a {imc:.2f} e você está na obesidade morbida')
input("PRESSIONE ENTER PARA FINALIZAR ;)")