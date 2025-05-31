import streamlit as st


st.title("⚙️ Configurações e Conta")
st.markdown("Ajuste suas preferências ou recupere o acesso à sua conta.")



st.subheader("Configuração página de Vendas")
preco_acquisicao = st.checkbox("preço de aquisição", value=st.session_state.get('preco_acc', False))
estoque = st.checkbox("controle de estoque", value=st.session_state.get('estoque', False))
if preco_acquisicao:
    st.session_state['preco_acc'] = True
else:
    st.session_state['preco_acc'] = False
    
    
if estoque:
    st.session_state['estoque'] = True
else:
    st.session_state['estoque'] = False
    
    

st.markdown("---")
