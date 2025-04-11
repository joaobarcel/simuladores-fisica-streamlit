import streamlit as st

st.title("🔌 Lei de Ohm e Potência Elétrica")

tensao = st.number_input("Tensão (V):", min_value=0.0)
corrente = st.number_input("Corrente (A):", min_value=0.0)

if st.button("Calcular"):
    if corrente != 0:
        resistencia = tensao / corrente
    else:
        resistencia = 0

    potencia = tensao * corrente

    st.write(f"Resistência: {resistencia:.2f} Ω")
    st.write(f"Potência: {potencia:.2f} W")

    if potencia > 500:
        st.warning("⚠️ Circuito de alta potência! Verificar dissipação de calor.")
