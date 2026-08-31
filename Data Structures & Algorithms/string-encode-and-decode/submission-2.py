class Solution:
    def __init__(self) -> None:
        self.virgulas = []
    def encode(self, strs) -> str:
        enconder = ""
        i = 0
        for string in strs:
            if i == 0:
                i += len(string)
            else:
                i += len(string) + 1
            enconder += string
            if i != 0:
                enconder += ","
            
            self.virgulas.append(i)
        enconder = enconder[:len(enconder)-1]
        return enconder

    def decode(self, s) -> str:
        ultimo = 0
        saida = []
        for n in self.virgulas:
            saida.append(s[ultimo:n])
            if n != 0:
                ultimo = n+1
        
        return saida