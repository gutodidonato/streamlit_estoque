import streamlit as st


def main():
    st.title("Gastos e Despesas")
    st.markdown("Gerencie seus gastos e despesas de forma eficiente.")
    st.markdown("---")
    st.subheader("Valor gasto: :rainbow[R$ 4300.00]")
    st.markdown("---")
    st.subheader("Lista de Gastos")
    gastos = {
        'gasto1': {'descricao': 'Compra de Materiais', 'valor': 1500.00, 'data': '2023-10-01'},
        'gasto2': {'descricao': 'Pagamento de Fornecedores', 'valor': 2000.00, 'data': '2023-10-02'},
        'gasto3': {'descricao': 'Despesas Operacionais', 'valor': 800.00, 'data': '2023-10-03'}
    }
    
    for gasto, info in gastos.items():
        with st.expander(f"Gasto: {info['descricao']} - {info['data']}"):
            st.write(f"Valor: R$ {info['valor']:.2f}")
            if st.button("Remover Gasto", key=gasto):
                st.warning(f"Gasto {info['descricao']} removido.")
                st.rerun()
    if st.button("Adicionar Gasto"):
        descricao = st.text_input("Descrição do Gasto")
        valor = st.number_input("Valor do Gasto", min_value=0.0, format="%.2f")
        data = st.date_input("Data do Gasto")
        
        if st.button("Salvar"):
            if descricao and valor > 0:
                novo_gasto = {'descricao': descricao, 'valor': valor, 'data': data.strftime('%Y-%m-%d')}
                gastos[f'gasto{len(gastos) + 1}'] = novo_gasto
                st.success(f"Gasto '{descricao}' adicionado com sucesso!")
                st.rerun()
            else:
                st.error("Por favor, preencha todos os campos corretamente.")
main()        