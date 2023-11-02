"""classes são objetos que recebem funções."""

class Carro():
    """Uma tentativa simples de representar um carro"""

    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos que descrevem o carro"""
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.combustivel = 100
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

    def tanque_gasolina(self):
        """Exibe a quantidade do combustível"""
        resp = f'Nível do combustível {self.combustivel}%'
        return resp

""" print('CARRO 1')
carro1 = Carro("Honda", 'Civic', 2015)
print(carro1.descricao_nome())
print(carro1.tanque_gasolina())
print('-' * 30) """

""" entrando no conceito de HERANÇA """
#é comum chamarem a classe-pai de SUPERclasse e a filho de SUBclasse
class CarroEletrico(Carro): #ao definir como parametro da class a classe Carro() tornamos a classe CarroElétrico um filho do Carro.
    """Representa aspectos de um carro específico, no caso, carro elétrico"""
    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos da classe-pai"""
        super().__init__(fabricante, modelo, ano) #aqui nós chamamos os atributos da classe-pai.
        self.bateria = Bateria() #é possível adicionar uma classe como atributo
    
    def tanque_gasolina(self): #ao escreve um método com mesmo nome que existe na classe-pai, o método é subscrito.
        """Método para subscrever a contagem de gasolina em carros elétricos"""
        return 'Carros elétricos não usam gasolina'

class Bateria():
    """criando uma bateria"""
    def __init__(self, bateria=100):
        self.bateria = bateria

    def altera_bateria(self, novo_valor):
        """altera o valor da bateria"""
        self.bateria = novo_valor
    def mostra_bateria(self):
        print(self.bateria)

        
meu_carro = CarroEletrico('Honda', 'Civic', 2015)
print(meu_carro.descricao_nome())

meu_carro.bateria.altera_bateria(56)
meu_carro.bateria.mostra_bateria()