class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        pilha = []
        operacoes = {"+", "-", "*", "/"}
        for n in tokens:
            if n not in operacoes:
                pilha.append(int(n))
            else:
                if n == "+":
                    pilha.append(pilha.pop() + pilha.pop())
                elif n == "-":
                    resultado = pilha[-2] - pilha.pop()
                    pilha.pop()
                    pilha.append(resultado)
                elif n == "*":        
                    pilha.append(pilha.pop() * pilha.pop())
                else:
                    resultado = int(pilha[-2]/pilha.pop())
                    pilha.pop()
                    pilha.append(resultado)
        return pilha[0]