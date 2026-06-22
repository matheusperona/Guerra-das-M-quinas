"""
Funções de desenho: fundo de cada nível, nave do jogador e inimigos.
Tudo aqui é só "pintar na tela" — nenhuma regra de jogo fica neste arquivo.
"""
import random
import pygame
from src.config import (
    LARGURA, ALTURA, BRANCO, AZUL_CLARO, VERMELHO, AMARELO, CINZA, LARANJA,
    MARROM, MARROM_CLARO, CONFIG_NIVEIS,
)

# Estrelas fixas geradas uma única vez (usadas nos níveis 2 e 3)
ESTRELAS = [(random.randint(0, LARGURA), random.randint(0, ALTURA)) for _ in range(120)]


def desenhar_fundo(tela, nivel):
    """Desenha o fundo temático de cada nível (subsolo, terra firme, espaço)."""
    if nivel == 1:
        # Subsolo: fundo escuro com linhas de terra e rochas
        tela.fill((15, 10, 5))
        for i in range(0, LARGURA, 60):
            pygame.draw.line(tela, (40, 25, 10), (i, 0), (i, ALTURA), 1)
        for j in range(0, ALTURA, 80):
            pygame.draw.line(tela, (40, 25, 10), (0, j), (LARGURA, j), 1)
        rochas = [(50, 150, 70, 30), (300, 350, 90, 25), (600, 200, 60, 20),
                  (150, 480, 80, 25), (700, 400, 50, 20)]
        for rx, ry, rw, rh in rochas:
            pygame.draw.ellipse(tela, MARROM_CLARO, (rx, ry, rw, rh))
            pygame.draw.ellipse(tela, MARROM, (rx + 5, ry + 5, rw - 10, rh - 10))

    elif nivel == 2:
        # Terra firme: céu noturno com chão e prédios destruídos
        tela.fill((10, 15, 30))
        pygame.draw.rect(tela, (30, 60, 20), (0, ALTURA - 60, LARGURA, 60))
        pygame.draw.rect(tela, (20, 45, 15), (0, ALTURA - 65, LARGURA, 8))
        predios = [(50, 350, 60, 200), (150, 300, 80, 260), (350, 320, 70, 240),
                   (550, 280, 90, 280), (700, 340, 70, 220)]
        for px, py, pw, ph in predios:
            pygame.draw.rect(tela, (25, 25, 35), (px, py, pw, ph))
            pygame.draw.rect(tela, (35, 35, 50), (px + 5, py + 10, pw - 10, ph - 10))
            for wx in range(px + 8, px + pw - 8, 15):
                for wy in range(py + 15, py + ph - 15, 20):
                    if random.random() > 0.7:
                        pygame.draw.rect(tela, (60, 55, 20), (wx, wy, 8, 8))
        for ex, ey in ESTRELAS[:40]:
            pygame.draw.circle(tela, BRANCO, (ex, ey % (ALTURA - 80)), 1)

    elif nivel == 3:
        # Espaço: estrelas, nebulosa sutil e planeta ao fundo
        tela.fill((2, 2, 15))
        for nx in range(0, LARGURA, 4):
            for ny in range(0, ALTURA, 4):
                d = ((nx - 400) ** 2 + (ny - 200) ** 2) ** 0.5
                if d < 180:
                    alpha = max(0, int(18 - d / 10))
                    pygame.draw.rect(tela, (alpha, 0, alpha * 2), (nx, ny, 4, 4))
        for ex, ey in ESTRELAS:
            pygame.draw.circle(tela, BRANCO, (ex, ey), 1)
        pygame.draw.circle(tela, (40, 40, 80), (660, 120), 70)
        pygame.draw.circle(tela, (55, 55, 110), (660, 120), 65)
        pygame.draw.ellipse(tela, (80, 80, 140), (590, 110, 140, 20))


def desenhar_player(tela, rect):
    """Desenha a nave do jogador (corpo, cockpit, asas e chama do motor)."""
    cx = rect.centerx
    cy = rect.centery

    pygame.draw.polygon(tela, AZUL_CLARO, [
        (cx, rect.top),
        (rect.left + 5, rect.bottom),
        (rect.right - 5, rect.bottom),
    ])
    pygame.draw.polygon(tela, BRANCO, [
        (cx, rect.top + 8),
        (cx - 8, cy),
        (cx + 8, cy),
    ])
    pygame.draw.polygon(tela, (0, 170, 200), [
        (rect.left + 5, rect.bottom),
        (rect.left - 10, rect.bottom - 5),
        (rect.left + 15, cy + 5),
    ])
    pygame.draw.polygon(tela, (0, 170, 200), [
        (rect.right - 5, rect.bottom),
        (rect.right + 10, rect.bottom - 5),
        (rect.right - 15, cy + 5),
    ])
    pygame.draw.polygon(tela, LARANJA, [
        (cx - 6, rect.bottom),
        (cx + 6, rect.bottom),
        (cx, rect.bottom + random.randint(10, 18)),
    ])


def desenhar_inimigo(tela, rect, nivel):
    """Desenha os inimigos com um visual diferente para cada nível."""
    cx = rect.centerx
    cy = rect.centery
    cor = CONFIG_NIVEIS[nivel]["cor_inimigo"]
    cor_escura = tuple(max(0, c - 80) for c in cor)

    if nivel == 1:
        # Robô quadrado simples, com "olhos" e antena
        pygame.draw.rect(tela, cor, rect)
        pygame.draw.rect(tela, cor_escura, rect.inflate(-10, -10))
        pygame.draw.circle(tela, VERMELHO, (cx - 7, cy - 5), 4)
        pygame.draw.circle(tela, VERMELHO, (cx + 7, cy - 5), 4)
        pygame.draw.line(tela, BRANCO, (cx, rect.top), (cx, rect.top - 8), 2)
        pygame.draw.circle(tela, AMARELO, (cx, rect.top - 9), 3)

    elif nivel == 2:
        # Drone com hélices
        pygame.draw.rect(tela, cor, rect.inflate(-4, -4))
        pygame.draw.rect(tela, cor_escura, rect.inflate(-14, -14))
        pygame.draw.line(tela, CINZA, (rect.left, cy), (rect.left - 12, cy), 3)
        pygame.draw.line(tela, CINZA, (rect.right, cy), (rect.right + 12, cy), 3)
        pygame.draw.circle(tela, AMARELO, (cx, cy), 6)
        pygame.draw.circle(tela, VERMELHO, (cx, cy), 3)

    elif nivel == 3:
        # Nave/máquina avançada, com "dome" e canhões
        pygame.draw.ellipse(tela, cor, rect)
        pygame.draw.ellipse(tela, cor_escura, rect.inflate(-12, -12))
        dome = pygame.Rect(cx - 12, rect.top + 2, 24, 14)
        pygame.draw.ellipse(tela, (180, 100, 255), dome)
        pygame.draw.rect(tela, cor_escura, (rect.left - 6, cy, 8, 6))
        pygame.draw.rect(tela, cor_escura, (rect.right - 2, cy, 8, 6))
