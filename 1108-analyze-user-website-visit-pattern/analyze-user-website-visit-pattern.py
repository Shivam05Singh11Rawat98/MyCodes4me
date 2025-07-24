class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        user_serach_seq = defaultdict(list)
        for time,site,user in sorted(zip(timestamp,website,username)):
            user_serach_seq[user].append(site)
        
        possibleTuples = defaultdict(int)
        for user,sites in user_serach_seq.items():
            for pattern in set(combinations(sites,3)):
                possibleTuples[pattern]+=1
        
        print(possibleTuples)

        max_pattern,max_score="",0

        for pattern, score in possibleTuples.items():
            if max_score<score or (max_score==score and pattern<max_pattern):
                max_pattern = pattern
                max_score = score
        
        return max_pattern


