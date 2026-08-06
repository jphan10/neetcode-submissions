class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        have a dict where: count -> list of nums
        then join the dict values and return the top k elements
        '''

        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        

        freq = [[] for i in range(len(nums) + 1)]


        for key, value in counts.items():
            freq[value].append(key)


        rv = []

        for i in range(len(freq) - 1 , 0, -1):
            for n in freq[i]:
                rv.append(n)
                if len(rv) == k:
                    return rv

        



 
        