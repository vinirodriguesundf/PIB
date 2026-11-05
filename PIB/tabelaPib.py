# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('Tabela PIB.csv',sep=';',skiprows=3,names=['Setor', 'Regiao', 'Trimestre', 'Valor'],encoding='utf-8')

df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
df_limpo = df.dropna(subset=['Trimestre', 'Valor']).copy()
df_limpo['Valor'] = df_limpo['Valor'].astype(int)

df_limpo['Ano'] = df_limpo['Trimestre'].str.extract(r'(\d{4})')
df_limpo['Trim_Num'] = df_limpo['Trimestre'].str.extract(r'(\d)º')
df_limpo['Trimestre_Curto'] = df_limpo['Ano'] + ' T' + df_limpo['Trim_Num']

tabela_trimestral = df_limpo.pivot_table(
    index='Setor',
    columns='Trimestre_Curto',
    values='Valor',
    aggfunc='sum',
    sort=False)

tabela_trimestral_visivel = tabela_trimestral.apply(
    lambda col: col.map(lambda x: f"{x:,.0f}".replace(",", ".")))

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print(tabela_trimestral_visivel)
