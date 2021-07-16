if __name__ == '__main__':
    listanum = [10, 20, 30, 40, 50, 60, 70]
    lista_filtrada = list(filter(lambda i:i>30, listanum))
    for n in lista_filtrada:
        print(f'{n}')