import random
import os
while True:
    print('-='*30)
    print('JOKENPÔ VIRTUAL')
    print('-='*30)
    print('PARA JOGAR TESOURA DIGITE 1')
    print('PARA JOGAR PAPEL DIGITE 2')
    print('PARA JOGAR PEDRA DIGITE 3')
    print('-='*30)
    escolha = int(input('DIGITE SUA OPÇÃO: '))
    print('-='*30)
    escolhapc = random.randint(1, 3)
    if (escolha == 1 and escolhapc == 1):
        print('VOCÊ ESCOLHEU TESOURA E O COMPUTADOR ESCOLHEU TESOURA')
        print('EMPATE DE TESOURAS!')
    elif(escolha == 2 and escolhapc == 2):
        print('VOCÊ ESCOLHEU PAPEL E O COMPUTADOR ESCOLHEU PAPEL')
        print('EMPATE DOS PAPEIS!')
    elif(escolha == 3 and escolhapc == 3):
        print('VOCÊ ESCOLHEU PEDRA E O COMPUTADOR ESCOLHEU PEDRA')
        print('EMPATE DAS PEDRAS!')
    elif(escolha == 3 and escolhapc == 1):
        print('VOCÊ ESCOLHEU PEDRA E O COMPUTADOR ESCOLHEU TESOURA')
        print('VOCÊ GANHOU!')
    elif(escolha == 2 and escolhapc == 3):
        print('VOCÊ ESCOLHEU PAPEL E O COMPUTADOR ESCOLHEU PEDRA')
        print('VOCÊ GANHOU!')
    elif(escolha == 1 and escolhapc == 2):
        print('VOCÊ ESCOLHEU TESOURA E O COMPUTADOR ESCOLHEU PAPEL')
        print('VOCÊ GANHOU!')
    elif(escolha == 1 and escolhapc == 3):
        print('VOCÊ ESCOLHEU TESOURA E O COMPUTADOR ESCOLHEU PEDRA')
        print('VOCÊ PERDEU!')
    elif(escolha == 2 and escolhapc == 1):
        print('VOCÊ ESCOLHEU PAPEL E O COMPUTADOR ESCOLHEU TESOURA')
        print('VOCÊ PERDEU!')
    elif(escolha == 3 and escolhapc == 2):
        print('VOCÊ ESCOLHEU PEDRA E O COMPUTADOR ESCOLHEU PAPEL')
        print('VOCÊ PERDEU!')
    print('-='*30)
    print(' ')
    a=int(input("DIGITE 1 PARA REINICIAR OU 2 PARA FINALIZAR: "))
    if(a==2):
        break
    os.system('cls') or None