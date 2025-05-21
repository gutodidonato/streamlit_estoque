import streamlit as st


def main():
    st.markdown("""
    <style>
        .st-emotion-cache-1qv137k {
            background: #ff0000;
            padding: 10px;
            color: #ffffff;
            text-align: center;
            margin: 30px 30px;
        }
    </style>
""", unsafe_allow_html=True)
    
    
    produtos = st.Page(
        page='pages/produtos.py',
        default=True,
        title='Produtos e Estoque'
    )
    clientes = st.Page(
        page='pages/vendas.py',
        title='Página de Clientes'
    )
    carrinhos = st.Page(
        page='pages/carrinhos.py',
        title='Carrinhos Ativos'
    )
    vendas = st.Page(
        page='pages/estoques.py',
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
    
    configuracoes = st.Page(
        page='pages/configs.py',
        title='Configurações',
    )
    pg = st.navigation(
        {
            "Vendas": [produtos, clientes, carrinhos, vendas],
            "Materiais": [materiais, producao, gastos],
            "Configurações": [configuracoes],
        }
    )
    pg.run()

if __name__ == "__main__":
    #init_db()
    #print("Banco de dados inicializado.")
    main()
    
    