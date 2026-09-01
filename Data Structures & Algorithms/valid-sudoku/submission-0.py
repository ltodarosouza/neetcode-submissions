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
                    if i <= 2:
                        if j <= 2:
                            blocos[0].append(int(elemento))
                        elif j <= 5:
                            blocos[1].append(int(elemento))
                        else:
                           blocos[2].append(int(elemento))                
                    elif i <= 5:
                        if j <= 2:
                            blocos[3].append(int(elemento))
                        elif j <= 5:
                            blocos[4].append(int(elemento))
                        else:
                           blocos[5].append(int(elemento))  
                    else:
                        if j <= 2:
                            blocos[6].append(int(elemento))
                        elif j <= 5:
                            blocos[7].append(int(elemento))
                        else:
                           blocos[8].append(int(elemento))  
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