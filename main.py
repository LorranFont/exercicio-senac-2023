class Produto:
    def __init__(self,nome,preco,codigo_de_barras):
        self.nome = nome
        self.preco = preco
        self.codigo_de_barras = codigo_de_barras

    def exibir(self):
        print(f'Nome: {self.nome} - Preço: {self.preco}')

produto = Produto('iphone xr', 3200, 'leito de código de barra')
produto.exibir()
quantidade = int (input('Informe a quantidade: '))
print(f'O valor total é de: R${quantidade * produto.preco}')
