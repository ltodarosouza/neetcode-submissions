class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = []
        produtorio = 1
        for i in range(len(nums)):
            if i == 0:
                mult.append(1)
                continue
            produtorio *= nums[i-1]
            mult.append(produtorio)
        produtorio = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                mult[i] *= 1
                continue
            produtorio *= nums[i+1]
            mult[i] *= produtorio
        return mult
