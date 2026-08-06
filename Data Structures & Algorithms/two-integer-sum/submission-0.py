class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Use the compliment approach.
        Compute the compliment using the target and the current num
        If the compliment has been seen (stored in a freq hash)
        then return both indexes

        If not seen then store num -> index in freq hash
        
        '''

        freq = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in freq:
                return [freq[compliment], i]
            else:
                freq[num] = i