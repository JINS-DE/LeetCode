class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10        # 마지막 자리 추출
            x //= 10              # 마지막 자리 제거

            # 오버플로우 체크 (32비트 범위 벗어나면 0)
            if result > (2**31 - 1) // 10 or (
                result == (2**31 - 1) // 10 and digit > 7
            ):
                return 0

            result = result * 10 + digit

        return result * sign
