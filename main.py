import streamlit as st
from utils.configs import set_options

st.set_page_config(page_title="Resumo de Vendas", layout="wide")

def main():
    set_options()
    
    with open('css/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    
    produtos = st.Page(
        page='pages/produtos.py',
        default=True,
        title='Produtos e Estoque'
    )
    clientes = st.Page(
        page='pages/contatos.py',
        title='Página de Clientes'
    )
    carrinhos = st.Page(
        page='pages/carrinhos.py',
        title='Carrinhos Ativos'
    )
    vendas = st.Page(
        page='pages/vendas.py',
        title='Vendas'
    )
    materiais = st.Page(
        page='pages/materiais.py',
        title='Materiais'
    )
    producao = st.Page(
        page='pages/producao.py',
        title='Produção'
    )
    gastos = st.Page(
        page='pages/gastos.py',
        title='Gastos'
    )
    home = st.Page(
        page='pages/home.py',
        title='Página Inicial',
    )
    
    configuracoes = st.Page(
        page='pages/configs.py',
        title='Configurações',
    )
    pg = st.navigation(
        {
            "Inicio": [home, configuracoes],
            "Vendas": [produtos, clientes, carrinhos, vendas],
            "Materiais": [materiais, producao, gastos],
        }
    )
    pg.run()

if __name__ == "__main__":
    #init_db()
    #print("Banco de dados inicializado.")
    main()
    
    