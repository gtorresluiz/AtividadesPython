#bibliotecas
import pygame, sys
from pygame.locals import *

# Setando jogos
pygame.init()
tempo = pygame.time.Clock()
fonte = pygame.font.Font(None, 36)

# Constantes
janela_largura = 800
janela_altura = 800

# Cores
vermelho = (255, 0, 0)  # cor da pedra
branco = (255, 255, 255)  # cor do jogador
preto = (0, 0, 0)  # cor do fundo
amarelo = (255, 255, 0)  # cor da fonte do texto
azul_ciano = (0, 255, 255)  # cor dos quadradinhos

# Posição e tamanho do jogador
jogador_tamanho = 20
jogador_pos = [(janela_largura // 2) - (jogador_tamanho // 2), (janela_altura // 2) - (jogador_tamanho // 2)]
jogador_velocidade = 5

# Pedras para o labirinto
labirinto_pedras = [
    (150, 0, 50, 300), (150, 400, 50, 400), # Coluna esquerda
    (300, 100, 50, 300), (300, 500, 50, 300), # Coluna central
    (450, 0, 50, 300), (450, 400, 50, 400), # Coluna direita
    (600, 100, 50, 300), (600, 500, 50, 300), # Coluna direita
]

# Quadradinhos amarelos nas bordas da tela
quadradinhos = [
    (50, 50, 10, 10), (750, 50, 10, 10), (50, 750, 10, 10), (750, 750, 10, 10),
    (50, 400, 10, 10), (750, 400, 10, 10), (400, 50, 10, 10), (400, 750, 10, 10),
    (100, 50, 10, 10), (700, 50, 10, 10), (100, 750, 10, 10), (700, 750, 10, 10),
    (50, 100, 10, 10), (750, 100, 10, 10), (50, 700, 10, 10), (750, 700, 10, 10)
]

placar = 0
pontuacao_anterior = -1   
tempo_inicio = pygame.time.get_ticks()

# Configurando a janela
tela = pygame.display.set_mode((janela_largura, janela_altura), 0, 32)
pygame.display.set_caption("Sprint Jogo Python")

# Funções
def inserir_pedra(pedras):
    for pedra in pedras:
        pygame.draw.rect(tela, vermelho, pygame.Rect(*pedra))

def inserir_quadradinhos(quadradinhos):
    for quadradinho in quadradinhos:
        pygame.draw.rect(tela, azul_ciano, pygame.Rect(*quadradinho))

def inserir_jogador():
    pygame.draw.rect(tela, branco, pygame.Rect(jogador_pos[0], jogador_pos[1], jogador_tamanho, jogador_tamanho))

def checar_colisao(rect1, rect2):
    return pygame.Rect(rect1).colliderect(rect2)

def pos_colisao(ret_jogador, objetos):
    for obj in objetos:
        if checar_colisao(ret_jogador, obj):
            return obj
    return None

def config_comandos():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jogador_pos[0] -= jogador_velocidade
    if keys[pygame.K_RIGHT]:
        jogador_pos[0] += jogador_velocidade
    if keys[pygame.K_UP]:
        jogador_pos[1] -= jogador_velocidade
    if keys[pygame.K_DOWN]:
        jogador_pos[1] += jogador_velocidade

def inserir_placar():
    global pontuacao_anterior, placar
    placar_design = fonte.render(f'Pontuação: {placar}', True, amarelo)
    tela.blit(placar_design, (10, 10))
    if placar != pontuacao_anterior:  
        pontuacao_anterior = placar
        print(f'Pontuação: {placar}')

def inserir_tempo(tempo_decorrido):
    tempo_design = fonte.render(f'Tempo: {tempo_decorrido} s', True, amarelo)
    tela.blit(tempo_design, (10, 50))

#função de wrap around
def entorno():
    if jogador_pos[0] < 0:
        jogador_pos[0] = janela_largura - jogador_tamanho
    elif jogador_pos[0] > janela_largura:
        jogador_pos[0] = 0
    if jogador_pos[1] < 0:
        jogador_pos[1] = janela_altura - jogador_tamanho
    elif jogador_pos[1] > janela_altura:
        jogador_pos[1] = 0

def game_over(mensagem):
    tela.fill(preto)  # Limpa a tela
    fonte_game_over = pygame.font.Font(None, 74)
    game_over_design = fonte_game_over.render(mensagem, True, vermelho)
    tela.blit(game_over_design, ((janela_largura // 2) - (game_over_design.get_width() // 2), (janela_altura // 2) - (game_over_design.get_height() // 2))) #centro da tela
    pygame.display.flip()
    pygame.time.wait(3000)

# Loop principal
rodando = True
while rodando == True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    #chama funcoes      
    config_comandos()
    entorno()
    
    # Termina o jogo em caso de colisão com uma pedra
    ret_jogador = (jogador_pos[0], jogador_pos[1], jogador_tamanho, jogador_tamanho)
    if pos_colisao(ret_jogador, labirinto_pedras):
        game_over("Game Over")
        rodando = False
    
    # Verifica colisão com quadradinhos
    quadradinho_coletado = pos_colisao(ret_jogador, quadradinhos)
    if quadradinho_coletado:
        quadradinhos.remove(quadradinho_coletado)
        placar += 20
        jogador_tamanho += 5 
        
    # vitória quando chega em 300 pontos 
    if jogador_tamanho >= 75:   
        game_over("Você venceu")
        rodando = False
    
    #executa o resto do jogo
    tela.fill(preto)
    inserir_jogador()
    inserir_pedra(labirinto_pedras)
    inserir_quadradinhos(quadradinhos)
    inserir_placar()
    
    # Calcula e exibe o tempo decorrido
    tempo_decorrido = (pygame.time.get_ticks() - tempo_inicio) // 1000
    inserir_tempo(tempo_decorrido)
    
    pygame.display.flip()
    tempo.tick(30)

#encerra o jogo  
pygame.quit()
sys.exit()
