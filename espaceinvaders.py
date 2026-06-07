import pygame 
import time
import random 


largura=800
altura=600
speed=60
pygame.init()
fonte=pygame.font.SysFont(None, 35)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Guerra das máquinas!')
relogio = pygame.time.Clock()


# Cores
preto = (0, 0, 0)
branco=(225, 225, 225)
azul_claro=(0,225,225)
vermelho=(255, 0, 0) 

#posição do player
player_rect = pygame.Rect(400, 500, 50, 50) 

lasers=[]
velocidade_laser=10
shoot=True

sentinelas=[]
velocidade_inimigo = 1.5
tempo_ultimo_inimigo = 0
frequencia_inimigos = 1000
score=0

# Loop principal do jogo
fim_jogo=False
while not fim_jogo:
    tempo_atual = pygame.time.get_ticks()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo=True

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                novo_laser = pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 15)
                lasers.append(novo_laser)

    #movimentação com teclas 
    teclas = pygame.key.get_pressed()
    
    # Movimentação vertical (Cima / Baixo)
    if teclas[pygame.K_UP]:
        player_rect.y -= 5
    if teclas[pygame.K_DOWN]:
        player_rect.y += 5  
        
    # Movimentação horizontal (Esquerda / Direita)
    if teclas[pygame.K_LEFT]:
        player_rect.x -= 5
    if teclas[pygame.K_RIGHT]:
        player_rect.x += 5  
    
#travar o jogador
    if player_rect.x < 40:
        player_rect.x = 40
    if player_rect.x > 760:
        player_rect.x = 760
    if player_rect.y < 35:
        player_rect.y = 35
    if player_rect.y > 520:
        player_rect.y = 520


    if tempo_atual-tempo_ultimo_inimigo > frequencia_inimigos:
        # Gera um X aleatório para o inimigo não nascer fora da tela
        x_aleatorio = random.randint(0, largura - 40)
        novo_inimigo = pygame.Rect(x_aleatorio, -40, 40, 40)  # Nasce um pouco acima da tela
        sentinelas.append(novo_inimigo)
        tempo_ultimo_inimigo = tempo_atual
    for laser in lasers:
        laser.y -= velocidade_laser 
        
    # Remove os lasers que saíram da tela (para não pesar o jogo)
    for laser in lasers[:]:#remover os intens da lista
        if laser.bottom < 0:
            lasers.remove(laser)

    for inimigo in sentinelas[:]:
        inimigo.y += velocidade_inimigo
        
        # Se o inimigo passar da parte de baixo da tela, ele desaparece
        if inimigo.top > altura:
            sentinelas.remove(inimigo)
            continue
            
        # COLISÃO
        if player_rect.colliderect(inimigo):
            fim_jogo = True

        # COLISÃO: Laser bateu no inimigo
        for laser in lasers[:]:#remove itens da lista
            if laser.colliderect(inimigo):
                # Se o laser bateu, removemos o inimigo e o laser, e somamos pontos
                if inimigo in sentinelas: sentinelas.remove(inimigo)
                if laser in lasers: lasers.remove(laser)
                score += 10
    tela.fill(preto) 
    

    pygame.draw.rect(tela, azul_claro, player_rect)#quadrado verde 
    for laser in lasers:
        pygame.draw.rect(tela, branco, laser)
    for inimigo in sentinelas:
        pygame.draw.rect(tela, vermelho, inimigo)

    texto_score = fonte.render(f'Pontuação: {score}', True, branco)
    tela.blit(texto_score, (10, 10))

    relogio.tick(speed)
    pygame.display.flip()
#game over
tela.fill(preto)
mensagem= fonte.render('GAME OVER', True, branco)
tela.blit(mensagem, (largura/2 - 70, altura/2 - 20))
pygame.display.flip()
time.sleep(3)
pygame.quit()
