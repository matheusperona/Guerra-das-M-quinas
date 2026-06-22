"""
Telas de texto do jogo: tela inicial, transição entre níveis (com a lore),
tela de vitória e tela de game over.
"""
import time
import pygame
from src.config import (
    LARGURA, ALTURA, PRETO, BRANCO, AZUL_CLARO, VERMELHO, AMARELO, CINZA,
    CONFIG_NIVEIS, LORE_NIVEIS,
)
from src.desenho import ESTRELAS


def tela_inicial(tela, relogio, fontes):
    """Mostra o título e espera o jogador apertar ENTER para começar."""
    fonte, fonte_media, fonte_grande = fontes

    tela.fill(PRETO)
    t1 = fonte_grande.render("GUERRA DAS MÁQUINAS", True, AZUL_CLARO)
    t2 = fonte_media.render("Pressione ENTER para começar", True, BRANCO)
    t3 = fonte.render("ESC para sair", True, CINZA)
    t4 = fonte.render("Setas: mover   |   Espaço: atirar", True, CINZA)

    tela.blit(t1, (LARGURA // 2 - t1.get_width() // 2, 180))
    tela.blit(t2, (LARGURA // 2 - t2.get_width() // 2, 290))
    tela.blit(t3, (LARGURA // 2 - t3.get_width() // 2, 360))
    tela.blit(t4, (LARGURA // 2 - t4.get_width() // 2, 410))

    for ex, ey in ESTRELAS[:60]:
        pygame.draw.circle(tela, BRANCO, (ex, ey), 1)
    pygame.display.flip()

    aguardando = True
    while aguardando:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    return True
                if ev.key == pygame.K_ESCAPE:
                    return False
        relogio.tick(30)
    return False


def tela_transicao(tela, relogio, fontes, nivel):
    """
    Tela exibida antes de cada nível começar.
    Mostra o nome da fase e a lore (história) daquele trecho do jogo.
    Pressione ENTER para avançar (ou espera alguns segundos).
    """
    fonte, fonte_media, fonte_grande = fontes

    # Fade para preto
    for alpha in range(0, 256, 15):
        surf = pygame.Surface((LARGURA, ALTURA))
        surf.fill(PRETO)
        surf.set_alpha(alpha)
        tela.blit(surf, (0, 0))
        pygame.display.flip()
        pygame.time.delay(10)

    linhas_lore = LORE_NIVEIS.get(nivel, [])
    nome_nivel = CONFIG_NIVEIS[nivel]["nome"]

    tela.fill(PRETO)
    titulo = fonte_grande.render(nome_nivel, True, AZUL_CLARO)
    tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 60))

    y = 160
    for linha in linhas_lore:
        texto = fonte.render(linha, True, BRANCO)
        tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, y))
        y += 32

    aviso = fonte.render("Pressione ENTER para continuar", True, CINZA)
    tela.blit(aviso, (LARGURA // 2 - aviso.get_width() // 2, ALTURA - 50))
    pygame.display.flip()

    # Espera ENTER, mas também avança sozinho depois de um tempo (evita travar a apresentação)
    tempo_inicio = pygame.time.get_ticks()
    aguardando = True
    while aguardando:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return "sair"
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    aguardando = False
                if ev.key == pygame.K_ESCAPE:
                    return "sair"
        if pygame.time.get_ticks() - tempo_inicio > 6000:  # 6s e avança sozinho
            aguardando = False
        relogio.tick(30)

    return "ok"


def tela_vitoria(tela, fonte_media, fonte_grande):
    tela.fill(PRETO)
    v1 = fonte_grande.render("VITÓRIA!", True, AMARELO)
    v2 = fonte_media.render("Você destruiu o Núcleo das máquinas!", True, BRANCO)
    tela.blit(v1, (LARGURA // 2 - v1.get_width() // 2, ALTURA // 2 - 60))
    tela.blit(v2, (LARGURA // 2 - v2.get_width() // 2, ALTURA // 2 + 20))
    pygame.display.flip()
    time.sleep(4)


def tela_game_over(tela, fonte_media, fonte_grande, score):
    tela.fill(PRETO)
    go = fonte_grande.render("GAME OVER", True, VERMELHO)
    sc = fonte_media.render(f"Pontuação Final: {score}", True, BRANCO)
    tela.blit(go, (LARGURA // 2 - go.get_width() // 2, ALTURA // 2 - 60))
    tela.blit(sc, (LARGURA // 2 - sc.get_width() // 2, ALTURA // 2 + 20))
    pygame.display.flip()
    time.sleep(3)
