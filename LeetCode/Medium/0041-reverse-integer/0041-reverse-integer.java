import java.util.*;

class Solution {
    public int reverse(int x) {
        int sign = x < 0 ? -1 : 1;

        // 절댓값을 문자열로 변환 후 뒤집기
        String tmp = new StringBuilder(String.valueOf(Math.abs((long)x))).reverse().toString();

        // Long.parseLong은 순수 숫자 문자열만 받음
        long answer = Long.parseLong(tmp) * sign;

        // int 범위 벗어나면 0 리턴
        if (answer < Integer.MIN_VALUE || answer > Integer.MAX_VALUE) {
            return 0;
        }

        return (int) answer;
    }
}
