class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        resultado = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                indice = stack.pop()
                resultado[indice] = i - indice
            stack.append(i)
        
        return resultado    

