'''
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
'''


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # create count arr
        l = len(nums)
        count = [0]*(l+1)

        # for loops nums
        for n in nums:
            # inc index by one
            count[n] += 1
        
        # create var names
        missing, extra = None, None

        # for loop count
        for i in range(1, l+1):
            # if count > 1 extra
            if count[i] == 2:
                extra = i
            # if count < 1 missing
            if count[i] == 0:
                missing = i

        return [extra, missing]
        

'''
Common pitfalls I hit on “Set Mismatch” (and similar array problems):

Used n in nums inside a loop, not realizing membership on a list is O(n), making the whole solution O(n^2).

Used nums.count(n) in the loop, again O(n) each time and causing Time Limit Exceeded.

Got confused between range(n) and range(n + 1); need to match the value range (1..n) to indices and avoid off-by-one.

Assumed the array was sorted without the problem guaranteeing it; should never rely on ordering unless it’s explicitly stated.
'''