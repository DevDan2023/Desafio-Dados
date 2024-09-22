# Ex01
import pandas as pd
import matplotlib.pyplot as plt
import locale

tabela = pd.read_excel('Desafio - Time de Projetos e Dados.xlsx', sheet_name='Dados - Questão 1')
tabela = tabela[tabela['Filial'] !=0]
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


# Descobrindo o valor total de vendas da empresa
total_de_vendas_da_empresa = tabela['valor_compra'].sum()
total_de_vendas_da_empresa_formatado = locale.currency(total_de_vendas_da_empresa, grouping=True)
print("O total de vendas da empresa foi de R${}".format(total_de_vendas_da_empresa_formatado))
print("---"*20)



# Descobrindo o valor total dos impostos 
imposto_total = tabela['Imposto'].sum()
imposto_total_formatado = locale.currency(imposto_total, grouping=True)
print("O valor total de impostos a ser pago será de {}".format(imposto_total_formatado))
print("---" * 20)



# Descobrindo qual loja mais vendeu
total_de_vendas_unidade = tabela.groupby('Filial')['valor_compra'].sum()
total_de_vendas_unidade_formatado = total_de_vendas_unidade.apply(lambda x: locale.currency(x, grouping=True))
print("O valor total de vendas por unidade foi de \n{}".format(total_de_vendas_unidade_formatado))
print('---'*20)



# Cores
cor1="blue"
cor2="purple"
cor3="green"
cor4="yellow"
cor5="black"
cor6="Lightblue"

# Criando um gráfico de barras para visualizar a loja que mais vendeu
plt.figure(figsize=(5,3))
bars =plt.bar(range(len(total_de_vendas_unidade.index)), total_de_vendas_unidade, color=[cor1, cor2, cor3, cor4, cor5, cor6])
# Adicionando os valores nas barras
for bar, valor in zip(bars, total_de_vendas_unidade):
    plt.text(bar.get_x() + bar.get_width(), bar.get_height(), locale.currency(valor, grouping=True), ha='center', va='bottom', fontsize=8 )
plt.xlabel('Loja')
plt.ylabel('Valor de Vendas (R$)')
plt.title('Total de vendas por Loja')
plt.xticks(range(len(total_de_vendas_unidade)), total_de_vendas_unidade.index, fontsize=5)
plt.show()

