import java.util.*;
class Solution {
    public int lengthOfLastWord(String s) {
        String [] st = s.strip().split(" ");
        return st[st.length-1].length();
    }
}