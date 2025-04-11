import streamlit as st

st.title("⚖️ Leis de Newton")

massa = st.number_input("Massa (kg):", min_value=0.0)
aceleracao = st.number_input("Aceleração (m/s²):")

if st.button("Calcular Força"):
    forca = massa * aceleracao
    st.success(f"Força resultante: {forca:.2f} N")

st.write("Se a força for maior que 100 N, cuidado com a estrutura!")

if massa > 0 and aceleracao > 0 and forca > 100:
    st.warning("⚠️ Força elevada detectada!")
