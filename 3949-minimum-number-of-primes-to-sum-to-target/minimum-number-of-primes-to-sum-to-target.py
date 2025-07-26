class Solution:
    def __init__(self):
        self.primes = [2]
    def prime_list(self,m):
        num=3
        while len(self.primes)<m:
            isprime = True
            for i in range(len(self.primes)): 
                if num % self.primes[i] == 0:
                    isprime = False
                    break
            if isprime:
                self.primes.append(num)
            if len(self.primes)==m:
                return
            
            num+=2
            

    def minNumberOfPrimes(self, n: int, m: int) -> int:
        self.prime_list(m)
        print(self.primes)
        dp={}
        def dfs(total):
            if total==0:
                return 0
            
            if total<0:
                return math.inf
            
            if total in dp:
                return dp[total]

            temp_ans = math.inf
            for i in range(len(self.primes)):
                temp_ans = min(temp_ans,1+dfs(total-self.primes[i]))
            dp[total] = temp_ans
            return temp_ans
        
        res = dfs(n)
        return res if res!=math.inf else -1 
            

            