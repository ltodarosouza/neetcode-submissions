class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        nums = set(nums)
        if len(nums) == 0:
            return 0
        maior = 1
        for num in nums:
            if num-1 not in nums:
                atual = num
                cont = 1
                while atual in nums:
                    atual += 1
                    cont += 1
                maior = max(cont, maior)
        return maior-1

