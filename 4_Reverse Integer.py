# 0 일 때 체크 안해서 fail, 범위 체크안해서 fail 떴었음
class Solution:
    def reverse(self, x: int) -> int:
        unsigned = False

        # 음수 처리
        if x < 0:
            unsigned = True
        x = str(x)

        # 음수 기호 제거
        if unsigned:
            x = x.replace('-', '')

        # 리스트로 변환 후, 좌우 반전
        x = list(x)
        left, right = 0, len(x) - 1
        while left < right:
            x[left], x[right] = x[right], x[left]  # 값을 스왑
            left += 1
            right -= 1

        # 불필요한 앞쪽 '0' 제거
        while len(x) > 0 and x[0] == '0':
            del x[0]

        # 빈 리스트가 될 경우 (즉, 모든 숫자가 0일 경우)
        if len(x) == 0:
            return 0

        # 리스트를 다시 문자열로 변환
        x = ''.join(x)

        # 음수인 경우 '-' 추가
        if unsigned:
            x = '-' + x

        # 정수로 변환
        x = int(x)

        # 32비트 범위 체크
        if x < -2**31 or x > 2**31 - 1:
            return 0

        return x
