import pandas as pd
import sqlite3
from colunas import loja_columns , produto_columns


def posicionar_colunas(df) -> pd.DataFrame:
    df = df.iloc[:, :9]

    df = df.loc[2:].reset_index(drop=True)

    df = df.drop(df.columns[0],axis=1)

    return df

def tratando_nulos(df) -> pd.DataFrame:
    for coluna in df.columns:
        df[coluna] = df[coluna].replace({'-': None}, inplace=False)

    return df

conn = sqlite3.connect('cotton_baby.db')


#tratando lojas com promotor
df_p = pd.read_excel('BASE PESQUISA DE PREÇO.xlsx' , sheet_name='LOJAS COM PROMOTOR', )

df_p = posicionar_colunas(df_p)

df_p.columns = loja_columns

df_p = tratando_nulos(df_p)

df_p['is_client'] = True

#df_p.to_excel('teste.xlsx', index=False)

#tratando lojas não cliente

df_nc = pd.read_excel('BASE PESQUISA DE PREÇO.xlsx' , sheet_name='LOJAS NÃO CLIENTES ')

df_nc = posicionar_colunas(df_nc)

df_nc = tratando_nulos(df_nc)

df_nc['agencia'] = None
df_nc['cod_loja_gm'] = None


df_nc.columns = loja_columns

df_nc['is_client'] = False

df_nc = df_nc[df_p.columns]
#df_nc.to_excel('teste.xlsx',index=False)

df_lojas = pd.concat([df_p, df_nc], axis=0, ignore_index=True)

#df_lojas.to_excel('teste.xlsx',index=False)

df_lojas.to_sql('tbl_lojas', conn, if_exists='append', index=False)