class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        last = n*n

        seen = set()
        q = [(1,0)]

        while q:            
            pos,step = q.pop(0)
            
            if pos == final: return step

            i =  n - 1 - (pos-1)//n
            print(((pos-1)//n)%2)
            j = (pos-1)%n if ((pos-1)//n)%2==0 else n - 1 - ((pos-1)%n)
            print(i,j)
            print(pos)
            if board[i][j]!=-1:
                pos,step = board[i][j], step
            if pos==last: return step

            for i in range(1, 7):
                if (pos + i) not in seen:
                    seen.add(pos + i)
                    q.append((pos + i, step + 1))

        return -1
            


