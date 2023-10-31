"""classes são objetos que recebem funções."""

class Carro():
    """Uma tentativa simples de representar um carro"""

    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos que descrevem o carro"""
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0 #acrescentando um atributo

    def descricao_nome(self):
        """Retorna um nome descritivo"""
        nome_longo = f'Modelo: {self.modelo}\nAno: {self.ano}\nFabricante: {self.fabricante}'
        return nome_longo.title()
    
    def leia_odometro(self):
        """Retorna o valor do odometro"""
        odo = f'O veículo tem {self.odometro} KM'
        return odo
    
    def altera_odometro(self, novo_odometro):
        """Altera o dometro pelo valor do argumento"""
        self.odometro = novo_odometro
        return 


meu_carro = Carro('Ferrari', 'Enzo', 2013)
print(meu_carro.descricao_nome())
print(meu_carro.leia_odometro())
print('Mudando o odometro\n')
meu_carro.odometro = 15 #é possível alterar o valor deste atributo apenas declarando
print(meu_carro.leia_odometro())


print('Mudando odometro por um método')
meu_carro.altera_odometro(10) #alterando odometro através de um novo método
print(meu_carro.leia_odometro())

