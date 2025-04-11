import streamlit as st

st.title("⚡ Energia Mecânica")

massa = st.number_input("Massa (kg):", min_value=0.0)
velocidade = st.number_input("Velocidade (m/s):", min_value=0.0)
altura = st.number_input("Altura (m):", min_value=0.0)
g = 9.81

if st.button("Calcular Energias"):
    Ec = 0.5 * massa * velocidade**2
    Ep = massa * g * altura
    Em = Ec + Ep

    st.write(f"Energia Cinética: {Ec:.2f} J")
    st.write(f"Energia Potencial Gravitacional: {Ep:.2f} J")
    st.success(f"Energia Mecânica Total: {Em:.2f} J")
