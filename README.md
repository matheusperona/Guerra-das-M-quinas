Guerra das Máquinas

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

Integrantes do grupo

Vinícius Lima,
Manuela Terto,
Davi Alves,
Matheus Perona

Estrutura do projeto

main.py: ponto de entrada da aplicação.
src/: código-fonte principal do jogo (loop, regras, sprites e dados).
assets/: imagens, fontes e sons.
data/: arquivos persistentes (recorde/ranking).
tests/: testes unitários com pytest.
docs/: documentação do projeto, incluindo proposta inicial.

Descrição do jogo

O jogo é inspirado em Space Invaders. Ele se passa durante uma guerra entre humanos e máquinas, em que o jogador controla uma nave para enfrentar os ataques inimigos e destruir obstáculos pelo mapa.

A aventura é dividida em três níveis, cada um com uma ambientação e dificuldade diferente. O primeiro nível acontece no subsolo, onde as máquinas iniciam o ataque e a dificuldade é menor. O segundo nível ocorre em terra firme, com desafios mais difíceis. O terceiro nível se passa no espaço, onde fica a base das máquinas e onde a dificuldade atinge nível máximo.

Objetivo do jogador

O objetivo do jogador é controlar a nave, destruir os obstáculos e inimigos do mapa, evitar ser destruído e avançar pelos três níveis do jogo: subsolo, terra firme e espaço.

Para vencer, o jogador precisa sobreviver aos ataques das máquinas e completar todos os níveis.

Regras do jogo

O jogador controla uma nave que pode se movimentar e atirar.
Os inimigos e obstáculos aparecem no mapa e devem ser destruídos.
Cada obstáculo ou inimigo destruído aumenta a pontuação do jogador.
O jogador deve evitar colisões e ataques das máquinas.
Se a nave do jogador for destruída, a partida termina.
Ao completar um nível, o jogador avança para o próximo cenário.
A dificuldade aumenta a cada nível, seguindo a ordem: subsolo, terra firme e espaço.

Controles

Seta para cima: mover para cima
Seta para baixo: mover para baixo
Seta para esquerda: mover para esquerda
Seta para direita: mover para direita
Espaço: atirar
ESC: sair do jogo

Como executar o projeto

1. Clonar o repositório
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
Como executar os testes
python -m pytest
Checklist mínimo para entrega

Preencher este README com nome final, descrição real, regras e controles do jogo.
Atualizar docs/proposta.MD com a proposta do grupo.
Garantir que o jogo executa com python main.py.
Garantir que os testes passam com pytest.

Observações para os alunos

Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
Comentem partes importantes da lógica, principalmente regras do jogo.
Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
