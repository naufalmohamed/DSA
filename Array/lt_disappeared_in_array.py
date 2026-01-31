'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
'''

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # create count list
        count = [0]*(len(nums)+1)

        # loop through nums and add to count
        for num in nums:
            count[num] += 1

        # create res list
        res = []

        # loop through count and add to res the zero vals
        for idx in range(1,(len(nums)+1)):
            if count[idx] == 0:
                res.append(idx)
        return res 
    

'''
Silly Mistakes:
- Used : in range
- enumerate will start with idx 0

'''
