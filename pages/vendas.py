import streamlit as st

def main():
    st.title("📊 Vendas")
    st.markdown("Gerencie suas vendas e acompanhe o desempenho do seu negócio.")
    st.subheader("Resumo de Vendas")
    vendas = {
        'venda1' : {'produtos': [{'nome': 'Camiseta', 'quantidade': 10, 'valor': 150.00}, {'nome': 'Perfume', 'quantidade': 30, 'valor': 300.00}]},
        'venda2' : {'produtos': [{'nome': 'Tênis', 'quantidade': 5, 'valor': 500.00}, {'nome': 'Relógio', 'quantidade': 2, 'valor': 2000.00}]},
        'venda3' : {'produtos': [{'nome': 'Calça Jeans', 'quantidade': 8, 'valor': 800.00}, {'nome': 'Mochila', 'quantidade': 4, 'valor': 400.00}]}
    }
    for venda, info in vendas.items():
        with st.expander(f"Venda: {venda}"):
            for produto in info['produtos']:
                st.write(f"Produto: {produto['nome']}, Quantidade: {produto['quantidade']}, Valor Total: R$ {produto['valor']:.2f}")
            if st.button("Remover Venda", key=venda):
                st.warning(f"Venda {venda} removida.")
                st.rerun()
                
main()