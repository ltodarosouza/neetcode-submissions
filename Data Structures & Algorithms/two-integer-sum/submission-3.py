class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = sorted(enumerate(nums), key=lambda x: x[1])
        i, j = 0, len(indexed) - 1
        
        while i < j:
            n1 = indexed[i][1]
            n2 = indexed[j][1]
            soma = n1 + n2
            if soma == target:
                return sorted([indexed[i][0], indexed[j][0]])
            elif soma < target:
                i += 1
            else:
                j -= 1
        
        return []