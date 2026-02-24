# Jogo MNK - Fundamentos da Programacao (FP)
Este foi o meu primeiro contacto com a programação. Contém alguns erros de implementação.

**Jogo MNK - Fundamentos da Programação**
Este projeto foi desenvolvido no âmbito da Unidade Curricular de Fundamentos da Programação (2024/25) no Instituto Superior Técnico. O objetivo é implementar um sistema de jogo em Python que permita a interação entre um jogador humano e o computador num tabuleiro de dimensões variáveis.

**O que é o Jogo MNK?**
O jogo m, n, k é uma generalização de jogos de tabuleiro abstratos como o Jogo do Galo ($3, 3, 3$) ou o Gomoku ($15, 15, 5$):
- m × n: Dimensões do tabuleiro (linhas × colunas).
- k: Número de pedras consecutivas necessárias para vencer.
- Vitória: O primeiro jogador a alinhar k pedras (horizontal, vertical ou diagonal) ganha a partida.

**Estratégias**
O programa implementa três níveis de dificuldade para o computador, utilizando diferentes heurísticas de decisão:
- Fácil: O computador joga de forma quase aleatória, priorizando posições adjacentes às suas próprias peças.
- Normal: Baseia-se em colocar ou bloquear peças consecutivas (L < k), tentando maximizar a sua vantagem ou impedir a do adversário.
- Difícil: Utiliza uma lógica mais avançada que combina a procura de vitória imediata com a simulação de jogos até ao fim para prever o melhor resultado possível (Vitória ou Empate).

O código python está explicado mais detalhadamente, função a função, no ficheiro pdf. Para o conseguir ler é necessário baixá-lo.
