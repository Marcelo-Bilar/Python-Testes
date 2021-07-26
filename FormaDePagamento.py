from Enums.MeioPagamento import MeioPagamento
from Classes.Compra import Compra

if __name__ == '__main__':
    produtos_disponiveis = [
        {'nome': 'Chinelo', 'preco_unidade': 20},
        {'nome': 'Tenis', 'preco_unidade': 250},
        {'nome': 'Sandalia', 'preco_unidade': 100},
        {'nome': 'Calça', 'preco_unidade': 120}
    ]

    produtos_selecionados = []

    while True: 
        produto_digitado = input("Digite o nome do produto que irá comprar ('sair' para sair): ")

        if(produto_digitado == 'sair'):
            break

        produtos_encontrados = list(filter(lambda p : p['nome'] == produto_digitado, produtos_disponiveis))

        if len(produtos_encontrados) == 0:
            print('Esse produto não foi encontrado, Favor digite outro')
        else:
            while True:
                try:
                    qtd_produto = int(input('Digite a quantidade que você deseja: '))
                    break
                except:
                    print('Quantidade digitada incorreta, favor digitar novamente. ')

            produtos_selecionados.append({
                'nome': produto_digitado,
                'quantidade': qtd_produto,
                'valor': produtos_encontrados[0]['preco_unidade']
            })
            
    while True:
            try:
                meio_pagamento_digitado = input('Digite a forma de Pagamento (Pix ou Boleto): ')
                meio_pagamento = MeioPagamento(meio_pagamento_digitado)
                break
            except:
                print('Forma de Pagamento inválida, favor digitar novamente')

    compra = Compra(meio_pagamento, produtos_selecionados)
    compra.RealizarCompra()