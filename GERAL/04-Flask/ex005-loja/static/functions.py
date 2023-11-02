class Produto():
    def __init__(self, nome, preco, estoque, img, status):
       """inicializa os atributos dos produtos"""
       self.nome = nome
       self.preco = preco
       self.estoque = estoque
       self.img = img
       self.status = status

    def descricao_produto(self):
        nome = f'{self.nome}\n{self.preco}\n{self.estoque}\n{self.img}\n{self.status}'
        return nome
    

