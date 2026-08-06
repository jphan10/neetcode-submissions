class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # increment counts on first string
        # decrement counts on second string
        # if any values drop below 0, return false
        # if you make it all the way through both loops return true

        freq = {}

        if len(t) != len(s):
            return False

        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        for c in t:
            if c in freq:
                if freq[c] <= 0:
                    return False
                else:
                    freq[c] -= 1
            else:
                return False
        
        return True
