class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for number in range(32):
            result = 2**number
            if n < result:
                break
            elif n == result:
                return True
        return False