class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def fibo(x):
            if x<=1:
                return 1
            if x in memo:
                return memo[x]
            memo[x]= fibo(x-1)+fibo(x-2)
            return memo[x]
        return fibo(n)