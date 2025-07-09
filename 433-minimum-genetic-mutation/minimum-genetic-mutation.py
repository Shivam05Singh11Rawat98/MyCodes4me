class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([])
        q.append((startGene,0))
        seen = set(bank)

        if endGene not in seen:
            return -1

        while q:
            gene,step = q.popleft()
            if gene==endGene:
                return step
            
            ##calculations part
            for i in range(9):
                for c in ['A','C','G','T']:
                    temp_gene = gene[:i] + c + gene[i+1:]
                    if temp_gene in seen:
                        q.append((temp_gene,step+1))
                        seen.remove(temp_gene)

        return -1