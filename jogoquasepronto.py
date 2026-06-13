import pygame
import time
import random

# === CONFIGURAÇÕES ===
largura = 800
altura = 600
speed = 60

pygame.init()
fonte = pygame.font.SysFont(None, 35)
fonte_grande = pygame.font.SysFont(None, 70)
fonte_media = pygame.font.SysFont(None, 45)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Guerra das Máquinas!')
relogio = pygame.time.Clock()

# === CORES ===
preto        = (0, 0, 0)
branco       = (225, 225, 225)
azul_claro   = (0, 225, 225)
vermelho     = (255, 50, 50)
amarelo      = (255, 220, 0)
cinza        = (100, 100, 100)
laranja      = (255, 140, 0)
roxo         = (140, 0, 200)
verde        = (0, 200, 50)
azul_escuro  = (10, 10, 60)
marrom       = (80, 50, 20)
marrom_claro = (120, 80, 40)
cinza_escuro = (30, 30, 30)

# === CONFIGURAÇÕES POR NÍVEL ===
config_niveis = {
    1: {
        "nome": "Nível 1 — Subsolo",
        "vel_inimigo": 1.2,
        "freq_inimigos": 1200,
        "vel_laser": 10,
        "inimigos_atiram": False,
        "freq_tiro_inimigo": 0,
        "vel_tiro_inimigo": 0,
        "score_para_avancar": 80,
        "cor_inimigo": vermelho,
        "max_inimigos_tela": 6,
    },
    2: {
        "nome": "Nível 2 — Terra Firme",
        "vel_inimigo": 2.0,
        "freq_inimigos": 900,
        "vel_laser": 12,
        "inimigos_atiram": True,
        "freq_tiro_inimigo": 2500,
        "vel_tiro_inimigo": 5,
        "score_para_avancar": 200,
        "cor_inimigo": laranja,
        "max_inimigos_tela": 8,
    },
    3: {
        "nome": "Nível 3 — Espaço",
        "vel_inimigo": 2.8,
        "freq_inimigos": 650,
        "vel_laser": 14,
        "inimigos_atiram": True,
        "freq_tiro_inimigo": 1500,
        "vel_tiro_inimigo": 7,
        "score_para_avancar": 999999,  # sem limite, jogador vence destruindo tudo
        "cor_inimigo": roxo,
        "max_inimigos_tela": 10,
    },
}

# === ESTRELAS (fundo do espaço) ===
estrelas = [(random.randint(0, largura), random.randint(0, altura)) for _ in range(120)]


def desenhar_fundo(nivel):
    """Desenha o fundo temático de cada nível."""
    if nivel == 1:
        # Subsolo: fundo escuro com linhas de terra
        tela.fill((15, 10, 5))
        for i in range(0, largura, 60):
            pygame.draw.line(tela, (40, 25, 10), (i, 0), (i, altura), 1)
        for j in range(0, altura, 80):
            pygame.draw.line(tela, (40, 25, 10), (0, j), (largura, j), 1)
        # Rochas decorativas
        for rx, ry, rw, rh in [(50,150,70,30),(300,350,90,25),(600,200,60,20),(150,480,80,25),(700,400,50,20)]:
            pygame.draw.ellipse(tela, marrom_claro, (rx, ry, rw, rh))
            pygame.draw.ellipse(tela, marrom, (rx+5, ry+5, rw-10, rh-10))

    elif nivel == 2:
        # Terra firme: céu noturno com chão
        tela.fill((10, 15, 30))
        # Chão
        pygame.draw.rect(tela, (30, 60, 20), (0, altura - 60, largura, 60))
        pygame.draw.rect(tela, (20, 45, 15), (0, altura - 65, largura, 8))
        # Prédios destruídos ao fundo
        predios = [(50,350,60,200),(150,300,80,260),(350,320,70,240),(550,280,90,280),(700,340,70,220)]
        for px, py, pw, ph in predios:
            pygame.draw.rect(tela, (25, 25, 35), (px, py, pw, ph))
            pygame.draw.rect(tela, (35, 35, 50), (px+5, py+10, pw-10, ph-10))
            # Janelas apagadas
            for wx in range(px+8, px+pw-8, 15):
                for wy in range(py+15, py+ph-15, 20):
                    if random.random() > 0.7:
                        pygame.draw.rect(tela, (60, 55, 20), (wx, wy, 8, 8))
        # Estrelas esparsas
        for ex, ey in estrelas[:40]:
            pygame.draw.circle(tela, branco, (ex, ey % (altura - 80)), 1)

    elif nivel == 3:
        # Espaço: fundo escuro estrelado com nebulosa sutil
        tela.fill((2, 2, 15))
        # Nebulosa
        for nx in range(0, largura, 4):
            for ny in range(0, altura, 4):
                d = ((nx - 400)**2 + (ny - 200)**2) ** 0.5
                if d < 180:
                    alpha = max(0, int(18 - d / 10))
                    pygame.draw.rect(tela, (alpha, 0, alpha * 2), (nx, ny, 4, 4))
        # Estrelas
        for ex, ey in estrelas:
            pygame.draw.circle(tela, branco, (ex, ey), 1)
        # Planeta ao fundo
        pygame.draw.circle(tela, (40, 40, 80), (660, 120), 70)
        pygame.draw.circle(tela, (55, 55, 110), (660, 120), 65)
        pygame.draw.ellipse(tela, (80, 80, 140), (590, 110, 140, 20))


def desenhar_player(rect):
    """Desenha a nave do jogador."""
    cx = rect.centerx
    cy = rect.centery
    # Corpo principal
    pygame.draw.polygon(tela, azul_claro, [
        (cx, rect.top),
        (rect.left + 5, rect.bottom),
        (rect.right - 5, rect.bottom)
    ])
    # Cockpit
    pygame.draw.polygon(tela, branco, [
        (cx, rect.top + 8),
        (cx - 8, rect.centery),
        (cx + 8, rect.centery)
    ])
    # Asas
    pygame.draw.polygon(tela, (0, 170, 200), [
        (rect.left + 5, rect.bottom),
        (rect.left - 10, rect.bottom - 5),
        (rect.left + 15, rect.centery + 5)
    ])
    pygame.draw.polygon(tela, (0, 170, 200), [
        (rect.right - 5, rect.bottom),
        (rect.right + 10, rect.bottom - 5),
        (rect.right - 15, rect.centery + 5)
    ])
    # Chama do motor
    pygame.draw.polygon(tela, laranja, [
        (cx - 6, rect.bottom),
        (cx + 6, rect.bottom),
        (cx, rect.bottom + random.randint(10, 18))
    ])


def desenhar_inimigo(rect, nivel):
    """Desenha os inimigos com visual diferente por nível."""
    cx = rect.centerx
    cy = rect.centery
    cor = config_niveis[nivel]["cor_inimigo"]
    cor_escura = tuple(max(0, c - 80) for c in cor)

    if nivel == 1:
        # Robô quadrado simples
        pygame.draw.rect(tela, cor, rect)
        pygame.draw.rect(tela, cor_escura, rect.inflate(-10, -10))
        # Olhos
        pygame.draw.circle(tela, vermelho, (cx - 7, cy - 5), 4)
        pygame.draw.circle(tela, vermelho, (cx + 7, cy - 5), 4)
        # Antena
        pygame.draw.line(tela, branco, (cx, rect.top), (cx, rect.top - 8), 2)
        pygame.draw.circle(tela, amarelo, (cx, rect.top - 9), 3)

    elif nivel == 2:
        # Drone mais elaborado
        pygame.draw.rect(tela, cor, rect.inflate(-4, -4))
        pygame.draw.rect(tela, cor_escura, rect.inflate(-14, -14))
        # Hélices
        pygame.draw.line(tela, cinza, (rect.left, cy), (rect.left - 12, cy), 3)
        pygame.draw.line(tela, cinza, (rect.right, cy), (rect.right + 12, cy), 3)
        pygame.draw.circle(tela, amarelo, (cx, cy), 6)
        pygame.draw.circle(tela, vermelho, (cx, cy), 3)

    elif nivel == 3:
        # Nave alienígena/máquina avançada
        pygame.draw.ellipse(tela, cor, rect)
        pygame.draw.ellipse(tela, cor_escura, rect.inflate(-12, -12))
        # Dome
        dome = pygame.Rect(cx - 12, rect.top + 2, 24, 14)
        pygame.draw.ellipse(tela, (180, 100, 255), dome)
        # Canhões
        pygame.draw.rect(tela, cor_escura, (rect.left - 6, cy, 8, 6))
        pygame.draw.rect(tela, cor_escura, (rect.right - 2, cy, 8, 6))


def tela_transicao(nivel):
    """Exibe tela de transição entre níveis."""
    for alpha in range(0, 256, 5):
        surf = pygame.Surface((largura, altura))
        surf.fill(preto)
        surf.set_alpha(alpha)
        tela.blit(surf, (0, 0))
        pygame.display.flip()
        pygame.time.delay(15)

    tela.fill(preto)
    if nivel <= 3:
        msg1 = fonte_grande.render(config_niveis[nivel]["nome"], True, azul_claro)
        msg2 = fonte_media.render("Prepare-se!", True, branco)
        tela.blit(msg1, (largura // 2 - msg1.get_width() // 2, altura // 2 - 60))
        tela.blit(msg2, (largura // 2 - msg2.get_width() // 2, altura // 2 + 20))
    pygame.display.flip()
    time.sleep(2)


def tela_vitoria():
    tela.fill(preto)
    v1 = fonte_grande.render("VITÓRIA!", True, amarelo)
    v2 = fonte_media.render("Você destruiu a base das máquinas!", True, branco)
    tela.blit(v1, (largura // 2 - v1.get_width() // 2, altura // 2 - 60))
    tela.blit(v2, (largura // 2 - v2.get_width() // 2, altura // 2 + 20))
    pygame.display.flip()
    time.sleep(4)


def tela_game_over(score):
    tela.fill(preto)
    go = fonte_grande.render("GAME OVER", True, vermelho)
    sc = fonte_media.render(f"Pontuação Final: {score}", True, branco)
    tela.blit(go, (largura // 2 - go.get_width() // 2, altura // 2 - 60))
    tela.blit(sc, (largura // 2 - sc.get_width() // 2, altura // 2 + 20))
    pygame.display.flip()
    time.sleep(3)


def jogar_nivel(nivel, score_inicial, vidas_iniciais):
    cfg = config_niveis[nivel]

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
        if teclas[pygame.K_UP]:    player_rect.y -= 5
        if teclas[pygame.K_DOWN]:  player_rect.y += 5
        if teclas[pygame.K_LEFT]:  player_rect.x -= 5
        if teclas[pygame.K_RIGHT]: player_rect.x += 5

        # Limites da tela
        player_rect.x = max(5, min(player_rect.x, largura - player_rect.width - 5))
        player_rect.y = max(35, min(player_rect.y, altura - player_rect.height - 5))

        # === SPAWN DE INIMIGOS ===
        if (tempo_atual - tempo_ultimo_inimigo > cfg["freq_inimigos"]
                and len(sentinelas) < cfg["max_inimigos_tela"]):
            x_aleatorio = random.randint(10, largura - 50)
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
            if tiro.top > altura:
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
            if inimigo.top > altura:
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
                    if inimigo in sentinelas: sentinelas.remove(inimigo)
                    if laser in lasers: lasers.remove(laser)
                    score += 10
                    break

        # === CONDIÇÃO DE AVANÇO ===
        if score >= cfg["score_para_avancar"]:
            vitoria_nivel = True
            rodando = False

        # === DESENHO ===
        desenhar_fundo(nivel)
        desenhar_player(player_rect)

        for laser in lasers:
            pygame.draw.rect(tela, azul_claro, laser)
            pygame.draw.rect(tela, branco, laser.inflate(2, 2), 1)

        for inimigo in sentinelas:
            desenhar_inimigo(inimigo, nivel)

        for tiro in tiros_inimigos:
            pygame.draw.rect(tela, amarelo, tiro)

        # HUD
        texto_score = fonte.render(f'Pontuação: {score}', True, branco)
        texto_nivel = fonte.render(cfg["nome"], True, azul_claro)
        texto_vidas = fonte.render(f'Vidas: {"❤ " * vidas}', True, vermelho)
        tela.blit(texto_score, (10, 10))
        tela.blit(texto_nivel, (largura // 2 - texto_nivel.get_width() // 2, 10))
        tela.blit(texto_vidas, (largura - texto_vidas.get_width() - 10, 10))

        # Barra de progresso (nível 1 e 2)
        if cfg["score_para_avancar"] < 999999:
            prog = min(score / cfg["score_para_avancar"], 1.0)
            pygame.draw.rect(tela, cinza, (10, altura - 18, largura - 20, 10), 1)
            pygame.draw.rect(tela, verde, (11, altura - 17, int((largura - 22) * prog), 8))
            label = fonte.render("Progresso", True, cinza)
            tela.blit(label, (10, altura - 35))

        relogio.tick(speed)
        pygame.display.flip()

    if vitoria_nivel:
        return score, vidas, "vitoria"
    return score, vidas, "game_over"


# === TELA INICIAL ===
def tela_inicial():
    tela.fill(preto)
    t1 = fonte_grande.render("GUERRA DAS MÁQUINAS", True, azul_claro)
    t2 = fonte_media.render("Pressione ENTER para começar", True, branco)
    t3 = fonte.render("ESC para sair", True, cinza)
    t4 = fonte.render("Setas: mover   |   Espaço: atirar", True, cinza)
    tela.blit(t1, (largura // 2 - t1.get_width() // 2, 180))
    tela.blit(t2, (largura // 2 - t2.get_width() // 2, 290))
    tela.blit(t3, (largura // 2 - t3.get_width() // 2, 360))
    tela.blit(t4, (largura // 2 - t4.get_width() // 2, 410))
    # Estrelas no fundo da tela inicial
    for ex, ey in estrelas[:60]:
        pygame.draw.circle(tela, branco, (ex, ey), 1)
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
    return False


# === LOOP PRINCIPAL ===
if not tela_inicial():
    pygame.quit()
    exit()

score = 0
vidas = 3
resultado_final = "game_over"

for nivel in range(1, 4):
    tela_transicao(nivel)
    score, vidas, resultado = jogar_nivel(nivel, score, vidas)

    if resultado == "sair":
        break
    elif resultado == "game_over":
        tela_game_over(score)
        break
    elif resultado == "vitoria":
        if nivel == 3:
            resultado_final = "vitoria"
            tela_vitoria()
        # senão, continua para o próximo nível

pygame.quit()