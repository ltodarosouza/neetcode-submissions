class Solution:
    def isPalindrome(self, s: str) -> bool:
        letras = []
        for l in s:
            if l.isalnum():
                letras.append(l.lower())
        i = 0
        j = len(letras)-1
        valido = True
        while i < j:
            if letras[i] != letras[j]:
                valido = False
                break
            i += 1
            j -= 1
        return valido


        