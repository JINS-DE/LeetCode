class Solution:
    def reverse(self, x: int) -> int:
        # 음수인지 판별
        sign = -1 if x < 0 else 1
        # 절댓값 뒤집기
        rev = int(str(abs(x))[::-1]) * sign
        # 32-bit 범위 체크
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
