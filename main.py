class Produto:
    def __init__(self,nome,preco,codigo_de_barras):
        self.nome = nome
        self.preco = preco
        self.codigo_de_barras = codigo_de_barras

    def exibir(self,indice = 0):
        print(f'{indice} === Nome: {self.nome} - Preço: {self.preco}')

produto_um = Produto('iphone xr', 3200, 'leito de código de barras')
produto_dois = Produto('Iphone 11',4500,'leito de código de barras')

produtos = [produto_um,produto_dois]
for produto in produtos:
    indice = produtos.index(produto)
    produto.exibir(indice)
indice_selecionado = int(input('Selecione o produto: '))
if indice_selecionado > len(produtos) -1:
    print('Produto inexistente.')
else:
    produto = produtos[indice_selecionado]
    quantidade = int (input('Informe a quantidade: '))
    print(f'O valor total é de: R${quantidade * produto.preco}')
