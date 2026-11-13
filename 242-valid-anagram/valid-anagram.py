from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1_clean = s.replace(" ", "").lower()
        s2_clean = t.replace(" ", "").lower()

        if len(s1_clean) != len(s2_clean):
            return False

        counts = {}
        for char in s1_clean:
            counts[char] = counts.get(char, 0) + 1

        for char in s2_clean:
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1

        return True