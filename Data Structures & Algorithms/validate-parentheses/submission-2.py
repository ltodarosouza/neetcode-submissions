class Solution:
    def isValid(self, s: str) -> bool:
        abertura = {"[" : "colchetes", "{" : "chaves", "(" : "parenteses"}
        fechamento = {"}" : "chaves", ")": "parenteses", "]" : "colchetes"}
        pilha = []
        valido = True
        for l in s:
            if l in abertura:
                pilha.append(abertura[f"{l}"])
            else:
                if not pilha:
                    valido = False
                    break
                if pilha.pop() != fechamento[f"{l}"]:
                    valido = False
                    break
        if len(pilha) != 0:
            valido = False
        return valido
        