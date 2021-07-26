from Classes.Mamifero import Mamifero
from Classes.Ave import Ave
from Classes.Reptil import Reptil
from Classes.Peixe import Peixe



if __name__ == '__main__':
    lista_animais = [
        Mamifero('Leão', 4, False, False),
        Reptil('Serpente', 4, True, 0),
        Ave('Gavião', 500, True, False),
        Peixe('Tubarão', 2, True, True),
    ]

    nome_animal = input("Digite o nome Animal Vertebrado: ")

    animal_encontrado = list(filter(lambda a : a.nome == nome_animal, lista_animais))

    if len(animal_encontrado) == 0:
        print('Animal não encontrado')
    else: 
        try:
            if(isinstance(animal_encontrado[0], Mamifero)):
                print(f'Animal {animal_encontrado[0].nome} encontrado do tipo Mamífero, qtdMamas: {animal_encontrado[0].qtdMamas}, consegue botar ovo: {animal_encontrado[0].consegueBotarOvo},  é aquatico: {animal_encontrado[0].isMamiferoAquatico}')

            elif(isinstance(animal_encontrado[0], Reptil)):
                print(f'Animal {animal_encontrado[0].nome} encontrado do tipo Reptil, qtdpatas: {animal_encontrado[0].qtdPatas}, temperatura do corpo: {animal_encontrado[0].temperaturaCorporal},  é terrestre: {animal_encontrado[0].isReptilTerrestre}')

            elif(isinstance(animal_encontrado[0], Ave)):
                print(f'Animal {animal_encontrado[0].nome} encontrado do tipo Ave, qtdPenas: {animal_encontrado[0].qtdPenas}, consegue voar: {animal_encontrado[0].consegueVoar},  consegue fazer migração {animal_encontrado[0].consegueFazerMigracao}')

            elif(isinstance(animal_encontrado[0], Peixe)):
                print(f'Animal {animal_encontrado[0].nome} encontrado do tipo Peixe, qtdNadadeiras: {animal_encontrado[0].qtdNadadeiras}, é carnivoro: {animal_encontrado[0].isCarnivoro},  é de agua salgada: {animal_encontrado[0].isPeixeAguaSalgada}')
            else:
                print('Ocorreu um erro ao informar o tipo do animal')
        except Exception as e:
             print('Ocorreu um erro, tente novamente')