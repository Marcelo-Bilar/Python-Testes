print('-='*30)
print('ANALISADOR DE TRIANGULOS')
print('-='*30)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if((n1 <= n2 + n3 and n2 <= n1 + n3 and n3 <= n2 + n1) and (n1 == n2 and n2 == n3 and n3 == n1)):
    print('Os segmentos informados podem formar um triãngulo equilátero ')
elif((n1 <= n2 + n3 and n2 <= n1 + n3 and n3 <= n2 + n1) and ((n1 == n2 and n3 != n1) or (n3 == n2 and n1 != n3) or (n1 == n3 and n2 != n3))):
    print('Os segmentos informados podem formar um triãngulo isóceles ')
elif((n1 <= n2 + n3 and n2 <= n1 + n3 and n3 <= n2 + n1) and (n1 != n2 and n2 != n3 and n3 != n1)): 
    print('Os segmentos informados podem formar um triângulo escaleno')
else:
    print('Os segmentos informados não podem formar um triângulo')
input("PRESSIONE ENTER PARA FINALIZAR ;)")