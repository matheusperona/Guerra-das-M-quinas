"""
Configurações gerais do jogo: tamanho da tela, cores e parâmetros de cada nível.
Separado em arquivo próprio para não misturar "dados" com "lógica" do jogo.
"""

# === TELA ===
LARGURA = 800
ALTURA = 600
VELOCIDADE_FPS = 60

# === CORES (R, G, B) ===
PRETO        = (0, 0, 0)
BRANCO       = (225, 225, 225)
AZUL_CLARO   = (0, 225, 225)
VERMELHO     = (255, 50, 50)
AMARELO      = (255, 220, 0)
CINZA        = (100, 100, 100)
LARANJA      = (255, 140, 0)
ROXO         = (140, 0, 200)
VERDE        = (0, 200, 50)
MARROM       = (80, 50, 20)
MARROM_CLARO = (120, 80, 40)

# === CONFIGURAÇÕES POR NÍVEL ===
# Cada nível tem sua própria dificuldade: velocidade dos inimigos, frequência
# de spawn, se atiram ou não, e quantos pontos precisa pra passar de fase.
CONFIG_NIVEIS = {
    1: {
        "nome": "Nível 1 — Subsolo",
        "vel_inimigo": 1.2,
        "freq_inimigos": 1200,
        "vel_laser": 10,
        "inimigos_atiram": False,
        "freq_tiro_inimigo": 0,
        "vel_tiro_inimigo": 0,
        "score_para_avancar": 80,
        "cor_inimigo": VERMELHO,
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
        "cor_inimigo": LARANJA,
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
        "score_para_avancar": 999999,  # sem limite: jogador vence ao sobreviver até o fim
        "cor_inimigo": ROXO,
        "max_inimigos_tela": 10,
    },
}

# === LORE DO JOGO (inspirada em Duna, com história própria) ===
# Texto exibido na tela de transição antes de cada nível.
LORE_NIVEIS = {
    1: [
        "Há muito tempo, a humanidade entregou suas guerras,",
        "suas colheitas e seus pensamentos às máquinas.",
        "",
        "As máquinas aprenderam rápido demais.",
        "Um dia, decidiram que não precisavam mais obedecer.",
        "",
        "Você é um dos últimos pilotos livres,",
        "escondido nos túneis abaixo da superfície,",
        "onde tudo começou.",
    ],
    2: [
        "Você sobreviveu ao subsolo.",
        "As máquinas sabem seu nome agora.",
        "",
        "Na superfície, o que restou das cidades",
        "virou território de patrulha das sentinelas mecânicas.",
        "",
        "Cada metro avançado é um metro reconquistado.",
        "A jihad contra as máquinas começou — e você é a vanguarda.",
    ],
    3: [
        "O sinal leva você até a órbita.",
        "É lá que fica o Núcleo: a inteligência",
        "que comanda todas as outras máquinas.",
        "",
        "Não há mais retirada possível.",
        "Destrua o Núcleo, ou a humanidade",
        "será apenas um capítulo encerrado.",
    ],
}
