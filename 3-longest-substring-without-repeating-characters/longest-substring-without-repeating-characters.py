class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        max_len=0
        chr_set = set()

        for j in range(len(s)):
            while s[j] in chr_set:
                chr_set.remove(s[i])
                i+=1
            chr_set.add(s[j])
            max_len=max(max_len,j-i+1)

        return max_len