# problem : https://leetcode.com/problems/reverse-integer/#/description

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int = 2147483648
        sign_x = -1 if x < 0 else 1
        x = abs(x)
        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x //= 10
        z = sign_x * y
        if z < -max_int or z >= max_int:
            z = 0
        return z