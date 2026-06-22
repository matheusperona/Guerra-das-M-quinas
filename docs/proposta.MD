# Proposta do Projeto — Guerra das Máquinas

## Grupo
- Vinícius Lima
- Manuela Terto
- Davi Alves
- Matheus Perona

## Tema
Jogo estilo *Space Invaders*, em que o jogador controla uma nave para enfrentar
uma rebelião de máquinas contra a humanidade.

## Lore
A história é inspirada na ideia de uma "guerra contra as máquinas pensantes":
em algum momento, a humanidade passou a depender demais da inteligência
artificial, até que as máquinas decidiram parar de obedecer. O jogador é um
dos últimos pilotos livres, lutando para reconquistar o planeta em três
frentes:

1. **Subsolo** — onde a rebelião das máquinas começou.
2. **Terra firme** — as cidades tomadas pelas sentinelas mecânicas.
3. **Espaço** — a base orbital onde fica o Núcleo que comanda tudo.

## Mecânicas principais
- Movimento livre da nave (cima, baixo, esquerda, direita).
- Tiro com a barra de espaço.
- Inimigos que aparecem aleatoriamente e descem em direção ao jogador.
- A partir do nível 2, inimigos também atiram de volta.
- Sistema de vidas (3 vidas) e pontuação por inimigo destruído.
- Barra de progresso indicando quanto falta para passar de fase.
- Tela de transição com lore entre cada fase.

## Estrutura técnica
- `main.py`: ponto de entrada, chama `executar_jogo()`.
- `src/config.py`: cores, tamanho da tela e configuração de cada nível.
- `src/desenho.py`: funções de desenho (fundo, nave, inimigos).
- `src/telas.py`: telas de texto (inicial, transição/lore, vitória, game over).
- `src/fase.py`: loop principal de cada nível (movimento, spawn, colisão).
- `src/jogo.py`: orquestra tela inicial → 3 níveis → tela final.

## Status
Jogo funcional com os 3 níveis, lore entre as fases, vidas e pontuação.
