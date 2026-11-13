
# Problem: Contains Duplicate
# LeetCode: 217
# Difficulty: Easy

# Approach: Hash Set
# Time Complexity: O(n) average
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
