import streamlit as st
import pandas as pd

# CSS personalizado para estilização
with open("cotton.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# Título principal com estilo
st.markdown('<p class="titulo">Qual sua agência?</p>', unsafe_allow_html=True)

# Lista de opções para as caixas de seleção
opcoesAg = ['----', 'agencia 1', 'agencia 2', 'agencia 3', 'agencia 4']
opcoesPrd = ['----', 'cotonete', 'fralda', 'algodão']
opcoesConc = ['----', 'concorrente 1', 'concorrente 2', 'concorrente 3', 'concorrente 4']

selecaoPrd = None
# funções

# Botão
def botao():
    if st.button('Submit'):
        # Validação: Verifica se algo foi selecionado antes de enviar
        if (selecaoAg and selecaoPrd != '----') and (selecaoAg is not None and selecaoPrd is not None):
            st.success(f'Você selecionou {selecaoAg} e o produto {selecaoPrd}.O preço {preco}')
        else:
            st.error('Por favor, selecione uma agência e um produto antes de submeter.')

def Produto():
    selecaoPrd = st.selectbox(
        'Escolha um produto:',
        opcoesPrd
    )
    return selecaoPrd

def Concorrente():
    selecaoConc = st.selectbox(
        'Qual a marca deste produto?:',
        opcoesConc
    )
    return selecaoConc

def Preco():
    st.write(f"Digite o preço do produto {selecaoPrd}")
    str_preco = st.text_input("",key='input_number',placeholder='0,00')

    preco = float(str_preco)

    return str_preco

def clear_inputs():
    st.session_state['input_number'] = 0
if 'input_number' not in st.session_state:
    st.session_state['input_number'] = 0

def reset_number():
    st.session_state['input_number'] = 0


# Caixa de seleção da agência
selecaoAg = st.selectbox(
    'Escolha uma agência:',  # Texto que aparece acima da select box
    opcoesAg  # Lista de opções
)

# Estrutura condicional para cada seleção de agência
if selecaoAg == 'agencia 1':
    st.markdown('<p class="subtitulo">Seja bem-vindo agência 1!</p>', unsafe_allow_html=True)
    st.markdown('<p class="texto">Qual produto deseja escolher?</p>', unsafe_allow_html=True)
    selecaoPrd = Produto()
    selecaoConc = Concorrente()
    preco = Preco()
    submit = botao()

elif selecaoAg == 'agencia 2':
    st.markdown('<p class="subtitulo">Seja bem-vindo agência 2!</p>', unsafe_allow_html=True)
    st.markdown('<p class="texto">Qual produto deseja escolher?</p>', unsafe_allow_html=True)
    selecaoPrd = Produto()
    selecaoConc = Concorrente()
    preco = Preco()
    submit = botao()

elif selecaoAg == '----':
    st.write()
else:
    st.markdown('<p class="texto">Não reconhecido.</p>', unsafe_allow_html=True)
