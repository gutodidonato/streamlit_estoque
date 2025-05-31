import streamlit as st

def gerenciamento_produtos():    
    with st.expander(label="Produto"):
        col1, col2 = st.columns(2)
        with col1:
            st.write("Categoria: Fruta") 
            st.write("Preço: R$ 5,00") 
            
        
            st.write("Preço de custo: R$ 3,00")
            descricao_produto( )
        with col2:
            st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        if st.session_state.get('estoque', False):
            barra_progresso(30, 33)
            status_gerenciamento(34, 33, 35)
        

    
        
def descricao_produto():
    st.text_area("Descrição do produto",
                 "Descrição do produto: Fruta, sabor doce, cor amarela, tamanho médio, peso 1kg",
)

    
def barra_progresso(qtd, qtd_maxima):
    col1, col2 = st.columns(2)
    with col1:
        st.write("Quantidade em estoque: ", qtd)
    with col2:
        st.write("Quantidade máxima: ", qtd_maxima)
    progresso = int((qtd / qtd_maxima) * 100)
    bar = st.progress(progresso, text=f"Estoque: {qtd}")
    return bar 

def status_gerenciamento(qtd, qtd_alerta, qtd_maxima):
    if qtd > qtd_maxima:
        st.warning(f"Estamos além do estoque máximo, quantidade: {qtd}")
        st.warning(f"Estoque: {qtd} - estoque maximo: {qtd_maxima} - estoque alerta : {qtd_alerta}")
    elif qtd < qtd_maxima and qtd > qtd_alerta:
        st.success(f"Estoque normal, quantidade: {qtd}") 
        st.success(f"Estoque: {qtd} - estoque maximo: {qtd_maxima} - estoque alerta : {qtd_alerta}")
    else:
        st.warning(f"Estamos com pouco estoque")
        st.warning(f"Estoque: {qtd} - estoque maximo: {qtd_maxima} - estoque alerta : {qtd_alerta}")