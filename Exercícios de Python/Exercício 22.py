nome = str(input('Digite seu nome completo: ')).strip()

print('Em maisculo seu nome fica ', nome.upper())
print('Em minusculo seu nome fica ', nome.lower())
print(f'Seu nome tem ', (len(nome) - nome.count(' ')),'letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')
input("PRESSIONE ENTER PARA FINALIZAR ;)")