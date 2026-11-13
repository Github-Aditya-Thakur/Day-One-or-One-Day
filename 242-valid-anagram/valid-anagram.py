from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_clean = s.replace(" ","").lower()
        t_clean = t.replace(" ","").lower()

        return Counter(s_clean)== Counter(t_clean)
            
