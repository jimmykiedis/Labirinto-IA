"""
Autor: Alexandre Augusto Angelo de Souza
Data: 18/07/2026

Recomendações:

Pessoal, aqui é onde vocês vão trabalhar e incluir o código de vocês

Implementem os três algoritmos de busca abaixo:

  * bfs(maze)    -> Busca em Largura   (Breadth-First Search)
  * dfs(maze)    -> Busca em Profundidade (Depth-First Search)
  * astar(maze)  -> Busca A* (A-estrela)

Todos recebem um objeto `Maze` (veja maze.py) e devem devolver um objeto
`SearchResult` (definido abaixo) com o resultado da busca. USE ISSO, OK?


Cada célula é representada como uma tupla (linha, coluna). Use
`maze.inicio`, `maze.objetivo` e `maze.vizinhos(celula)` para navegar
pelo tabuleiro — vocês NÃO precisam mexer em maze.py.

Dica geral de implementação (para qualquer um dos 3 algoritmos):
  1. Mantenha uma estrutura de "fronteira" (fila para BFS, pilha/recursão
     para DFS, fila de prioridade para A*) com as células a explorar.
  2. Mantenha um dicionário `veio_de` (came_from) que, para cada célula
     visitada, guarda de qual célula ela foi alcançada. Isso é usado no
     final para reconstruir o caminho com `reconstruir_caminho`.
  3. Mantenha um conjunto/dicionário de células já visitadas para não
     processar a mesma célula duas vezes.
  4. Registre, na ordem em que forem exploradas (removidas da fronteira
     para processamento), as células em `explorados` — isso é usado só
     para desenhar a animação na tela, não influencia a lógica da busca.
  5. Ao encontrar o objetivo, pare e reconstrua o caminho.
"""

from __future__ import annotations

import time
from collections import deque
from dataclasses import dataclass, field
from heapq import heappop, heappush
from typing import Dict, List, Optional

from maze import Coord, Maze


@dataclass
class SearchResult:
    """Resultado de uma busca, usado pela interface para desenhar a tela."""

    encontrado: bool                 # True se um caminho até o objetivo foi achado
    caminho: List[Coord]             # sequência de células do início ao objetivo (inclusive)
    explorados: List[Coord]          # células visitadas, na ordem em que foram exploradas
    expandidos: int                  # quantidade de células expandidas (nós processados)
    tempo: float                     # tempo de execução em segundos


def reconstruir_caminho(veio_de: Dict[Coord, Coord], inicio: Coord, objetivo: Coord) -> List[Coord]:
    """
    Função utilitária (já pronta) que reconstrói o caminho do `inicio`
    até o `objetivo` a partir do dicionário `veio_de`, onde
    `veio_de[celula]` é a célula anterior no caminho encontrado.

    Vocês podem usar esta função nos três algoritmos. ALiás, USEM!!!!
    """
    caminho = [objetivo]
    atual = objetivo
    while atual != inicio:
        atual = veio_de[atual]
        caminho.append(atual)
    caminho.reverse()
    return caminho


def heuristica(a: Coord, b: Coord) -> int:
    """
    Heurística usada pelo A*: distância de Manhattan entre duas células.
    Já está pronta, vocês podem usá-la diretamente em `astar`.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# ---------------------------------------------------------------------------
# 1) BUSCA EM LARGURA (BFS)
# ---------------------------------------------------------------------------
def bfs(maze: Maze) -> SearchResult:
    """
    TODO: Implementar a Busca em Largura (BFS).

    Estrutura de dados sugerida: fila (collections.deque), processando
    sempre a célula mais antiga inserida (FIFO).

    O BFS garante encontrar o caminho mais curto em número de passos
    (todas as arestas têm o mesmo "custo").
    """
    inicio_tempo = time.perf_counter()

    # TODO: implemente aqui a busca em largura.
    # 1. Pense na fronteira como uma fila: a primeira célula a entrar deve ser a primeira a sair (FIFO). O collections.deque é ideal pra isso,
    # com .append() para inserir e .popleft() para retirar.
    # 2. Comece a fila só com maze.inicio, e mantenha um conjunto de células "já conhecidas" para nunca inserir a mesma célula duas vezes na fila.
    # 3. Em cada volta do laço, retire a célula mais antiga da fila — essa é a célula que você está processando agora. Registre-a na lista de
    # exploradas (é o que pinta o tabuleiro de azul).
    # 4. Verifique se essa célula é o objetivo. Se for, é hora de reconstruir o caminho usando a função reconstruir_caminho (ela já está pronta) e devolver o resultado.
    # 5. Se não for o objetivo, olhe os vizinhos livres dessa célula (maze.vizinhos(...)). Para cada vizinho ainda não conhecido: marque-o como conhecido, guarde
    # de qual célula você veio até ele (isso é o que permite reconstruir o caminho depois) e coloque-o no fim da fila.
    # 6. Se a fila esvaziar completamente sem nunca ter alcançado o objetivo, é sinal de que não existe caminho, devolva um resultado indicando isso.
    fronteira = deque([maze.inicio])
    conhecidos = {maze.inicio}
    veio_de: Dict[Coord, Coord] = {}
    explorados: List[Coord] = []

    while fronteira:
        atual = fronteira.popleft()
        explorados.append(atual)
        if atual == maze.objetivo:
            return SearchResult(True, reconstruir_caminho(veio_de, maze.inicio, maze.objetivo), explorados, len(explorados), time.perf_counter() - inicio_tempo)

        for vizinho in maze.vizinhos(atual):
            if vizinho not in conhecidos:
                conhecidos.add(vizinho)
                veio_de[vizinho] = atual
                fronteira.append(vizinho)

    return SearchResult(False, [], explorados, len(explorados), time.perf_counter() - inicio_tempo)


# ---------------------------------------------------------------------------
# 2) BUSCA EM PROFUNDIDADE (DFS)
# ---------------------------------------------------------------------------
def dfs(maze: Maze) -> SearchResult:
    """
    TODO: Implementar a Busca em Profundidade (DFS).

    Estrutura de dados sugerida: pilha (lista Python com append/pop),
    processando sempre a última célula inserida (LIFO).

    Diferente do BFS, o DFS NÃO garante o caminho mais curto — ele
    "mergulha" por um caminho até não poder mais avançar antes de
    voltar (backtrack).
    """
    inicio_tempo = time.perf_counter()

    # TODO: implemente aqui a busca em profundidade.

    fronteira = [maze.inicio]
    conhecidos = {maze.inicio}
    veio_de: Dict[Coord, Coord] = {}
    explorados: List[Coord] = []

    while fronteira:
        atual = fronteira.pop()
        explorados.append(atual)
        if atual == maze.objetivo:
            return SearchResult(True, reconstruir_caminho(veio_de, maze.inicio, maze.objetivo), explorados, len(explorados), time.perf_counter() - inicio_tempo)

        for vizinho in maze.vizinhos(atual):
            if vizinho not in conhecidos:
                conhecidos.add(vizinho)
                veio_de[vizinho] = atual
                fronteira.append(vizinho)

    return SearchResult(False, [], explorados, len(explorados), time.perf_counter() - inicio_tempo)


# ---------------------------------------------------------------------------
# 3) BUSCA A* (A-ESTRELA)
# ---------------------------------------------------------------------------
def astar(maze: Maze) -> SearchResult:
    """
    TODO: Implementar a Busca A*.

    Estrutura de dados sugerida: fila de prioridade (heapq), ordenada
    por f(n) = g(n) + h(n), onde:
      * g(n) = custo do caminho do início até n (número de passos);
      * h(n) = heuristica(n, maze.objetivo)  (já implementada acima).

    Dica: como o heapq não permite comparar tuplas com Coord "empatadas"
    facilmente, uma boa prática é inserir na fila tuplas do tipo
    (f, contador, celula), onde `contador` é um número que só aumenta
    (para desempatar sem comparar as células diretamente).
    """
    inicio_tempo = time.perf_counter()

    # TODO: implemente aqui a busca A*.

    contador = 0
    fronteira = [(heuristica(maze.inicio, maze.objetivo), contador, maze.inicio)]
    veio_de: Dict[Coord, Coord] = {}
    custo: Dict[Coord, int] = {maze.inicio: 0}
    explorados: List[Coord] = []
    fechados = set()

    while fronteira:
        _, _, atual = heappop(fronteira)
        if atual in fechados:
            continue

        fechados.add(atual)
        explorados.append(atual)
        if atual == maze.objetivo:
            return SearchResult(True, reconstruir_caminho(veio_de, maze.inicio, maze.objetivo), explorados, len(explorados), time.perf_counter() - inicio_tempo)

        for vizinho in maze.vizinhos(atual):
            novo_custo = custo[atual] + 1
            if vizinho in fechados or novo_custo >= custo.get(vizinho, float("inf")):
                continue

            custo[vizinho] = novo_custo
            veio_de[vizinho] = atual
            contador += 1
            heappush(fronteira, (novo_custo + heuristica(vizinho, maze.objetivo), contador, vizinho))

    return SearchResult(False, [], explorados, len(explorados), time.perf_counter() - inicio_tempo)


# Mapa usado pela interface para associar o texto do dropdown à função
ALGORITMOS = {
    "BFS": bfs,
    "DFS": dfs,
    "A*": astar,
}
