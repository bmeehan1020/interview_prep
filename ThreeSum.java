import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

/**
 * ThreeSum (Medium)
 * 
 * Given an array nums of n integers, are there elements a, b, c in nums such
 * that a + b + c = 0? Find all unique triplets in the array which gives the sum
 * of zero. Notice that the solution set must not contain duplicate triplets.
 */
public class ThreeSum {
    public static List<List<Integer>> threeSum(int[] nums) {
        HashSet<Integer> elems = new HashSet<>();
        List<List<Integer>> result = new ArrayList<>();

        for (int n : nums) {
            elems.add(n);
        }

        for (int i = 0; i < nums.length; i++) {
            elems.remove(nums[i]);
            for (int j = i + 1; j < nums.length; j++) {
                int triplet = -(nums[i] + nums[j]);
                if (elems.contains(triplet)) {
                    result.add(Arrays.asList(nums[i], nums[j], triplet));
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(threeSum(new int[] { -1, 0, 1, 2, -1, -4 }));
    }
}