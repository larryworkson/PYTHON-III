from functions import ativar_db, listar_vendas

vendas = listar_vendas()

data = ativar_db(exec='''SELECT data as mes, SUM(precotot) as total_vendas FROM vendas GROUP BY mes ORDER BY mes''')
""" for i in data:
    print(i) """

meses = [linha[0] for linha in data]
tot_vendas = [linha[1] for linha in data]

print(meses)
print(tot_vendas)