import streamlit as st

st.title("GameBoxd 🎮")
st.write("Meu primeiro app de catálogo de jogos")

nome_jogo = st.text_input("Digite o nome do jogo")
nota = st.slider("Dê uma nota", 0, 10)

if st.button("Salvar"):
    st.success(f"{nome_jogo} recebeu nota {nota}")