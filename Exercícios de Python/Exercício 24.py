cidade = str(input('Digite o nome da cidade: ')).lower().split()
if('santo' in cidade[0]):
    cidadea = ' '.join(cidade)
    print(f'A cidade {cidadea.capitalize()} começa com santo')
else:
    cidadea = ' '.join(cidade)
    print(f'A cidade {cidadea.capitalize()} não começa com santo')
input("PRESSIONE ENTER PARA FINALIZAR ;)")