import streamlit as st
import time
import random

# Tive que mudar a estratégia! O Tkinter não roda no servidor do Streamlit 
# pq ele tenta abrir uma janela física. Entendi que pra Web a lógica é outra.
# Versão 2.0 - "A Cobrinha por Botões" kkk

st.title("🐍 Meu Estudo de Lógica: Snake Game")

# Setup do Tabuleiro (Lista de listas pra representar o grid)
if 'snake' not in st.session_state:
    st.session_state.snake = [[5, 5], [5, 6], [5, 7]]
    st.session_state.food = [random.randint(0, 9), random.randint(0, 9)]
    st.session_state.direction = "Cima"
    st.session_state.score = 0
    st.session_state.game_over = False

def mover(nova_dir):
    if st.session_state.game_over:
        return

    st.session_state.direction = nova_dir
    head = st.session_state.snake[-1].copy()
    
    if nova_dir == "Cima": head[0] -= 1
    elif nova_dir == "Baixo": head[0] += 1
    elif nova_dir == "Esquerda": head[1] -= 1
    elif nova_dir == "Direita": head[1] += 1

    # Checar se bateu na parede (Grid 10x10)
    if head[0] < 0 or head[0] >= 10 or head[1] < 0 or head[1] >= 10 or head in st.session_state.snake:
        st.session_state.game_over = True
        return

    st.session_state.snake.append(head)
    
    if head == st.session_state.food:
        st.session_state.score += 1
        st.session_state.food = [random.randint(0, 9), random.randint(0, 9)]
    else:
        st.session_state.snake.pop(0)

# Interface do Usuário
st.subheader(f"Pontos: {st.session_state.score}")

if st.session_state.game_over:
    st.error(f"GAME OVER! Você fez {st.session_state.score} pontos.")
    if st.button("Tentar de novo"):
        st.session_state.clear()
        st.rerun()
else:
    # Desenhar o "Tabuleiro" usando emojis (mais simples pra quem está aprendendo)
    grid = ""
    for r in range(10):
        for c in range(10):
            if [r, c] == st.session_state.snake[-1]:
                grid += "🟢 " # Cabeça
            elif [r, c] in st.session_state.snake:
                grid += "🟩 " # Corpo
            elif [r, c] == st.session_state.food:
                grid += "🍎 " # Comida
            else:
                grid += "⬛ " # Vazio
        grid += "\n"
    
    st.text(grid)

    # Controles (Pq o teclado no navegador é mais difícil de configurar)
    st.write("Controles:")
    col1, col2, col3 = st.columns([1,1,1])
    with col2: st.button("⬆️", on_click=mover, args=("Cima",))
    c1, c2, c3 = st.columns([1,1,1])
    with c1: st.button("⬅️", on_click=mover, args=("Esquerda",))
    with c2: st.button("⬇️", on_click=mover, args=("Baixo",))
    with c3: st.button("➡️", on_click=mover, args=("Direita",))

st.info("Ainda estou aprendendo a fazer o movimento automático, por enquanto é no clique! kkk")
