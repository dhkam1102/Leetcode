# solution in java 
#class Solution {
#     public boolean containsDuplicate(int[] nums) {
#         Set<Integer> hash_set = new HashSet<>();
#         for (int num : nums) {
#             boolean result = hash_set.add(num);
#             if (result == false) {
#                 return true;
#             }
#         }
#         return false;
#     }
# }

# //space: O(N), speed: O(N)