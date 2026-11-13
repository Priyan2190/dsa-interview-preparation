
# Problem: Group Anagrams
# LeetCode: 49
# Difficulty: Medium

# Approach: Hash Map + Sorting
# Time Complexity: O(k * m log m)
# Space Complexity: O(k * m)

class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]

        return list(anagrams.values())
