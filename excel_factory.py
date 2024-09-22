import openpyxl
import sqlite3
from pandas import DataFrame
import bd_worker as bd

workbook = openpyxl.Workbook()

sheet = workbook.active

def build_agencia() -> DataFrame:

    tbl_agencias = DataFrame(bd.bd_tbl_agencias(),columns=['GERENTE', 'SUPERVISOR', 'AGÊNCIA', 'REDE', 'ENDEREÇO', 'CIDADE' , 'UF'])

    return tbl_agencias
def build_excel_file(produto='---'):
    produtos_ordem = bd.bd_produto()

    df_agencia = build_agencia()

    if produto == '---':
        pass

    else:
        pass