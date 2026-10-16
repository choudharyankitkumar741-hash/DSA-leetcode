class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # Define 32-bit integer boundaries
        int_min, int_max = -2**31, 2**31 - 1
        
        # Track sign and work with absolute value
        sign = -1 if x < 0 else 1
        num = abs(x)
        
        rev = 0
        while num != 0:
            digit = num % 10
            
            # Check for overflow before multiplying by 10
            if rev > (int_max - digit) // 10:
                return 0
                
            rev = rev * 10 + digit
            num //= 10
            
        result = sign * rev
        
        # Final safety bounds check
        if result < int_min or result > int_max:
            return 0
            
        return result

        