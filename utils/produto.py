import streamlit as st
import time

def gerenciamento_produtos():    
    categoria = st.selectbox("Selecione a categoria do produto",
                            ["Frutas", "Legumes", "Bebidas", "Doces", "Outros"])
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
        

def adicionar_produto():
    st.write("Adicionar produto")
    nome_produto = st.text_input("Nome do produto")
    categoria_produto = st.selectbox("Categoria do produto", ["Frutas", "Legumes", "Bebidas", "Doces", "Outros"])
    preco_produto = st.number_input("Preço do produto", min_value=0.0, format="%.2f")
    quantidade_produto = st.number_input("Quantidade do produto", min_value=0, step=1)
    
    if st.button("Adicionar"):
        st.success(f"Produto {nome_produto} adicionado com sucesso!")
        time.sleep(3)
        st.rerun()

def editar_produto():
    categoria = st.selectbox("Selecione a categoria do produto", key="categoria_produto",
                            options=["Frutas", "Legumes", "Bebidas", "Doces", "Outros"])
    with st.expander(label="Produto"):
        st.write("Categoria: Fruta")
        st.write("Preço: R$ 5,00")
        st.write("Preço de custo: R$ 3,00")
        st.text_area("Descrição do produto",
                     "Descrição do produto: Fruta, sabor doce, cor amarela, tamanho médio, peso 1kg", key="descricao_produto",)
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        if st.session_state.get('estoque', False):
            barra_progresso(30, 33)
            status_gerenciamento(34, 33, 35)
    if st.button("Editar Produto"):
        st.write("Editar produto")
        nome_produto = st.text_input("Nome do produto")
        categoria_produto = st.selectbox("Categoria do produto", ["Frutas", "Legumes", "Bebidas", "Doces", "Outros"])
        preco_produto = st.number_input("Preço do produto", min_value=0.0, format="%.2f")
        quantidade_produto = st.number_input("Quantidade do produto", min_value=0, step=1)
        
        if st.button("Salvar Alterações"):
            st.success(f"Produto {nome_produto} editado com sucesso!")
            time.sleep(3)
            st.rerun()   
            
def buscar_produto():
    st.write("Buscar produto")
    nome_produto = st.text_input("Nome do produto ou parte do nome")
    if nome_produto:
        with st.expander(label="Produto"):
            st.write("Categoria: Fruta")
            st.write("Preço: R$ 5,00")
            st.write("Preço de custo: R$ 3,00")
            st.text_area("Descrição do produto",
                         "Descrição do produto: Fruta, sabor doce, cor amarela, tamanho médio, peso 1kg", key="descricao_produto_buscar")
            st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
            if st.session_state.get('estoque', False):
                barra_progresso(30, 33)
                status_gerenciamento(34, 33, 35)