"""
Lógica de uma fase (nível) do jogo: movimento do jogador, spawn de inimigos,
tiros, colisões e condição de vitória/derrota daquele nível.
"""
import random
import pygame
from src.config import LARGURA, ALTURA, VELOCIDADE_FPS, PRETO, BRANCO, AZUL_CLARO, AMARELO, VERMELHO, CINZA, VERDE, CONFIG_NIVEIS
from src.desenho import desenhar_fundo, desenhar_player, desenhar_inimigo


def jogar_nivel(tela, relogio, fonte, nivel, score_inicial, vidas_iniciais):
    """
    Roda o loop daquele nível até o jogador vencer, perder ou sair.
    Retorna (score, vidas, resultado), onde resultado é "vitoria", "game_over" ou "sair".
    """
    cfg = CONFIG_NIVEIS[nivel]

    player_rect = pygame.Rect(375, 500, 50, 50)
    lasers = []
    sentinelas = []
    tiros_inimigos = []
    score = score_inicial
    vidas = vidas_iniciais

    tempo_ultimo_inimigo = 0
    tempo_ultimo_tiro_inimigo = 0

    rodando = True
    vitoria_nivel = False

    while rodando:
        tempo_atual = pygame.time.get_ticks()

        # === EVENTOS ===
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return score, vidas, "sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return score, vidas, "sair"
                if evento.key == pygame.K_SPACE:
                    novo_laser = pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 15)
                    lasers.append(novo_laser)

        # === MOVIMENTO DO PLAYER ===
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            player_rect.y -= 5
        if teclas[pygame.K_DOWN]:
            player_rect.y += 5
        if teclas[pygame.K_LEFT]:
            player_rect.x -= 5
        if teclas[pygame.K_RIGHT]:
            player_rect.x += 5

        # Limites da tela
        player_rect.x = max(5, min(player_rect.x, LARGURA - player_rect.width - 5))
        player_rect.y = max(35, min(player_rect.y, ALTURA - player_rect.height - 5))

        # === SPAWN DE INIMIGOS ===
        if (tempo_atual - tempo_ultimo_inimigo > cfg["freq_inimigos"]
                and len(sentinelas) < cfg["max_inimigos_tela"]):
            x_aleatorio = random.randint(10, LARGURA - 50)
            novo_inimigo = pygame.Rect(x_aleatorio, -45, 40, 40)
            sentinelas.append(novo_inimigo)
            tempo_ultimo_inimigo = tempo_atual

        # === TIRO DOS INIMIGOS ===
        if cfg["inimigos_atiram"] and sentinelas:
            if tempo_atual - tempo_ultimo_tiro_inimigo > cfg["freq_tiro_inimigo"]:
                atirador = random.choice(sentinelas)
                tiro = pygame.Rect(atirador.centerx - 2, atirador.bottom, 4, 12)
                tiros_inimigos.append(tiro)
                tempo_ultimo_tiro_inimigo = tempo_atual

        # === ATUALIZAR LASERS DO PLAYER ===
        for laser in lasers[:]:
            laser.y -= cfg["vel_laser"]
            if laser.bottom < 0:
                lasers.remove(laser)

        # === ATUALIZAR TIROS INIMIGOS ===
        for tiro in tiros_inimigos[:]:
            tiro.y += cfg["vel_tiro_inimigo"]
            if tiro.top > ALTURA:
                tiros_inimigos.remove(tiro)
                continue
            if player_rect.colliderect(tiro):
                tiros_inimigos.remove(tiro)
                vidas -= 1
                if vidas <= 0:
                    return score, 0, "game_over"

        # === ATUALIZAR INIMIGOS ===
        for inimigo in sentinelas[:]:
            inimigo.y += cfg["vel_inimigo"]
            if inimigo.top > ALTURA:
                sentinelas.remove(inimigo)
                continue
            # Colisão com player
            if player_rect.colliderect(inimigo):
                sentinelas.remove(inimigo)
                vidas -= 1
                if vidas <= 0:
                    return score, 0, "game_over"
                continue
            # Colisão com laser
            for laser in lasers[:]:
                if laser.colliderect(inimigo):
                    if inimigo in sentinelas:
                        sentinelas.remove(inimigo)
                    if laser in lasers:
                        lasers.remove(laser)
                    score += 10
                    break

        # === CONDIÇÃO DE AVANÇO ===
        if score >= cfg["score_para_avancar"]:
            vitoria_nivel = True
            rodando = False

        # === DESENHO ===
        desenhar_fundo(tela, nivel)
        desenhar_player(tela, player_rect)

        for laser in lasers:
            pygame.draw.rect(tela, AZUL_CLARO, laser)
            pygame.draw.rect(tela, BRANCO, laser.inflate(2, 2), 1)

        for inimigo in sentinelas:
            desenhar_inimigo(tela, inimigo, nivel)

        for tiro in tiros_inimigos:
            pygame.draw.rect(tela, AMARELO, tiro)

        # HUD
        texto_score = fonte.render(f'Pontuação: {score}', True, BRANCO)
        texto_nivel = fonte.render(cfg["nome"], True, AZUL_CLARO)
        texto_vidas = fonte.render(f'Vidas: {"❤ " * vidas}', True, VERMELHO)
        tela.blit(texto_score, (10, 10))
        tela.blit(texto_nivel, (LARGURA // 2 - texto_nivel.get_width() // 2, 10))
        tela.blit(texto_vidas, (LARGURA - texto_vidas.get_width() - 10, 10))

        # Barra de progresso (níveis 1 e 2; nível 3 não tem limite fixo)
        if cfg["score_para_avancar"] < 999999:
            prog = min(score / cfg["score_para_avancar"], 1.0)
            pygame.draw.rect(tela, CINZA, (10, ALTURA - 18, LARGURA - 20, 10), 1)
            pygame.draw.rect(tela, VERDE, (11, ALTURA - 17, int((LARGURA - 22) * prog), 8))
            label = fonte.render("Progresso", True, CINZA)
            tela.blit(label, (10, ALTURA - 35))

        relogio.tick(VELOCIDADE_FPS)
        pygame.display.flip()

    if vitoria_nivel:
        return score, vidas, "vitoria"
    return score, vidas, "game_over"
