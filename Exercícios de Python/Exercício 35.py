print('-='*30)
print('ANALISADOR DE TRIANGULOS')
print('-='*30)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if(n1 <= n2 + n3 and n2 <= n1 + n3 and n3 <= n2 + n1):
    print('Os segmentos informados podem formar um triãngulo! ')
else: 
    print('Os segmentos informados não podem formar um triãngulo! ')
input("PRESSIONE ENTER PARA FINALIZAR ;)")