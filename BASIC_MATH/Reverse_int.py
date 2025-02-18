'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x<0):
            sign=-1
            x=abs(x)
        else:
            sign=1
        r=0
        while(x>0):
            l=x%10
            r=r*10+l
            x=x//10
        reversed=r*sign
        if reversed <= -2**31 or reversed >= 2**31 - 1:
            return 0
        return reversed
sol=Solution()
print(sol.reverse(-1234))



        