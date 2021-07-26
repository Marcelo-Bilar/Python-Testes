'''
    - Escrever um programa que recebe alguns produtos como argumento, -- OK
    - Validar se esses produtos estáo na lista de itens disponiveis do mercado -- OK
    - Caso esteja avisar o usuário quais produtos tem e quais não tem -- OK
    - E por ultimo exibir a lista de produtos disponiveis ordenados por ordem alfabética -- OK
'''

if __name__ == '__main__':
    try:
        produtos_usuario = []
        produtos_mercado = ['refrigerante', 'cerveja', 'pão', 'maçã']

        while True:
            produto = input("Digite um produto para adicionar na lista (Digite 'sair' para encerrar): ")

            if produto == 'sair':
                break

            produtos_usuario.append(produto)

        produtosIndisponiveis = []
        produtosDisponiveis = []
        
        for p in produtos_usuario:
            if not p in produtos_mercado:
                produtosIndisponiveis.append(p)
            else:
                produtosDisponiveis.append(p)

        print(f'Produtos Indisponiveis: {produtosIndisponiveis}')
        print(f'Produtos Disponiveis: {produtosDisponiveis}')

        produtos_mercado.sort()
        print(f'Todos os Produtos do Mercado: {produtos_mercado}')

    except Exception as e:
        print ("Ocorreu um erro ao receber informações")