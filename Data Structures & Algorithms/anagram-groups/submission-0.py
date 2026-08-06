class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Tricky one.

        Since we know the alphabet is exactly 26 charcters long
        we can uses arrays to count the frequency of characters for each
        string. What if we had a dict where: counts(arr) -> list(strings).
        Then we could join the values of the dict into a single arr
        '''

        # we'll use a defaultdict with the list param to store arr values
        rv = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ ord(c) -  ord("a") ] += 1
            rv[tuple(count)].append(s)

        return list(rv.values())