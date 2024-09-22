import streamlit as st

with open("cotton.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# Função do botão
def botao(selecaoConc, selecaoPrd, preco):
    if st.button('Submit'):  # Aqui deve estar o botão final de envio
        # Validação: Verifica se algo foi selecionado antes de enviar
        if preco is not None:
            st.success(f'Você definiu o produto ( {selecaoPrd} ) da marca ( {selecaoConc} ) com o preço: ( {preco} )')
        else:
            st.error('Por favor, insira todas as opções corretamente.')


def Redes(exibRede):
    selecaoRede = st.selectbox(
        'Selecione uma rede',
        exibRede
    )
    return selecaoRede

def Estados(exibEst):
    selecaoEst = st.selectbox(
        'Selecione um estado',
        exibEst
    )
    return selecaoEst

def Cidades(exibCid):
    selecaoCid = st.selectbox(
        'Selecione uma cidade',
        exibCid
    )
    return selecaoCid

def Endereco(exibEnd):
    selecaoEnd = st.selectbox(
        'Selecione o endereço da loja desejada',
        exibEnd
    )
    return selecaoEnd

# Função de seleção de produto
def Produto(exibPrd):
    selecaoPrd = st.selectbox(
        'Escolha um produto:',
        exibPrd
    )
    return selecaoPrd

# Função de seleção de concorrente
def Concorrente(exibConc):
    selecaoConc = st.selectbox(
        'Qual a marca deste produto?:',
        exibConc
    )
    return selecaoConc

# Função para entrada de preço
def Preco(selecaoPrd):
    st.write(f"Digite o preço do produto {selecaoPrd}")
    preco = st.number_input("",key='concorrente',placeholder='0,00')
    return preco
