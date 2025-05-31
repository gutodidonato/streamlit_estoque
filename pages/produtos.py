import streamlit as st 
from utils.produto import gerenciamento_produtos, adicionar_produto, editar_produto, buscar_produto

st.title("Produtos e Estoque")

tab1, tab2, tab3, tab4 = st.tabs(['Produtos Disponíveis', 'Adicionar Produtos', 'Edição de Produtos', 'Busca de Produtos'])
with tab1:
    gerenciamento_produtos()
with tab2:
    adicionar_produto()
with tab3:
    editar_produto()
with tab4:
    buscar_produto()
