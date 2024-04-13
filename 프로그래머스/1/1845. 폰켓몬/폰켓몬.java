import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        HashSet<Integer> monsters = new HashSet<>();
        
        for(int i = 0; i < nums.length; i++){
            monsters.add(nums[i]);
        }
        
        if(monsters.size() > nums.length/2)
            return nums.length/2;
        
        return monsters.size();
    }
}

