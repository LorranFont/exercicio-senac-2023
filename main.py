class Produto:
    def __init__(self,nome,preco,codigo_de_barras):
        self.nome = nome
        self.preco = preco
        self.codigo_de_barras = codigo_de_barras

produto = Produto('iphone xr', 3200)
quantidade = int (input('Informe a quantidade: '))
print(quantidade)