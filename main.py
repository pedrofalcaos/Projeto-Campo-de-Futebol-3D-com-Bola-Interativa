import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import messagebox

class CampoFutebol3D:
    def __init__(self, largura=8, comprimento=16, altura=5):
        """Inicializa o campo de futebol 3D com dimensões especificadas."""
        self.largura = largura
        self.comprimento = comprimento
        self.altura = altura
        self.posicao_inicial = np.array([largura // 2, 0, 0])  # Posição inicial da bola no centro do campo
        self.posicao_bola = self.posicao_inicial.copy()
        # Definindo o gol com uma largura e altura adequadas
        self.gol_posicao = [largura // 3, 2 * largura // 3, comprimento - 0.5, comprimento - 1.5, altura * 0.6]
        self.fig = None
        self.ax = None
        self.bola = None

    def mover_bola(self, dx, dy, dz):
        """Move a bola em uma direção específica no espaço 3D."""
        self.posicao_bola[0] += dx
        self.posicao_bola[1] += dy
        self.posicao_bola[2] += dz

        # Verifica se a bola cruzou a linha do gol entre as três traves
        if (self.gol_posicao[0] <= self.posicao_bola[0] <= self.gol_posicao[1] and
            self.gol_posicao[3] < self.posicao_bola[1] <= self.gol_posicao[2] and
            0 <= self.posicao_bola[2] <= self.gol_posicao[4]):
            print("Gol no Sport")  # Mensagem no terminal
            self.posicao_bola = self.posicao_inicial.copy()  # Retorna a bola ao centro do campo
        # Verifica se a bola saiu completamente do campo pelas quatro linhas
        elif (self.posicao_bola[0] < 0 or self.posicao_bola[0] > self.largura or
              self.posicao_bola[1] < 0 or self.posicao_bola[1] > self.comprimento or
              self.posicao_bola[2] < 0 or self.posicao_bola[2] > self.altura):
            print("Bola fora")  # Mensagem no terminal
            # Limita a posição da bola aos limites do campo
            self.posicao_bola = np.clip(self.posicao_bola, [0, 0, 0], [self.largura, self.comprimento, self.altura])

        # Exibe as coordenadas da bola no terminal após o movimento
        print(f"Coordenadas da bola: X={self.posicao_bola[0]}, Y={self.posicao_bola[1]}, Z={self.posicao_bola[2]}")

    def mostrar_grafico(self):
        """Cria uma visualização em tempo real do campo e do movimento da bola."""
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Configuração do gráfico
        self.ax.set_xlim(0, self.largura)
        self.ax.set_ylim(0, self.comprimento)
        self.ax.set_zlim(0, self.altura)
        self.ax.set_xlabel('Eixo X (Largura)')
        self.ax.set_ylabel('Eixo Y (Comprimento)')
        self.ax.set_zlabel('Eixo Z (Altura)')
        self.ax.set_title('Campo de Futebol 3D')

        # Campo verde com linhas fixas
        self.ax.set_facecolor((0, 0.5, 0))  # Cor verde para o fundo do gráfico

        # Plota as linhas de marcação do campo
        self.ax.plot([1, self.largura - 1], [self.comprimento / 2, self.comprimento / 2], [0, 0], color='white')  # Linha do meio
        self.ax.plot([1, 1], [1, self.comprimento - 1], [0, 0], color='white')  # Linha lateral esquerda
        self.ax.plot([self.largura - 1, self.largura - 1], [1, self.comprimento - 1], [0, 0], color='white')  # Linha lateral direita
        self.ax.plot([1, self.largura - 1], [1, 1], [0, 0], color='white')  # Linha de fundo
        self.ax.plot([1, self.largura - 1], [self.comprimento - 1, self.comprimento - 1], [0, 0], color='white')  # Linha de fundo oposta

        # Plota o gol em 3D com tamanho ajustado
        gol_x = [self.gol_posicao[0], self.gol_posicao[1], self.gol_posicao[1], self.gol_posicao[0], self.gol_posicao[0]]
        gol_y = [self.gol_posicao[2], self.gol_posicao[2], self.gol_posicao[3], self.gol_posicao[3], self.gol_posicao[2]]
        gol_z = [0, 0, self.gol_posicao[4], self.gol_posicao[4], 0]
        self.ax.plot(gol_x, gol_y, gol_z, color='white', linewidth=3, label='Gol')

        # Inicializa a bola no gráfico
        self.bola, = self.ax.plot([], [], [], 'o', color='orange', markersize=10, label='Bola')

        # Conecta a função para tratar eventos de teclado
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)

        # Conecta o evento de fechamento da janela
        self.fig.canvas.mpl_connect('close_event', self.on_close)

        animacao = FuncAnimation(self.fig, self.atualizar_grafico, interval=200, blit=True)
        plt.legend()
        plt.show()

    def atualizar_grafico(self, frame):
        """Função de atualização para o gráfico de animação."""
        self.bola.set_data([self.posicao_bola[0]], [self.posicao_bola[1]])
        self.bola.set_3d_properties([self.posicao_bola[2]])

        return self.bola,

    def on_key_press(self, event):
        """Movimenta a bola com base nas teclas pressionadas."""
        if event.key == 'up':
            self.mover_bola(0, 1, 0)  # Move no eixo Y (frente)
        elif event.key == 'down':
            self.mover_bola(0, -1, 0)  # Move no eixo Y (trás)
        elif event.key == 'left':
            self.mover_bola(-1, 0, 0)  # Move no eixo X (esquerda)
        elif event.key == 'right':
            self.mover_bola(1, 0, 0)  # Move no eixo X (direita)
        elif event.key == ' ':  # Barra de espaço para subir no eixo Z
            self.mover_bola(0, 0, 1)
        elif event.key == 'c':  # Tecla "C" para descer no eixo Z
            self.mover_bola(0, 0, -1)

    def on_close(self, event):
        """Exibe uma mensagem pop-up quando o usuário tenta fechar o programa."""
        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal do tkinter

        while True:
            resposta = messagebox.askquestion("O Sport perdeu?", "O Sport perdeu?")
            if resposta == 'yes':
                root.destroy()  # Fecha a janela do tkinter e encerra o loop
                break
            else:
                messagebox.showinfo("Resposta errada", "Resposta errada, responda novamente.")

# Inicia a interface gráfica no mesmo fluxo principal
campo = CampoFutebol3D()
campo.mostrar_grafico()
