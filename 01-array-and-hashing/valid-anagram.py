
# Problem: Valid Anagram
# LeetCode: 242
# Difficulty: Easy

# Approach: Hash Map (Character Frequency)
# Time Complexity: O(n) average
# Space Complexity: O(1) for a fixed character set

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        freq = {}

        # Count characters in the first string
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # Decrease counts using the second string
        for char in t:
            if char in freq:
                freq[char] -= 1
            else:
                freq[char] = -1

        # All character frequencies must be zero
        for char in freq:
            if freq[char] != 0:
                return False

        return True
