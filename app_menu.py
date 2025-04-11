import streamlit as st
import subprocess

st.set_page_config(page_title="Física Aplicada - Menu", page_icon="📚")

st.title("📚 Menu Principal - Física Aplicada à Engenharia")

opcao = st.selectbox("Escolha um módulo para abrir:", [
    "Selecione...",
    "🔹 Movimento Retilíneo (MRU & MRUV)",
    "🔹 Leis de Newton",
    "🔹 Energia Mecânica",
    "🔹 Circuitos Elétricos"
])

# Executa outro script conforme a escolha
if opcao == "🔹 Movimento Retilíneo (MRU & MRUV)":
    st.success("Abrindo MRU & MRUV...")
    subprocess.run(["streamlit", "run", "mru_muv_app.py"])
elif opcao == "🔹 Leis de Newton":
    st.success("Abrindo Leis de Newton...")
    subprocess.run(["streamlit", "run", "leis_newton.py"])
elif opcao == "🔹 Energia Mecânica":
    st.success("Abrindo Energia Mecânica...")
    subprocess.run(["streamlit", "run", "energia.py"])
elif opcao == "🔹 Circuitos Elétricos":
    st.success("Abrindo Circuitos Elétricos...")
    subprocess.run(["streamlit", "run", "circuitos.py"])

st.markdown("---")
st.caption("Desenvolvido por João Barcelo ✨")
