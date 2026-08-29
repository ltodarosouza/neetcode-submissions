class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            if str(n) not in dic:
                dic[str(n)] = 1
            else:
                dic[str(n)] += 1
        ord = dict(sorted(dic.items(), key=lambda item: item[1], reverse= True))
        num = list(ord.keys())
        saida = []
        for i in range(k):
            saida.append(int(num[i]))
        return saida
        