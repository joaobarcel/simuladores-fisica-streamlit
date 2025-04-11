import streamlit as st

st.title("🚗 Movimento Retilíneo (MRU & MRUV)")

tipo_mov = st.radio("Escolha o tipo de movimento:", ["MRU", "MRUV"])

if tipo_mov == "MRU":
    distancia = st.number_input("Distância (m):", min_value=0.0)
    tempo = st.number_input("Tempo (s):", min_value=0.1)
    if st.button("Calcular velocidade (MRU)"):
        velocidade = distancia / tempo
        st.success(f"Velocidade: {velocidade:.2f} m/s")

else:
    velocidade_inicial = st.number_input("Velocidade inicial (m/s):")
    aceleracao = st.number_input("Aceleração (m/s²):")
    tempo = st.number_input("Tempo (s):", min_value=0.0)
    if st.button("Calcular distância (MRUV)"):
        distancia = velocidade_inicial * tempo + 0.5 * aceleracao * tempo**2
        st.success(f"Distância: {distancia:.2f} m")
