# Ex02
import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_excel('Desafio - Time de Projetos e Dados.xlsx', sheet_name='Dados - Questão 1')



# Encontrando a quantidade de CPF's na nota
contagem_CPF = tabela['CPF NA NOTA?'].value_counts()

print('---'*20)
print('A quantidade total de pessoas que colocaram o CPF na nota \n {}'.format(contagem_CPF))



# Calculando a %
total_de_registros = contagem_CPF.sum()
cpf_sim = (contagem_CPF['Sim'] / total_de_registros) * 100
cpf_não = (contagem_CPF['Na~o'] / total_de_registros) * 100

print('---'*20)
print('Porcentagem de CPF na nota {:.2f}%'.format(cpf_sim))
print('Porcentagem sem CPF na nota {:.2f}%'.format(cpf_não))



# Criando um gráfico de pizza
labels = ['Sim', 'Não']
sizes = [cpf_sim, cpf_não]
color = ['green', 'blue']
explode = (0.1, 0)

plt.figure(figsize=(4,4))
plt.pie(sizes, explode = explode, labels=labels, colors=color, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Porcentagem de CPF na nota')
plt.axis('equal')
plt.show()
