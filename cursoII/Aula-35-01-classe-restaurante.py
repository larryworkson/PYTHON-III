class Restaurante():
    def __init__(self, restaurante_nome='Sem nome', tipo_conzinha=''):
        self.nome = restaurante_nome
        self.tipo = tipo_conzinha
    
    def restaurante_descricao(self):
        print(self.nome)
        print(self.tipo)
    
    def restaurante_aberto(self):
        print(f'O restaurante {self.nome} está aberto!')

print('Cadastre seu restaurante')
nome = str(input('Nome: ').title())
tipo = str(input('Tipo de cozinha: ').title())
Restaurante(nome, tipo).restaurante_descricao()
Restaurante(nome).restaurante_aberto()