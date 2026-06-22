"""
Módulo principal do jogo. Junta tela inicial, os 3 níveis (com lore entre eles)
e as telas de vitória/game over. É chamado pelo main.py através de executar_jogo().
"""
import pygame
from src.config import LARGURA, ALTURA
from src.telas import tela_inicial, tela_transicao, tela_vitoria, tela_game_over
from src.fase import jogar_nivel


def executar_jogo():
    pygame.init()

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Guerra das Máquinas!')
    relogio = pygame.time.Clock()

    fonte = pygame.font.SysFont(None, 35)
    fonte_media = pygame.font.SysFont(None, 45)
    fonte_grande = pygame.font.SysFont(None, 70)
    fontes = (fonte, fonte_media, fonte_grande)

    # === TELA INICIAL ===
    if not tela_inicial(tela, relogio, fontes):
        pygame.quit()
        return

    score = 0
    vidas = 3

    for nivel in range(1, 4):
        resultado_transicao = tela_transicao(tela, relogio, fontes, nivel)
        if resultado_transicao == "sair":
            break

        score, vidas, resultado = jogar_nivel(tela, relogio, fonte, nivel, score, vidas)

        if resultado == "sair":
            break
        elif resultado == "game_over":
            tela_game_over(tela, fonte_media, fonte_grande, score)
            break
        elif resultado == "vitoria" and nivel == 3:
            tela_vitoria(tela, fonte_media, fonte_grande)
            # senão (nível 1 ou 2), o loop "for" simplesmente continua para o próximo nível

    pygame.quit()
