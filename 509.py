# Solução Fibonacci.Exercicio numero 509

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
            
        return b
        
