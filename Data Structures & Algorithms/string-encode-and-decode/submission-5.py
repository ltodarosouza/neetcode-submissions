class Solution:
    def encode(self, strs) -> str:
        enconder = ""
        for string in strs:
            i = len(string)
            enconder += f"{i}#{string}"
        return enconder
    def decode(self, s) -> str:
        saida = []
        j = 0
        while j < len(s):
            i = j
            while s[i] != "#":
                i += 1
            num = int(s[j:i])
            j = num + i + 1
            saida.append((s[i+1:j]))
            i += num
        return saida

