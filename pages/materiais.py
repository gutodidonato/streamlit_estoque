import streamlit as st 

def main():
    st.title("Materiais")
    st.markdown("Gerencie os materiais utilizados na produção.")
    st.markdown("---")
    materiais = {
        'material1': {'nome': 'Tecido', 'quantidade': 100, 'valor': 500.00},
        'material2': {'nome': 'Linha', 'quantidade': 200, 'valor': 150.00},
        'material3': {'nome': 'Botões', 'quantidade': 300, 'valor': 75.00}
    }
    produto = {
        'produto1' : {'materiais': [{'nome': 'Tecido', 'quantidade': 10, 'valor': 50.00}, {'nome': 'Linha', 'quantidade': 5, 'valor': 15.00}]},
        'produto2' : {'materiais': [{'nome': 'Tecido', 'quantidade': 20, 'valor': 100.00}, {'nome': 'Botões', 'quantidade': 10, 'valor': 30.00}]},
    }
    
    for produto, info in produto.items():
        with st.expander(f"Produto: {produto}"):
            for material in info['materiais']:
                st1, st2, st3 = st.columns(3)
                with st1:
                    st.write(f"Material: {material['nome']}")
                with st2:
                    st.write(f"Quantidade: {material['quantidade']}")
                with st3:
                    st.write(f"Valor Total: R$ {material['valor']:.2f}")
            
            stt1, stt2 = st.columns(2)
            with stt1:
                if st.button("Remover Produto", key=produto):
                    st.warning(f"Produto {produto} removido.")
                    st.rerun()
                
            with stt2:
                if st.button("Fabricar Produto", key=f"fabricar_{produto}"):
                    st.success(f"Produto {produto} fabricado com sucesso!")
    
    
main()