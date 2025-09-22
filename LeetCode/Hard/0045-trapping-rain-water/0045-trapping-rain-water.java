import java.util.*;
class Solution {
    public int trap(int[] height) {
        Stack<Integer> stack = new Stack<>();
        int total=0;
        for (int i=0;i<height.length;i++){
            while (!stack.isEmpty() && height[i] > height[stack.peek()]){
                int bottom = stack.pop();
                if (stack.isEmpty()) break;
                int leftWall = stack.peek();
                
                int width = i-leftWall-1;
                total += width*(Math.min(height[i],height[leftWall]) - height[bottom]);

            }
            stack.push(i);
        }
        return total ;
    } 
}