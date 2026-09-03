class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 0 1 4 7    1 2 2 1 
        # 1 3 5 8
        save = {}
        frotas = 0
        for i in range(len(position)):
            save[position[i]] = speed[i]
        position.sort(reverse = True)
        frota_frente = 0
        for c in position:
            tempo = (target-c) / save[c]
            if tempo > frota_frente:
                frotas += 1
                frota_frente = tempo
        return frotas


                    



        