# Ex03
import pandas as pd
import matplotlib.pyplot as plt
import locale


tabela = pd.read_excel('Desafio - Time de Projetos e Dados.xlsx', sheet_name='Dados - Questão 1')
tabela1 = tabela.iloc[:-2]
locale.setlocale(locale.LC_ALL,'pt-BR.UTF-8')




# Encontrando o vendedor que mais vendeu da empresa
top3_empresa = tabela1.groupby(['nome','usuario'])['valor_compra'].sum().reset_index()
top3_empresa = top3_empresa.sort_values('valor_compra', ascending=False)
top3_empresa['valor_compra'] = top3_empresa['valor_compra'].apply(lambda x: locale.currency(x, grouping=True))
top3_empresa_geral = top3_empresa.head(3)
print('Top 3 vendedores que mais venderam na empresa:\n {}'.format(top3_empresa_geral))
print('---' * 20)



# Top 3 vendedores por loja
top_vendedor_unidade = tabela1.groupby(['Filial','nome'])['valor_compra'].sum().reset_index()
top_vendedor_unidade = top_vendedor_unidade.sort_values(['Filial','valor_compra'], ascending=[True,False])
top_vendedor_unidade['valor_compra'] = top_vendedor_unidade['valor_compra'].apply(lambda x: locale.currency(x, grouping=True))
top3_vendas_unidade = top_vendedor_unidade.groupby('Filial').head(3)
print('Aqui estão os vendedores top 3 de cada unidade:\n {}'.format(top3_vendas_unidade))




