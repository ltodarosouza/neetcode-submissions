class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {}
        produtorio = 1
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
                continue
            produtorio *= nums[i-1]
            prefix[i] = produtorio
        sufix = {}
        produtorio = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                sufix[i] = 1
                continue
            produtorio *= nums[i+1]
            sufix[i] = produtorio
        outp = []
        for i in range(len(nums)):
            outp.append(prefix[i]*sufix[i])
        return outp