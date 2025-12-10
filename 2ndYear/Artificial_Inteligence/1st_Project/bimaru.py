# bimaru.py: Template para implementação do projeto de Inteligência Artificial 2022/2023.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
# 103266 Henrique Machado
# 102423 Bernardo Galante

# Board size 10x10
ROWS = 10
COLS = 10

import numpy as np
from sys import stdin

from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)

class BimaruState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = BimaruState.state_id
        BimaruState.state_id += 1

        self.remainingBoats = [(4,1), (3,2), (2,3), (1,4)] 
        # (quantidade, tipoBarco)
        # 4 submarinos, 3 contratorpedeiros, 2 cruzadores, 1 couraçado

        # comecamos por colocar o maior barco 
        self.currentBoat = 4

    def __lt__(self, other):
        return self.id < other.id

    def __eq__(self, pther):
        return self.id == other.id

    #hint: metodos de comparacao (equals)
    #move states
    # TODO: outros metodos da classe


class Board:
    """Representação interna de um tabuleiro de Bimaru."""
    def __init__(self, rowLimits: list, colLimits: list, rowCapacities: list, 
                            colCapacities: list, hints: list, playBoard: list):
        self.rowLimits = rowLimits
        self.colLimits = colLimits
        self.rowCapacities = rowCapacities
        self.colCapacities = colCapacities
        self.hints = hints
        self.playBoard = playBoard

    def get_value(self, row: int, col: int) -> str:
        """Devolve o valor na respetiva posição do tabuleiro."""
        return self.playBoard[row][col]

    def adjacent_vertical_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente acima e abaixo,
        respectivamente."""
        return self.playBoard[row][col - 1], self.playBoard[row][col + 1]

    def adjacent_horizontal_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        return self.playBoard[row - 1][col], self.playBoard[row + 1][col]

    def toString(self):
        """Imprime cada componente do objeto board no stdout"""
        print("\nRow Limits: \n", self.rowLimits)
        print("\nColumn Limits: \n", self.colLimits)
        print("\nRow Capacities: \n", self.rowCapacities)
        print("\nCol Capacities: \n", self.colCapacities)
        print("\nHints: \n", self.hints)
        print("\nBoard: \n", self.playBoard)
        return

    def print(self):
        """ Imprime o tabuleiro bimaru"""
        for row in range(ROWS):
            for col in range(COLS):
                if self.playBoard[row][col] == "":
                    print(" ", end="")
                print(self.playBoard[row][col], end="")
            print("\n")

    @staticmethod
    def parse_instance(): 
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board."""

        rowLimits = [int(c) for c in stdin.readline().split()[1::]]
        colLimits = [int(c) for c in stdin.readline().split()[1::]]
        rowCapacities = [0 for r in rowLimits]
        colCapacities = [0 for c in colLimits]
        playBoard = np.zeros((ROWS, COLS), dtype=str) # 10x10 Board
        hintNumber = int(stdin.readline())
        hints = list(range(hintNumber))
        submarines, rightPieces, leftPieces, topPieces, bottomPieces = [], [], [], [], []

        for i in range(hintNumber): 
            hint = stdin.readline().split()
            hints[i] = [int(c) for c in hint[1:-1:]] + hint[3::]
            playBoard[int(hint[1])][int(hint[2])] = hint[3]
            if hint[3] == "C":
                submarines.append((int(hint[1]),int(hint[2])))
            if hint[3] == "R":
                rightPieces.append((int(hint[1]),int(hint[2])))
            if hint[3] == "L":
                leftPieces.append((int(hint[1]),int(hint[2])))
            if hint[3] == "T":
                topPieces.append((int(hint[1]),int(hint[2])))
            if hint[3] == "B":
                bottomPieces.append((int(hint[1]),int(hint[2])))
            if hint[3] == "W":
                playBoard[int(hint[1])][int(hint[2])] = "."
            rowCapacities[int(hint[1])] += 1
            colCapacities[int(hint[2])] += 1

        # fill zero rows with water
        for i in range(ROWS):
            if rowLimits[i] == 0:
                for col in range(COLS):
                    playBoard[i][col] = "."

        # fill zero columns with water
        for i in range(COLS):
            if colLimits[i] == 0:
                for row in range(ROWS):
                    playBoard[row][i] = "."
        
        board = Board(rowLimits, colLimits, rowCapacities, 
                                            colCapacities, hints, playBoard)

        # rodear submarinos com agua
        if len(submarines) != 0:
            for c in submarines:
                # verifica se esta num canto
                if c[0] == 0 and c[1] == 0:
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]] = "."
                elif c[0] == 0 and c[1] == COLS-1:
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]] = "."
                elif c[0] == ROWS-1 and c[1] == 0:
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]][c[1]+1] = "."
                    playBoard[c[0]-1][c[1]] = "."
                elif c[0] == ROWS-1 and c[1] == COLS-1:
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]] = "."
                # verifica se esta numa fronteira
                elif c[0] == 0:
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]] = "."
                elif c[0] == ROWS-1:
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]][c[1]+1] = "."
                    playBoard[c[0]-1][c[1]] = "."
                elif c[1] == 0:
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]+1][c[1]] = "."
                    playBoard[c[0]][c[1]+1] = "."
                elif c[1] == COLS-1:
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]+1][c[1]] = "."
                    playBoard[c[0]][c[1]-1] = "."
                # esta no meio
                else:
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]+1][c[1]] = "."
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]][c[1]+1] = "."

        if len(rightPieces) != 0:
            # agua a volta menos a esquerda
            for c in rightPieces:
                playBoard[c[0]][c[1]-1] = "?"
                # verifica se esta no canto superior direito
                if c[0] == 0 and c[1] == COLS-1:
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]-2] = "."
                    playBoard[c[0]+1][c[1]] = "."
                # verifica se esta no canto inferior direito
                elif c[0] == ROWS-1 and c[1] == COLS-1:
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]-1][c[1]-2] = "."
                # verifica se esta em cima
                elif c[0] == 0:
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]][c[1]+1] = "."
                    if c[1] > 1:
                        playBoard[c[0]+1][c[1]-2] = "."
                # verifica se esta em baixo
                elif c[0] == ROWS-1:
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]][c[1]+1] = "."
                    if c[1] > 1:
                        playBoard[c[0]-1][c[1]-2] = "."
                # verifica se esta a esquerda
                elif c[1] == 1:
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]] = "."
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]][c[1]+1] = "."
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
                # verifica se esta a direita
                elif c[1] == COLS-1:
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]-2] = "."
                    playBoard[c[0]+1][c[1]] = "."
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]-2] = "."
                # esta no meio
                else:
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]-2] = "."
                    playBoard[c[0]+1][c[1]] = "."
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]-2] = "."
                    playBoard[c[0]][c[1]+1] = "."
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
    
        if len(leftPieces) != 0:
            # agua a volta menos a direita
            for c in leftPieces:
                playBoard[c[0]][c[1]+1] = "?"
                # verifica se esta no canto superior esquerdo
                if c[0] == 0 and c[1] == 0:
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]+2] = "."
                    playBoard[c[0]+1][c[1]] = "."
                # # verifica se esta no canto inferior esquerdo
                elif c[0] == ROWS-1 and c[1] == 0:
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]-1][c[1]+2] = "."
                # verifica se esta a esquerda
                elif c[1] == 0:
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]] = "."
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]-1][c[1]+2] = "."
                    playBoard[c[0]+1][c[1]+2] = "."
                # # verifica se esta a direita
                elif c[1] == COLS-2:
                    playBoard[c[0]][c[1]-1] = "."
                    if c[0] == 0:
                        playBoard[c[0]+1][c[1]-1] = "."
                        playBoard[c[0]+1][c[1]] = "."
                        playBoard[c[0]+1][c[1]+1] = "."
                    elif c[0] == ROWS-1:
                        playBoard[c[0]-1][c[1]-1] = "."
                        playBoard[c[0]-1][c[1]] = "."
                        playBoard[c[0]-1][c[1]+1] = "."
                    else:
                        playBoard[c[0]-1][c[1]-1] = "."
                        playBoard[c[0]-1][c[1]] = "."
                        playBoard[c[0]-1][c[1]+1] = "."
                        playBoard[c[0]+1][c[1]-1] = "."
                        playBoard[c[0]+1][c[1]] = "."
                        playBoard[c[0]+1][c[1]+1] = "."
                # # verifica se esta em cima
                elif c[0] == 0:
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]+2] = "."
                # # verifica se esta em baixo
                elif c[0] == ROWS-1:
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]-1][c[1]+2] = "."
                # esta no meio
                else:
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]+2] = "."
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]-1][c[1]+2] = "."

        if len(topPieces) != 0:
            # agua a volta menos em baixo
            for c in topPieces:
                playBoard[c[0]+1][c[1]] = "?"
                # verifica se esta no canto superior esquerdo
                if c[0] == 0 and c[1] == 0:
                    playBoard[c[0]][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]+2][c[1]+1] = "."
                # verifica se esta no canto superior direito
                elif c[0] == 0 and c[1] == COLS-1:
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]+2][c[1]-1] = "."
                # verifica se esta em cima
                elif c[0] == 0:
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]+2][c[1]-1] = "."
                    playBoard[c[0]+2][c[1]+1] = "."
                # verifica se esta em baixo
                elif c[0] == ROWS-2:
                    playBoard[c[0]-1][c[1]] = "."
                    if c[1] == 0:
                        playBoard[c[0]-1][c[1]+1] = "."
                        playBoard[c[0]][c[1]+1] = "."
                        playBoard[c[0]+1][c[1]+1] = "."
                    elif c[1] == COLS-1:
                        playBoard[c[0]-1][c[1]-1] = "."
                        playBoard[c[0]][c[1]-1] = "."
                        playBoard[c[0]+1][c[1]-1] = "."
                    else:
                        playBoard[c[0]-1][c[1]-1] = "."
                        playBoard[c[0]-1][c[1]+1] = "."
                        playBoard[c[0]][c[1]-1] = "."
                        playBoard[c[0]][c[1]+1] = "."
                        playBoard[c[0]+1][c[1]-1] = "."
                        playBoard[c[0]+1][c[1]+1] = "."
                # verifica se esta na fronteira esquerda
                elif c[1] == 0:
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]+2][c[1]+1] = "."
                # verifica se esta na fronteira direita
                elif c[1] == COLS-1:
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]+2][c[1]-1] = "."
                # esta no meio
                else:
                    playBoard[c[0]-1][c[1]] = "."
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]][c[1]+1] = "."
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]+2][c[1]-1] = "."
                    playBoard[c[0]+2][c[1]+1] = "."

        if len(bottomPieces) != 0:
            # agua a volta menos em cima
            for c in bottomPieces:
                playBoard[c[0]-1][c[1]] = "?"
                # verifica se esta no canto inferior esquerdo
                if c[0] == ROWS-1 and c[1] == 0:
                    playBoard[c[0]][c[1]+1] = "."
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]-2][c[1]+1] = "."
                # verifica se esta no canto inferior direito
                elif c[0] == ROWS-1 and c[1] == COLS-1:
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]-2][c[1]-1] = "."
                # verifica se esta em baixo
                elif c[0] == ROWS-1:
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]][c[1]+1] = "."
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]-2][c[1]-1] = "."
                    playBoard[c[0]-2][c[1]+1] = "."
                # verifica se esta em cima
                elif c[0] == 1:
                    playBoard[c[0]+1][c[1]] = "."
                    if c[1] == 0:
                        playBoard[c[0]+1][c[1]+1] = "."
                        playBoard[c[0]][c[1]+1] = "."
                        playBoard[c[0]-1][c[1]+1] = "."
                    elif c[1] == COLS-1:
                        playBoard[c[0]+1][c[1]-1] = "."
                        playBoard[c[0]][c[1]-1] = "."
                        playBoard[c[0]-1][c[1]-1] = "."
                    else:
                        playBoard[c[0]+1][c[1]-1] = "."
                        playBoard[c[0]+1][c[1]+1] = "."
                        playBoard[c[0]][c[1]-1] = "."
                        playBoard[c[0]][c[1]+1] = "."
                        playBoard[c[0]-1][c[1]-1] = "."
                        playBoard[c[0]-1][c[1]+1] = "."
                # verifica se esta na fronteira esquerda
                elif c[1] == 0:
                    playBoard[c[0]+1][c[1]] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]][c[1]+1] = "."
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]-2][c[1]+1] = "."
                # verifica se esta na fronteira direita
                elif c[1] == COLS-1:
                    playBoard[c[0]+1][c[1]] = "."
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]-2][c[1]-1] = "."
                # esta no meio
                else:
                    playBoard[c[0]+1][c[1]] = "."
                    playBoard[c[0]+1][c[1]-1] = "."
                    playBoard[c[0]+1][c[1]+1] = "."
                    playBoard[c[0]][c[1]-1] = "."
                    playBoard[c[0]][c[1]+1] = "."
                    playBoard[c[0]-1][c[1]-1] = "."
                    playBoard[c[0]-1][c[1]+1] = "."
                    playBoard[c[0]-2][c[1]-1] = "."
                    playBoard[c[0]-2][c[1]+1] = "."

        return board

class Bimaru(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        self.initial = BimaruState(board) # estado inicial é um BimaruState

    def actions(self, state: BimaruState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # todos os barcos foram colocados
        remainingBoats = state.remainingBoats
        if remainingBoats == [0,0,0,0]: return None

        # escolher maior barco possivel
        for b in range(len(remainingBoats)):
            #b=(qty, tipoBarco)
            if remainingBoats[b][0] > 0:
                if remainingBoats[b][1] == state.currentBoat: 
                    boatToPlace = state.currentBoat
            else:
                state.currentBoat -= 1

        # verificar linhas e colunas possiveis
        possibleRows = list()
        for row in range(ROWS):
            if state.board.rowLimits[row] >= boatToPlace: 
                possibleRows.append(row)

        possibleCols = list()
        for col in range(COLS):
            if state.board.colLimits[col] >= boatToPlace:
                possibleCols.append(col)

        # ver espacos livres em possibleRows/Cols
        if len(possibleCols) != 0:
            freePositionsCols = [[] for l in range(len(possibleCols))]
            for possCol in range(len(possibleCols)):
                print("posc:" , possCol)
                for row in range(ROWS):
                    if state.board.playBoard[row][possibleCols[possCol]] == '':
                        freePositionsCols[possCol].append((row, possibleCols[possCol]))

        if len(possibleRows) != 0:
            freePositionsRows = [[] for l in range(len(possibleRows))]
            for possRow in range(len(possibleRows)):
                for col in range(COLS):
                    if state.board.playBoard[possibleRows[possRow]][col] == '':
                        freePositionsRows[possRow].append((possibleRows[possRow], col))
        print("free pos rows: ", freePositionsRows)
        print("free pos col: ", freePositionsCols)

    def result(self, state: BimaruState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO
        pass

    def goal_test(self, state: BimaruState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo/final. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""
        if state.remainingBoats == [0,0,0,0]:
            # verifica se as linhas e colunas estão preenchidas ao máximo
            for col in range(COLS):
                if rowCapacities[col] != rowLimits[col]:
                    return False
            for row in range(ROWS):
                if colCapacities[row] != colCapacities[row]:
                    return False
            return True
        return False

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""

        # hint: funcao que sugere estado otimo

        # TODO
        pass

    # TODO: outros metodos da classe


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.

    board  = Board.parse_instance()
    problem = Bimaru(board)
    board.toString()
    board.print()
    problem.actions(problem.initial)
    pass
