# Labirinto IA — Avaliação de Algoritmos de Busca

Este projeto foi desenvolvido como uma atividade de avaliação na disciplina de Inteligência Artificial do professor Alexandre Augusto Angelo de Souza, da Universidade Federal da Grande Dourados (UFGD). A proposta tem como objetivo avaliar os alunos no desenvolvimento e na análise de três algoritmos fundamentais de busca em grafos e labirintos:

- Implementar a Busca em Largura
- Implementar a Busca em Profundidade
- Implementar a Busca A*

A atividade visa verificar a capacidade dos estudantes de compreenderem os conceitos teóricos e aplicarem corretamente as estratégias de busca em um ambiente prático, comparando comportamento, eficiência e qualidade da solução encontrada.

## Contexto da avaliação

A interface gráfica deste projeto foi desenvolvida pelo professor, que deixou a estrutura pronta para receber os algoritmos implementados pelos alunos. O objetivo central é que os estudantes trabalhem apenas na lógica de busca, enquanto a interface, o desenho do labirinto, os controles e a visualização dos resultados ficam a cargo do ambiente já preparado.

Assim, o professor disponibilizou uma base funcional com:

- geração do labirinto;
- representação do estado inicial e do objetivo;
- navegação pelos vizinhos das células;
- renderização visual do tabuleiro;
- seleção do algoritmo pelo usuário;
- exibição do caminho encontrado, células exploradas e métricas da busca.

Os alunos precisam apenas completar a implementação dos algoritmos em `algorithms.py`, seguindo as convenções fornecidas pelo professor.

## Como executar

Com o ambiente virtual ativado, instale o projeto a partir do `pyproject.toml`:

```bash
python -m pip install .
python main.py
```

O comando `python -m pip install .` lê as dependências declaradas em
`pyproject.toml` e instala automaticamente o `pygame` caso ele ainda não
esteja instalado ou não atenda à versão mínima exigida (`pygame>=2.5`).

Durante o desenvolvimento, o projeto também pode ser instalado em modo editável:

```bash
python -m pip install -e .
```

Uma janela deve abrir com:

- um tabuleiro com labirinto gerado aleatoriamente;
- o ponto de início em verde e o objetivo em vermelho/rosa;
- obstáculos em preto e células livres em cinza;
- um dropdown para escolher o algoritmo: `BFS`, `DFS` ou `A*`;
- um botão **Executar** para rodar a busca;
- um botão **Novo Labirinto** para gerar outro cenário;
- informações de estatísticas e legenda de cores.

Ao executar antes da implementação, a aplicação pode exibir a mensagem de que o algoritmo ainda não foi implementado. Após a conclusão correta dos algoritmos, o programa passa a desenhar as células exploradas e o caminho final encontrado.

## Estrutura do projeto

```
Labirinto/
├── main.py         # Ponto de entrada da interface (pronto)
├── ui.py           # Desenho do tabuleiro e componentes visuais (pronto)
├── maze.py         # Representação do labirinto (pronto)
├── algorithms.py   # Implementação dos algoritmos de busca
├── pyproject.toml   # Metadados e dependências do projeto
└── README.md       # Documentação do projeto
```

## O que deve ser implementado

Em `algorithms.py`, os alunos devem implementar as funções:

```python
def bfs(maze: Maze) -> SearchResult: ...
def dfs(maze: Maze) -> SearchResult: ...
def astar(maze: Maze) -> SearchResult: ...
```

Cada uma dessas funções recebe um objeto `Maze` e retorna um `SearchResult` contendo:

- `encontrado`: se o caminho até o objetivo foi encontrado;
- `caminho`: sequência de células do início ao objetivo;
- `explorados`: células visitadas na ordem de exploração;
- `expandidos`: quantidade de nós processados;
- `tempo`: tempo de execução do algoritmo.

## Requisitos

- Python 3.10+
- pygame (`pip install pygame`)

## Observação

Este repositório serve como base para a avaliação prática da disciplina de IA, com a interface pronta e o código de apoio já preparado, permitindo que o foco principal esteja na implementação correta e eficiente dos algoritmos de busca.

## Implementação

Implementação em código realizada por:

* Leonardo Farias de Oliveira
* Josiel Phelipe Oliveira Franco

## Créditos

A interface, a estrutura inicial do projeto e os algoritmos utilizados foram disponibilizados pelo professor **Alexandre Augusto Angelo de Souza**, da **Universidade Federal da Grande Dourados (UFGD)**, como parte da avaliação da disciplina de **Inteligência Artificial**.

Os autores deste projeto foram responsáveis pela **implementação dos algoritmos em código**, utilizando a estrutura e os algoritmos previamente fornecidos.
