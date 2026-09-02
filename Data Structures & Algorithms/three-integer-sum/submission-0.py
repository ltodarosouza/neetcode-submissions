class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4 -1 -1 0 1 2
        outp = []
        nums.sort()
        for i in range(len(nums)):
            atual = nums[i]
            oposto = -atual
            j = i + 1
            k = len(nums)-1
            while j < k:
                n1 = nums[j]
                n2 = nums[k]
                if n1 + n2 == oposto:
                    if [atual, n1, n2] in outp:
                        pass
                    else:
                        outp.append([atual, n1, n2])
                    j += 1
                    k -= 1
                elif n1 + n2 > oposto:
                    if n1 > n2:
                        j += 1
                        continue
                    else:
                        k -= 1
                        continue
                else:
                    if n1 > n2:
                        k -= 1
                        continue
                    else:
                        j += 1
                        continue
        
        return outp

