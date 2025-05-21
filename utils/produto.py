import streamlit as st

def gerenciamento_produtos():
    with st.expander(label="Produto"):
        st.write("Categoria: Fruta")
        my_bar = st.progress(80, text="Estoque: 33")
        status_gerenciamento(30, 33, 35)





def status_gerenciamento(qtd, qtd_alerta, qtd_maxima):
    if qtd > qtd_maxima:
        st.warning(f"Estamos além do estoque máximo, quantidade: {qtd}")
    elif qtd < qtd_maxima and qtd > qtd_alerta:
        st.success(f"Estoque normal, quantidade: {qtd}") 
    else:
        st.warning(f"Estamos com pouco estoque")
        st.warning(f"Estoque: {qtd} - estoque maximo: {qtd_maxima} - estoque alerta : {qtd_alerta}")