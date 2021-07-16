if __name__ == '__main__':
    try:
        notasDosAlunos = [50, 60, 35, 96, 77, 86, 81]
        notasFiltradas = list(filter(lambda nota : nota < 80, notasDosAlunos))
        print(f"{notasFiltradas}")
        
    except Exception as e:
        print ("Ocorreu um erro ao receber informações")