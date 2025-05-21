import streamlit as st 
from utils.produto import gerenciamento_produtos

st.title("Produtos e Estoque")

tab1, tab2, tab3 = st.tabs(['Produtos Disponíveis', 'Adicionar Produtos', 'Gerenciamento de Estoque'])
with tab1:
    gerenciamento_produtos()
with tab2:
    pass
with tab3:
    pass
