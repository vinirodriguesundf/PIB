import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


def tabela_pib():

    df = pd.read_csv('Tabela PIB.csv', sep=';', skiprows=3, names=['Setor', 'Regiao', 'Trimestre', 'Valor'], encoding='utf-8')

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
        sort=False
    )

    tabela_trimestral_visivel = tabela_trimestral.apply(
        lambda col: col.map(lambda x: f"{x:,.0f}".replace(",", "."))
    )

    return tabela_trimestral_visivel


def soma_ano():

    df = pd.read_csv('Tabela PIB.csv', sep=';', skiprows=3, names=['Setor', 'Regiao', 'Trimestre', 'Valor'], encoding='utf-8')

    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df_limpo = df.dropna(subset=['Trimestre', 'Valor']).copy()
    df_limpo['Valor'] = df_limpo['Valor'].astype(int)

    df_limpo['Ano'] = df_limpo['Trimestre'].str.extract(r'(\d{4})').astype(int)

    tabela_ano = df_limpo.pivot_table(
        index='Setor',
        columns='Ano',
        values='Valor',
        aggfunc='sum',
        sort=False
    )

    tabela_ano = tabela_ano.apply(
        lambda col: col.map(lambda x: f"{x:,.0f}".replace(",", "."))
    )

    return tabela_ano


def soma_4t():

    df = pd.read_csv('Tabela PIB.csv', sep=';', skiprows=3, names=['Setor', 'Regiao', 'Trimestre', 'Valor'], encoding='utf-8')
    df = df.drop(columns=['Regiao'])

    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df_limpo = df.dropna(subset=['Trimestre', 'Valor']).copy()
    df_limpo['Valor'] = df_limpo['Valor'].astype(int)

    df_limpo['Ano'] = df_limpo['Trimestre'].str.extract(r'(\d{4})').astype(int)
    df_limpo['Trim_Num'] = df_limpo['Trimestre'].str.extract(r'(\d)º').astype(int)

    df_limpo['Ano_Inicio'] = df_limpo['Ano'] - df_limpo['Trim_Num'].isin([1, 2]).astype(int)
    df_limpo['Soma_4T'] = (
        df_limpo['Ano_Inicio'].astype(str) + '/' + (df_limpo['Ano_Inicio'] + 1).astype(str)
    )

    contagem = df_limpo.groupby('Soma_4T')['Trimestre'].nunique()
    periodos_completos = contagem[contagem == 4].index
    df_4t = df_limpo[df_limpo['Soma_4T'].isin(periodos_completos)].copy()

    tabela_4t = df_4t.pivot_table(
        index='Setor',
        columns='Soma_4T',
        values='Valor',
        aggfunc='sum',
        sort=False
    )

    tabela_4t_visivel = tabela_4t.apply(
        lambda col: col.map(lambda x: f"{x:,.0f}".replace(",", "."))
    )

    return tabela_4t_visivel


def diferenca_semestres():

    df = pd.read_csv('Tabela PIB.csv', sep=';', skiprows=3, names=['Setor', 'Regiao', 'Trimestre', 'Valor'], encoding='utf-8')

    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df_limpo = df.dropna(subset=['Trimestre', 'Valor']).copy()
    df_limpo['Valor'] = df_limpo['Valor'].astype(int)

    df_limpo['Ano'] = df_limpo['Trimestre'].str.extract(r'(\d{4})')
    df_limpo['Trim_Num'] = df_limpo['Trimestre'].str.extract(r'(\d)º')

    df_1sem = df_limpo[df_limpo['Trim_Num'].isin(['1', '2'])].copy()

    tabela_semestral = df_1sem.pivot_table(
        index='Setor',
        columns='Ano',
        values='Valor',
        aggfunc='sum',
        sort=False
    )

    anos_anteriores = [col for col in tabela_semestral.columns if col != '2026']
    tabela_dif_sem = tabela_semestral[anos_anteriores].apply(lambda col: tabela_semestral['2026'] - col)

    tabela_dif_sem.columns = [f"26-{ano}" for ano in anos_anteriores]
    tabela_dif_sem['2026(1ºS)'] = tabela_semestral['2026']

    tabela_dif_sem_visivel = tabela_dif_sem.apply(
        lambda col: col.map(lambda x: f"{x:,.0f}".replace(",", "."))
    )

    return tabela_dif_sem_visivel
