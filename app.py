import streamlit as st
import time
import random

# Tentei fazer com Pygame mas o Streamlit roda no servidor, 
# entao fiz essa versao 'web' pra testar a logica de estados!
# Estudo de Python - @SeuUsuario

st.set_page_config(page_title="Meu Lab de Python", page_icon="🐍")

st.title("🐍 Lab de Estudos: Lógica do Snake")
st.write("Estou estudando como o Python gerencia estados (session_state).")

# Inicializando as variaveis que vao 'guardar' o jogo na memoria do navegador
if 'pontos' not in st.session_state:
    st.session_state.pontos = 0
if 'recorde' not in st.session_state:
    st.session_state.recorde = 0

# Simulação de colisão/comida (Lógica que estou treinando)
def comer_frutinha():
    st.session_state.pontos += 10
    if st.session_state.pontos > st.session_state.recorde:
        st.session_state.recorde = st.session_state.pontos
    st.toast("Boa! +10 pontos 🍎") # Pequeno alerta visual

col1, col2 = st.columns(2)
with col1:
    st.metric("Pontuação", st.session_state.pontos)
with col2:
    st.metric("Meu Recorde", st.session_state.recorde)

st.divider()

st.subheader("Controle da Cobrinha (Simulado)")
st.write("Como o Streamlit atualiza a página toda, estou testando botões para a movimentação:")

if st.button("🍎 Capturar Frutinha!"):
    comer_frutinha()
    st.balloons() # Efeito visual de comemoração

if st.button("Resetar Jogo"):
    st.session_state.pontos = 0
    st.warning("Jogo reiniciado! Voltando ao zero.")

# Comentario de rodapé 'humano'
st.info("Nota mental: Estudar como fazer o loop automático sem o usuário precisar clicar.")
