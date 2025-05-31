import streamlit as st 

def set_options():
    if 'preco_acc' not in st.session_state:
        st.session_state['preco_acc'] = False
    if 'estoque' not in st.session_state:
        st.session_state['estoque'] = False
    