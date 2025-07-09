class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = set(wordList)
        if endWord not in seen:
            return 0
        q = deque([(beginWord,1)])
        while q:
            word,step = q.popleft()
            if word == endWord:
                return step
            #calculations - word formation    
            for c in 'abcdefghijklmnopqrstuvwxyz':
                for i in range(len(beginWord)):
                    newWord = word[:i]+c+word[i+1:]
                    if newWord in seen:
                        q.append((newWord,step+1))
                        seen.remove(newWord)
        
        return 0
