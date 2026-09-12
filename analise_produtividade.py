"""
Análise exploratória de dados de produtividade.

Projeto originalmente desenvolvido para uma disciplina de Ciência de Dados
e posteriormente organizado como projeto de portfólio.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


url = 'https://raw.githubusercontent.com/cibelerusso/Datasets/main/DadoseDecisoes.csv'

df = pd.read_csv(url)

# Criação da variável binária de produtividade com base na mediana.
mediana = df['Produtividade'].median()
df['Produtividade_bin'] = np.where(df['Produtividade'] > mediana, 1, 0)

# Tabelas de frequência das variáveis qualitativas.
print("Tabela de Frequência para Gênero:")
print(df['Gênero'].value_counts().to_frame())

print("\nTabela de Frequência para Departamento:")
print(df['Departamento'].value_counts().to_frame())

print("\nTabela de Frequência para Home_Office:")
print(df['Home_Office'].value_counts().to_frame())

print("\nTabela de Frequência para Produtividade_bin:")
print(df['Produtividade_bin'].value_counts().to_frame())

# Gráficos de barras para as variáveis qualitativas.
qualitativas = ['Gênero', 'Departamento', 'Home_Office', 'Produtividade_bin']

for variavel in qualitativas:
    plt.figure(figsize=(7, 5))
    sns.countplot(data=df, x=variavel, hue=variavel, legend=False)
    plt.title(f'Distribuição de {variavel}')
    plt.xlabel(variavel)
    plt.ylabel('Frequência')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Boxplots para variáveis quantitativas.
quantitativas = [
    'Idade',
    'Salário',
    'Horas_Trabalhadas',
    'Produtividade',
    'Satisfação',
    'Tempo_Empresa',
    'Cursos_Realizados'
]

for variavel in quantitativas:
    plt.figure(figsize=(7, 5))
    sns.boxplot(data=df, y=variavel)
    plt.title(f'Boxplot de {variavel}')
    plt.tight_layout()
    plt.show()

# Tabelas de contingência e proporções.
print("\nDepartamento x Produtividade_bin:")
tabela = pd.crosstab(df['Departamento'], df['Produtividade_bin'])
print(tabela)

print("\nProporções de produtividade por departamento (%):")
proporcoes = pd.crosstab(
    df['Departamento'],
    df['Produtividade_bin'],
    normalize='index'
) * 100
print(proporcoes)

# Exploração adicional da relação entre variáveis e produtividade.
print("\nDepartamento x Home_Office:")
print(pd.crosstab(df['Departamento'], df['Home_Office']))

print("\nDepartamento x Cursos_Realizados:")
print(pd.crosstab(df['Departamento'], df['Cursos_Realizados']))

print("\nProdutividade média por departamento:")
print(df.groupby('Departamento')['Produtividade'].mean().sort_values(ascending=False))

print("\nProdutividade média por Home_Office:")
print(df.groupby('Home_Office')['Produtividade'].mean().sort_values(ascending=False))
