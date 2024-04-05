class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n_nums = []

        for num in nums:
           n_nums.append(num)
        
        for num in nums:
           n_nums.append(num)
        
        return n_nums

solution = Solution()
result = solution.getConcatenation(nums=[1,2,1])
print(result)