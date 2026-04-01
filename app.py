import streamlit as st
import random

# Título com cara de "Projeto em Construção"
st.set_page_config(page_title="Snake Lab v2", page_icon="🐍")
st.title("🐍 Lab de Python: Desafio da Lógica")

# Inicializando o estado do jogo (Session State é como a 'memória' do navegador)
if 'snake_pos' not in st.session_state:
    st.session_state.snake_pos = [[5, 5]]
    st.session_state.food_pos = [random.randint(0, 9), random.randint(0, 9)]
    st.session_state.score = 0
    st.session_state.fim_de_jogo = False

# Função que processa o movimento quando o botão é clicado
def mover_cobra(direcao):
    if st.session_state.fim_de_jogo:
        return

    cabeca = st.session_state.snake_pos[-1].copy()
    
    if direcao == "Cima": cabeca[0] -= 1
    elif direcao == "Baixo": cabeca[0] += 1
    elif direcao == "Esquerda": cabeca[1] -= 1
    elif direcao == "Direita": cabeca[1] += 1

    # Checar colisão com as bordas do grid 10x10
    if cabeca[0] < 0 or cabeca[0] > 9 or cabeca[1] < 0 or cabeca[1] > 9 or cabeca in st.session_state.snake_pos:
        st.session_state.fim_de_jogo = True
    else:
        st.session_state.snake_pos.append(cabeca)
        if cabeca == st.session_state.food_pos:
            st.session_state.score += 10
            st.session_state.food_pos = [random.randint(0, 9), random.randint(0, 9)]
        else:
            st.session_state.snake_pos.pop(0)

# Renderização do Visual
st.subheader(f"Pontos: {st.session_state.score}")

if st.session_state.fim_de_jogo:
    st.error(f"GAME OVER! Score final: {st.session_state.score}")
    if st.button("Reiniciar"):
        st.session_state.clear()
        st.rerun()
else:
    # Criando o tabuleiro usando Markdown e Emojis
    tabuleiro = ""
    for r in range(10):
        linha = ""
        for c in range(10):
            if [r, c] == st.session_state.snake_pos[-1]:
                linha += "🟢" # Cabeça
            elif [r, c] in st.session_state.snake_pos:
                linha += "🟩" # Corpo
            elif [r, c] == st.session_state.food_pos:
                linha += "🍎" # Comida
            else:
                linha += "⬜" # Fundo
        tabuleiro += linha + "\n"
    
    st.text(tabuleiro)

    # Controles por botões (único jeito 100% seguro no Streamlit Cloud free)
    st.write("Clique para mover:")
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2: st.button("⬆️", on_click=mover_cobra, args=("Cima",))
    
    c4, c5, c6 = st.columns([1, 1, 1])
    with c4: st.button("⬅️", on_click=mover_cobra, args=("Esquerda",))
    with c5: st.button("⬇️", on_click=mover_cobra, args=("Baixo",))
    with c6: st.button("➡️", on_click=mover_cobra, args=("Direita",))

st.caption("Nota de estudo: Implementando botões porque o Streamlit não captura eventos de teclado nativos como um app desktop.")
