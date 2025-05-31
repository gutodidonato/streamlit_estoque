import streamlit as st
import pandas as pd
import plotly.express as px
import random


# Título principal
st.title("🛍️ Painel de Vendas - Resumo Geral")
st.markdown("Bem-vindo! Aqui está um resumo rápido das suas vendas mais recentes. Tudo em tempo real e com carinho 😉")

# Dados simulados
produtos = ['Camiseta', 'Tênis', 'Boné', 'Calça Jeans', 'Mochila']
vendas = [random.randint(50, 200) for _ in produtos]
valores = [v * random.uniform(50, 200) for v in vendas]
df = pd.DataFrame({
    "Produto": produtos,
    "Unidades Vendidas": vendas,
    "Receita (R$)": [round(v, 2) for v in valores]
})

# KPIs principais
st.subheader("📌 Indicadores Gerais")
kpi1, kpi2, kpi3 = st.columns(3, gap="medium", border=True)
kpi1.metric("Produtos Vendidos", f"{df['Unidades Vendidas'].sum()} unidades")
kpi2.metric("Receita Total", f"R$ {df['Receita (R$)'].sum():,.2f}")
kpi3.metric("Produto Mais Vendido", df.loc[df['Unidades Vendidas'].idxmax(), 'Produto'])


st.markdown("---")
st.subheader(":red[Produtos em falta]")
produtos_em_falta = {'Camiseta': {'quantidade' : 33, 'quantidade_minima': 22 }, 'Tênis': {'quantidade' : 13, 'quantidade_minima': 22 }}
for produto, info in produtos_em_falta.items():
    if (info['quantidade'] < info['quantidade_minima']):
        st.warning(f"Produto {produto} está abaixo do estoque mínimo. Quantidade atual: {info['quantidade']}, Quantidade mínima: {info['quantidade_minima']}")

st.markdown("---")

col1, col2 = st.columns(2, gap="medium", border=True)
with col1:
    st.subheader("📦 Vendas por Produto")
    fig_bar = px.bar(df, x="Produto", y="Unidades Vendidas", color="Produto", title="Unidades Vendidas por Produto")
    st.plotly_chart(fig_bar, use_container_width=True)
with col2:
    st.subheader("💰 Receita por Produto")
    fig_pie = px.pie(df, values="Receita (R$)", names="Produto", title="Distribuição da Receita")
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")
st.subheader("🧾 Detalhamento dos Dados")
st.dataframe(df, use_container_width=True)

