def minMoves(target: int, maxDoubles: int) -> int:

        sin = 0
        dub = 0
        t = target

        

        while dub < maxDoubles and (t // 2 >= 2):
            t = t // 2
            dub += 1

        '''
        if target%2==0:
            sin = target // dub**2 
        elif dub == 0:
            sin = target - 1
        else:
            sin = target // dub**2 + 1
        '''
        moves = target // 28**5
        print(moves)

        print(sin)
        print(dub)
        
minMoves(766972377, 92)

#print([i for i in range(0, 10)])
