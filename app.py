import streamlit as st
import bd_worker as bw
import func as func

# CSS personalizado para estilização
with open("cotton.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# Título principal com estilo
st.markdown('<p class="titulo">Qual sua agência?</p>', unsafe_allow_html=True)

# Lista de opções padrão
default = "----"
placeholder = [default]
opcoesAg = bw.bd_lista_agencia()  # Função que lista todas as agências
exibAg = placeholder + opcoesAg

# Caixa de seleção da agência
selecaoAg = st.selectbox(
    'Escolha uma agência:',
    exibAg
)

# Se uma agência for selecionada, carrega as redes associadas
if selecaoAg != default:
    st.markdown('<p class="subtitulo">Selecione a rede associada à agência.</p>', unsafe_allow_html=True)
    opcoesRede = bw.bd_pesquisa_rede(selecaoAg)  # Consulta filtrada pela agência
    exibRede = placeholder + opcoesRede
    selecaoRede = st.selectbox('Escolha uma rede:', exibRede)

    # Se uma rede for selecionada, carrega os estados associados
    if selecaoRede != default:
        st.markdown('<p class="subtitulo">Selecione o estado associado à rede.</p>', unsafe_allow_html=True)
        opcoesEst = bw.bd_pesquisa_uf(selecaoAg, selecaoRede)  # Consulta filtrada pela agência e rede
        exibEst = placeholder + opcoesEst
        selecaoEst = st.selectbox('Escolha um estado:', exibEst)

        # Se um estado for selecionado, carrega as cidades associadas
        if selecaoEst != default:
            st.markdown('<p class="subtitulo">Selecione a cidade associada ao estado.</p>', unsafe_allow_html=True)
            opcoesCid = bw.bd_pesquisa_cidade(selecaoAg, selecaoRede,
                                              selecaoEst)  # Consulta filtrada pela agência, rede e estado
            exibCid = placeholder + opcoesCid
            selecaoCid = st.selectbox('Escolha uma cidade:', exibCid)

            # Se uma cidade for selecionada, carrega os endereços associados
            if selecaoCid != default:
                st.markdown('<p class="subtitulo">Selecione o endereço associado à cidade.</p>', unsafe_allow_html=True)
                opcoesEnd = bw.bd_pesquisa_endereco(selecaoAg, selecaoRede, selecaoEst,
                                                    selecaoCid).values()  # Consulta filtrada pela agência, rede, estado e cidade
                exibEnd = opcoesEnd
                selecaoEnd = st.selectbox('Escolha um endereço:', exibEnd)

                # Se um endereço for selecionado, carrega os produtos associados
                if selecaoEnd != default:
                    st.markdown('<p class="subtitulo">Selecione o produto associado ao endereço.</p>',
                                unsafe_allow_html=True)
                    opcoesPrd = bw.bd_produto()  # Consulta filtrada pela agência, rede, estado, cidade e endereço
                    exibPrd = placeholder + opcoesPrd
                    selecaoPrd = st.selectbox('Escolha um produto:', exibPrd)

                    # Se um produto for selecionado, carrega os concorrentes associados
                    if selecaoPrd != default:
                        st.markdown('<p class="subtitulo">Preço Cotton.</p>', unsafe_allow_html=True)
                        precoCotton = st.number_input("", key='cotton', placeholder='0,00')
                        st.markdown('<p class="subtitulo">Selecione o concorrente associado ao produto.</p>',
                                    unsafe_allow_html=True)
                        opcoesConc = bw.bd_concorrentes(
                            selecaoPrd)  # Consulta filtrada pela agência, rede, estado, cidade, endereço e produto
                        exibConc = placeholder + opcoesConc
                        selecaoConc = st.selectbox('Escolha um concorrente:', exibConc)

                        # Se um concorrente for selecionado, permite a entrada de preço
                        if selecaoConc != default:
                            st.write(f'<p class="subtitulo">Preço concorrente {selecaoConc}.</p>',
                                     unsafe_allow_html=True)
                            preco = st.number_input("", key='concorrente', placeholder='0,00')

                            st.warning("Lembre-se de verificar se todos os dados estão preenchidos corretamente")
                            func.botao(selecaoConc, selecaoPrd, preco)

