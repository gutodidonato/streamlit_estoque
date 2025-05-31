import streamlit as st



def main():
    st.title("Produzidos")
    st.markdown("Gerencie os produtos produzidos e seus detalhes.")
    st.markdown("### Lista de Produtos Produzidos")
    produtos_produzidos = {
        'produto1': {'nome': 'Camiseta Personalizada', 'quantidade': 100, 'custo': 500.00, 'data': '2023-10-01'},
        'produto2': {'nome': 'Caneca Personalizada', 'quantidade': 200, 'custo': 300.00, 'data': '2023-10-02'},
        'produto3': {'nome': 'Chaveiro Personalizado', 'quantidade': 150, 'custo': 150.00, 'data': '2023-10-03'}
    }
    for produto, info in produtos_produzidos.items():
        with st.expander(f"Produto: {info['nome']} - {info['data']}"):
            st.write(f"Quantidade Produzida: {info['quantidade']}")
            st.write(f"Custo Total: R$ {info['custo']:.2f}")
            st.write(f"Data de Produção: {info['data']}")
            if st.button("Remover Produto", key=produto):
                st.warning(f"Produto {info['nome']} removido.")
                st.rerun()
main()