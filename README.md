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

O jogo é inspirado em Space Invaders, com uma lore própria sobre uma guerra entre humanos e máquinas. O jogador controla uma nave para enfrentar sentinelas mecânicas que descem pela tela, atirando para destruí-las antes que colidam com a nave (e, a partir do nível 2, antes que os próprios inimigos atirem de volta).

A aventura é dividida em três níveis, cada um com uma ambientação, lore e dificuldade diferente. O primeiro nível acontece no subsolo, onde a rebelião das máquinas começou e a dificuldade é menor. O segundo nível ocorre em terra firme, nas cidades tomadas pelas sentinelas. O terceiro nível se passa no espaço, na base orbital onde fica o Núcleo que comanda as máquinas — aqui a dificuldade atinge o nível máximo. Antes de cada nível, uma tela de transição conta um pouco da história daquele trecho do jogo.

Objetivo do jogador

O objetivo do jogador é controlar a nave, destruir os inimigos que aparecem, evitar ser destruído e avançar pelos três níveis do jogo: subsolo, terra firme e espaço.

Para vencer, o jogador precisa sobreviver aos ataques das máquinas e completar todos os níveis sem perder as 3 vidas.

Regras do jogo

O jogador controla uma nave que pode se movimentar e atirar.
Os inimigos aparecem aleatoriamente no topo da tela e descem em direção ao jogador.
Cada inimigo destruído aumenta a pontuação do jogador.
O jogador começa com 3 vidas; cada colisão com inimigo ou tiro inimigo tira 1 vida.
Se as vidas chegarem a zero, a partida termina (game over).
Ao atingir a pontuação necessária, o jogador avança para o próximo nível.
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

Preencher este README com nome final, descrição real, regras e controles do jogo. ✅ feito
Atualizar docs/proposta.md com a proposta do grupo. ✅ feito
Garantir que o jogo executa com python main.py. (testar antes de entregar)
Garantir que os testes passam com pytest. ⚠️ ainda não há testes — confirmar com o professor se isso é exigido na entrega de hoje.

Observações para os alunos

Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
Comentem partes importantes da lógica, principalmente regras do jogo.
Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
