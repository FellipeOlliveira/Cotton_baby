import sqlite3
from pandas import read_excel


def bd_tbl_agencias():
    connection = sqlite3.connect('cotton_baby.db')
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT GERENTE, SUPERVISOR, AGÊNCIA, REDE, ENDEREÇO, CIDADE , UF 
        FROM tbl_lojas
        """)

    tbl = cursor.fetchall()

    # Mostrar o resultado
    # print(lista_de_estados)
    cursor.close()
    connection.close()
    return tbl
def bd_lista_agencia() -> list:
    connection = sqlite3.connect('cotton_baby.db')
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM vw_agencias
        """)

    ufs = cursor.fetchall()

    # Converter para lista de strings
    lista_de_estados = [estado[0] for estado in ufs]

    # Mostrar o resultado
    #print(lista_de_estados)
    cursor.close()
    connection.close()
    return lista_de_estados

def bd_pesquisa_rede(agencia:str) -> list:
    connection = sqlite3.connect('cotton_baby.db')
    cursor = connection.cursor()

    cursor.execute(
        f"""
        SELECT DISTINCT REDE FROM tbl_lojas
        WHERE AGÊNCIA = "{agencia}"
        """)

    redes = cursor.fetchall()

    lista_de_redes = [rede[0] for rede in redes]

    cursor.close()
    connection.close()
    return lista_de_redes

def bd_pesquisa_uf(agencia:str,rede:str) -> list:
    connection = sqlite3.connect('cotton_baby.db')
    cursor = connection.cursor()

    cursor.execute(
        f"""
            SELECT  DISTINCT uf FROM tbl_lojas
            WHERE AGÊNCIA = "{agencia}"
            AND
            REDE = "{rede}"
            """)

    ufs = cursor.fetchall()

    lista_de_ufs = [uf[0] for uf in ufs]

    cursor.close()
    connection.close()
    return lista_de_ufs

def bd_pesquisa_cidade(agencia:str,rede:str,uf:str) -> list:
    connection = sqlite3.connect('cotton_baby.db')
    cursor = connection.cursor()

    cursor.execute(
        f"""
                SELECT DISTINCT CIDADE FROM tbl_lojas
                WHERE AGÊNCIA = "{agencia}"
                AND
                REDE = "{rede}"
                AND
                UF = "{uf}"
                """)

    cidades = cursor.fetchall()

    lista_de_cidades = [cidade[0] for cidade in cidades]

    cursor.close()
    connection.close()
    return lista_de_cidades

def bd_pesquisa_endereco(agencia:str,rede:str,uf:str,cidade:str)-> dict:
    connection = sqlite3.connect('cotton_baby.db')
    cursor = connection.cursor()

    cursor.execute(
        f"""
            SELECT [cod loja], ENDEREÇO FROM tbl_lojas
            WHERE AGÊNCIA = "{agencia}"
            AND
            REDE = "{rede}"
            AND
            UF = "{uf}"
            AND
            CIDADE = "{cidade}"
        """)

    enderecos = cursor.fetchall()

    lista_de_enderecos = {endereco[0]:endereco[1] for endereco in enderecos}

    cursor.close()
    connection.close()
    return lista_de_enderecos

def bd_produto() -> list:
    connection = sqlite3.connect('cotton_baby.db')
    cursor = connection.cursor()

    cursor.execute(
        f"""
            SELECT * FROM TBL_PRODUTOS
        """)

    produtos = cursor.fetchall()

    lista_de_produtoss = [produto[1] for produto in produtos]

    cursor.close()
    connection.close()
    return lista_de_produtoss

def bd_concorrentes(produto:str) -> list:
    connection = sqlite3.connect('cotton_baby.db')
    cursor = connection.cursor()

    cursor.execute(
        f"""
            SELECT [concorrente nome] FROM tbl_rel_produto_concorrente
            WHERE [produto nome] = "{produto}"
        """)

    concorrentes = cursor.fetchall()

    lista_de_concorrentes = [concorrente[0] for concorrente in concorrentes]

    cursor.close()
    connection.close()
    return lista_de_concorrentes


def bd_lista_cidades() -> list:
    connection = sqlite3.connect('cotton_baby.db')
    cursor = connection.cursor()

    cursor.execute(
        f"""
               SELECT DISTINCT CIDADE FROM tbl_lojas
           """)

    cidades = cursor.fetchall()

    lista_de_cidades = [cidade[0] for cidade in cidades]

    cursor.close()
    connection.close()
    return lista_de_cidades

def bd_lista_ufs() -> list:
    connection = sqlite3.connect('cotton_baby.db')
    cursor = connection.cursor()

    cursor.execute(
        f"""
               SELECT DISTINCT UF FROM tbl_lojas
           """)

    enderecos = cursor.fetchall()

    lista_de_enderecos = [endereco[0] for endereco in enderecos]

    cursor.close()
    connection.close()
    return lista_de_enderecos

def  bd_lista_enderecos() -> list:
    connection = sqlite3.connect('cotton_baby.db')
    cursor = connection.cursor()

    cursor.execute(
        f"""
                   SELECT  ENDERECOS FROM tbl_lojas
               """)

    cidades = cursor.fetchall()

    lista_de_cidades = [cidade[0] for cidade in cidades]

    cursor.close()
    connection.close()
    return lista_de_cidades

def bd_lista_concorrente() -> dict:
    connection = sqlite3.connect('cotton_baby.db')
    cursor = connection.cursor()

    cursor.execute(
        f"""
            SELECT * FROM tbl_concorrentes
        """)

    concorrentes = cursor.fetchall()

    lista_de_concorrentes = {concorrente[0]:concorrente[1] for concorrente in concorrentes}


    cursor.close()
    connection.close()
    return lista_de_concorrentes

def bd_insert_precos(cod_loja:str,loja_rede:str,loja_agencia:str,cod_produto:str,uf:str,cidade:str,cod_concorrente:str,concorrente_nome:str,preco:str) ->None:
    connection = sqlite3.connect('cotton_baby.db')
    cursor = connection.cursor()

    cursor.execute(
        f"""
        INSERT INTO tbl_rel_produto_concorrente
        (loja_cod,loja_rede,loja_agencia,cod_produto,uf,cidade,cod_concorrente,concorrente_nome,preco)
        VALUES
        (
        {cod_loja},
        "{loja_rede}",
        "{loja_agencia}",
        {cod_produto},
        "{uf}",
        "{cidade}",
        {cod_concorrente},
        "{concorrente_nome}",
        {preco}
        )""")

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    #print(bd_lista_agencia())

    agencia = 'BELKA PROMO'
    #print(bd_pesquisa_rede(agencia))

    rede = 'ATACADÃO'
    #print(bd_pesquisa_uf(agencia,rede))

    uf = 'RS'
    #print(bd_pesquisa_cidade(agencia,rede,uf))

    cidade = 'PORTO ALEGRE'
    #print(bd_pesquisa_endereco(agencia,rede,uf,cidade))

    #print(bd_produto())

    produto = 'ALGODÃO BOLA 50GR'
    #print(bd_lista_concorrente())
