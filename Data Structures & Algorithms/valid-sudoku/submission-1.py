class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # ver duplicadas em uma linha
        # ver duplicadas em uma coluna
        # ver duplicadas em cada bloco
        colunas = [[] for _ in range(9)]
        linhas = [[] for _ in range(9)]
        blocos = [[] for _ in range(9)]
        for i in range (len(board)):
            linha = board[i]
            for j in range (len(linha)):
                elemento = linha[j]
                if elemento != ".":
                    linhas[i].append(int(elemento))
                    colunas[j].append(int(elemento))
                    blocos[(i//3)*3+j//3].append(int(elemento))
        valido = True
        for i in range(9):
            if len(set(blocos[i])) != len(blocos[i]):
                valido = False
                break
            elif len(set(linhas[i])) != len(linhas[i]):
                valido = False
                break
            elif len(set(colunas[i])) != len(colunas[i]):
                valido = False
                break
        return valido