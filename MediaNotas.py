if __name__ == '__main__':
    try:
        notasDosAlunos = [50, 60, 35, 96, 77]
        mediaDasNotas = lambda notas : sum(notas) / len(notas)
        print(f"A media das notas é {mediaDasNotas(notasDosAlunos)}")
        
    except Exception as e:
        print ("Ocorreu um erro ao receber informações")