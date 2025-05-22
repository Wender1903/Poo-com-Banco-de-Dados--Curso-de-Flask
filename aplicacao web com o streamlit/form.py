import streamlit as st
import dadosofc

st.title("Séries")

nome = st.text_input("Nome da Série")
ano = st.number_input("Ano de Lançamento da Série", min_value=1990, max_value=2025)
nota = st.slider("Nota da Série", min_value=0.0, max_value=10.0)

if st.button('Adicionar'):
    dadosofc.inserir_dados(nome, ano, nota)
    st.success("Série Cadastrada com Sucesso")

series = dadosofc.obter_dados()
st.header("Lista de Séries Cadastradas")
st.table(series)