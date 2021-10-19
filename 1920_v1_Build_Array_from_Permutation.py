from typing import List
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []

        # for i in range(len(nums)):
        #     ans.append(nums[nums[i]])

        ans = [nums[nums[i]] for i in range(len(nums))]
        return ans

if __name__ == '__main__':
    input = [0,2,1,5,3,4]

    solution = Solution()
    result = solution.buildArray(input)

    print(result)
