class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)[::-1]
        if x[-1]=='-':
            return 0 if -int(x[:-1]) < -(2**31) else -int(x[:-1])
        else:
            return 0 if int(x)>(2**31)-1 else int(x)