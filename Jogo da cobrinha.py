# Importa a biblioteca tkinter (interface gráfica) com o apelido tk
import tkinter as tk

# Importa a biblioteca random para gerar posições aleatórias da comida
import random

# --- Configurações básicas ---
largura = 400       # Largura da janela do jogo
altura = 400        # Altura da janela do jogo
tamanho = 20        # Tamanho dos blocos da cobra e da comida
velocidade = 200    # Intervalo de atualização do jogo em milissegundos

# Define a direção inicial da cobra
direcao = "direita"

# Lista que representa a cobra com posições (x, y) dos blocos
cobra = [
    [100, 100],   # Cabeça
    [80, 100],    # Corpo
    [60, 100]     # Cauda
]

# Define posição inicial da comida de forma aleatória
comida = [
    random.randrange(0, largura, tamanho),
    random.randrange(0, altura, tamanho)
]

# --- Função que desenha a cobra e a comida na tela ---
def desenhar():
    canvas.delete("all")  # Limpa todo o conteúdo do canvas (tela)

    # Desenha cada bloco da cobra como um retângulo verde
    for segmento in cobra:
        x, y = segmento
        canvas.create_rectangle(x, y, x + tamanho, y + tamanho, fill="green")

    # Desenha a comida como um círculo vermelho
    x, y = comida
    canvas.create_oval(x, y, x + tamanho, y + tamanho, fill="red")

# --- Função que muda a direção da cobra quando uma tecla é pressionada ---
def mudar_direcao(event):
    global direcao  # Acessa a variável global de direção
    tecla = event.keysym  # Pega o nome da tecla pressionada

    # Impede a cobra de ir diretamente para a direção oposta
    if tecla == "Up" and direcao != "baixo":
        direcao = "cima"
    elif tecla == "Down" and direcao != "cima":
        direcao = "baixo"
    elif tecla == "Left" and direcao != "direita":
        direcao = "esquerda"
    elif tecla == "Right" and direcao != "esquerda":
        direcao = "direita"

# --- Função que atualiza o estado do jogo a cada 'velocidade' ms ---
def atualizar():
    global comida  # Acessa a variável global comida

    # Pega a posição atual da cabeça da cobra
    x, y = cobra[0]

    # Move a cabeça para a nova posição com base na direção
    if direcao == "cima":
        y -= tamanho
    elif direcao == "baixo":
        y += tamanho
    elif direcao == "esquerda":
        x -= tamanho
    elif direcao == "direita":
        x += tamanho

    # Cria nova posição da cabeça
    nova_cabeca = [x, y]

    # Verifica colisão com bordas da tela ou com o próprio corpo
    if x < 0 or x >= largura or y < 0 or y >= altura or nova_cabeca in cobra:
        canvas.delete("all")  # Limpa a tela
        # Escreve "FIM DE JOGO!" no centro da tela
        canvas.create_text(largura/2, altura/2, text="FIM DE JOGO!", font=("Arial", 24), fill="red")
        return  # Encerra a execução da função (fim do jogo)

    # Adiciona a nova cabeça da cobra
    cobra.insert(0, nova_cabeca)

    # Verifica se a cobra comeu a comida
    if nova_cabeca == comida:
        # Gera nova comida em posição aleatória
        comida = [random.randrange(0, largura, tamanho), random.randrange(0, altura, tamanho)]
    else:
        # Remove o último segmento (a cauda), simulando movimento
        cobra.pop()

    # Redesenha a tela com a nova posição
    desenhar()

    # Agenda a próxima atualização do jogo após 'velocidade' milissegundos
    janela.after(velocidade, atualizar)

# --- Criação da janela do jogo ---
janela = tk.Tk()  # Cria a janela principal
janela.title("Jogo da Cobrinha Simples")  # Define o título da janela

# Cria o canvas (área gráfica onde a cobra será desenhada)
canvas = tk.Canvas(janela, width=largura, height=altura, bg="black")
canvas.pack()  # Adiciona o canvas à janela

# Liga os eventos de teclas ao controle de direção da cobra
janela.bind("<KeyPress>", mudar_direcao)

# Inicia o jogo chamando a função atualizar pela primeira vez
atualizar()

# Mantém a janela aberta em loop (esperando interações do usuário)
janela.mainloop()
