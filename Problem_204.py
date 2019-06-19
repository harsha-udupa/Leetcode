'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        elif n<4:
            return 1
        prime=[2,3]
        count=2
        for i in range(4,n):
            if (self.isprime(i,prime)):
                count+=1
                prime.append(i)
        return count
    
    def isprime(self,n,prime):
        
        for i in prime:
            if n%i ==0:
                return False
            if i*i>n:
                return True
        return True
            
