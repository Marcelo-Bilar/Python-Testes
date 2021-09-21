num1 = int(input('Digite uma nota: '))
num2 = int(input('Digite outra nota: '))
media = (num1+num2)/2
if(media<5):
    print(f'O aluno tirou {media} e está reprovado')
elif(media>=5 and media<=6.9):
    print(f'O aluno tirou {media} e está de recuperação')
else:
    print(f'O aluno tirou {media} e está aprovado')
input("PRESSIONE ENTER PARA FINALIZAR ;)")