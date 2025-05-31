import streamlit as st  


def main():
    st.title(" Usuários ")
    st.markdown("Gerencie os usuários do sistema.")
    st.subheader("Lista de Usuários")
    usuarios = {'João': {'nome': 'João', 'email':'joão@xpto.com'}, 
                'Ana': {'nome': 'Ana', 'email':'ana@xpto.com'}}
    if st.button("Adicionar Usuário"):
        nome = st.text_input("Nome do Usuário")
        email = st.text_input("Email do Usuário")
        if st.button("Salvar"):
            if nome and email:
                usuarios[nome] = {'nome': nome, 'email': email}
                st.success(f"Usuário {nome} adicionado com sucesso!")
                st.rerun()
            else:
                st.error("Por favor, preencha todos os campos.")
                
    for usuario, info in usuarios.items():
        with st.expander(f"Usuário: {info['nome']}"):
            st.write(f"Email: {info['email']}")
            if st.button("Remover Usuário", key=usuario):
                st.warning(f"Usuário {info['nome']} removido.")
                st.rerun()
                
    
        
main()