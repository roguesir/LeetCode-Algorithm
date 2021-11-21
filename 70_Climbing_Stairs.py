# Method 1

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib = lambda n:1 if n<=2 else fib(n-1)+fib(n-2)
        return fib(n+1)


# Method 2

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        return int(sqrt(5)/5*((((1+sqrt(5))/2))**(n+1)-(((1-sqrt(5))/2))**(n+1)))


# Method 3

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=1
        b=1
        def fib(n, a, b):
            while n != 0:
                a, b = b, a+b
                n -= 1
            return b
        return fib(n-1, a, b)


# method 4
class Solution:
    def climbStairs(self, n: int) -> int:

        p, q, r = 0, 0, 1
        for i in range(n):
            p = q
            q = r
            r = p+q
        return r