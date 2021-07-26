from Classes.Pagamento import Pagamento


class Compra(Pagamento): 
    def __init__(self, meio_pagamento, produtos):
        super().__init__(meio_pagamento)
        self.produtos = produtos

        
    def __CalcularValorCompra(self):
        valor_compra = 0

        for p in self.produtos:
            valor_compra += p['valor'] * p['quantidade']

        return valor_compra

    def RealizarCompra(self):
        valor_compra = self.__CalcularValorCompra()
        self.RealizarPagamento(valor_compra)