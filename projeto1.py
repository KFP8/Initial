# step 0 - understand the challenge you want to solve.

# step 1 - cycle through all files of database folder.
import os
import pandas as pd
import plotly.express as px

lista_arquivo = os.listdir("C://Users//User//Downloads//Vendas")
print(lista_arquivo)

tabela_total = pd.DataFrame()

# step 2 - import the sales database.
for arquivo in lista_arquivo:
    if 'Vendas' in arquivo:
    #import file
        tabela = pd.read_csv(f'C://Users//User//Downloads//Vendas//{arquivo}')
        tabela_total = pd.concat([tabela_total, tabela], ignore_index = True)
        #.append não funiona mais no pandas pelo o que parece

# step 3 - compile the database.
print(tabela_total)

# step 4 - Calculate the best-selling product (amount).
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
print(tabela_produtos)

# step 5 - calculate the most billed product (invoicing).
#create column
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
print(tabela_total)
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_faturamento)

# step 6 - calculate the store/city that sold the most (invoicing) - create a dashboard
tabela_loja = tabela_total.groupby('Loja').sum()
tabela_loja = tabela_loja[['Faturamento']]
print(tabela_loja)


grafico = px.bar(tabela_loja, x=tabela_loja.index, y='Faturamento')
grafico.show()