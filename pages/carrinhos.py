import streamlit as st 


clientes = {'Pedro': {'nome' : 'Pedro', 'email': 'pedro@xpto.com'},
           'Maria': {'nome' : 'Maria', 'email': 'maria@xpto.com'}}


def gerenciamento_carrinhos():
    st.title("Gerenciamento de Carrinhos Ativos")
    
    if 'carrinhos' not in st.session_state:
        st.session_state['carrinhos'] = []
    
    if st.button("Adicionar Carrinho"):
        carrinho = {'cliente': ''}
        st.session_state['carrinhos'].append(carrinho)
    
    for i, carrinho in enumerate(st.session_state['carrinhos']):
        with st.expander(f"Carrinho {i + 1}"):
            cliente = st.selectbox("Cliente", list(clientes.keys()), key=f"cliente_{i}")
            carrinho['cliente'] = clientes[cliente]['nome']
            
            if st.button("Remover Carrinho", key=f"remover_{i}"):
                st.session_state['carrinhos'].pop(i)
                st.rerun()
    
    if st.session_state['carrinhos']:
        st.write("Carrinhos Ativos:")
        for c in st.session_state['carrinhos']:
            st.write(f"Cliente: {c['cliente']}")
    else:
        st.write("Nenhum carrinho ativo.")
        
def main():
    gerenciamento_carrinhos()
           
 
main()