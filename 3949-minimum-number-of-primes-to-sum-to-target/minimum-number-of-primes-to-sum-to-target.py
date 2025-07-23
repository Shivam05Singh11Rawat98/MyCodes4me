class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        def generateprime(M,N):
            primes = [2]  # Initialize an empty list to store prime numbers and add 2 as the first prime number
            num = 3  # Start checking for prime numbers from 3
            while len(primes) < N:  # Keep searching until we find N prime numbers
                is_prime = True  # Assume the current number is prime until proven otherwise
                for i in range(len(primes)):
                    if num % primes[i] == 0:  # If the current number is divisible by any previously found prime numbers
                        is_prime = False  # Then it is not a prime number
                        break  # Exit the loop since we've already proven it's not prime
                if is_prime:  # If the current number is still prime after checking all previously found prime numbers
                    primes.append(num)
                if len(primes)==M:
                    break  # Add it to our list of prime numbers
                num += 2
            return primes
        primes = generateprime(n,m)
        cache = {}
        def dp(curr_sum):
            if curr_sum==n:
                return 0
            if curr_sum>n:
                return float("inf")
            if curr_sum in cache:
                return cache[curr_sum]
            
            min_count = float("inf")
            for prime in primes:
                min_count = min(min_count, dp(curr_sum+prime)+1)
            
            cache[curr_sum] = min_count
            return min_count
        
        res = dp(0)
        return res if res != float('inf') else -1