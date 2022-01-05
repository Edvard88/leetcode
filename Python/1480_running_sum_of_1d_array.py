from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        reslut = []

        for i, _ in enumerate(nums):
            sum_result = 0

            for index in range(i + 1):
                sum_result += nums[index]

            reslut.append(sum_result)

        # Version 2
        # for i, _ in enumerate(nums):
        #     reslut.append(sum(nums[:i + 1]))

        return reslut

if __name__ == '__main__':
    input = [1,2,3,4]

    solution = Solution()
    result = solution.runningSum(input)

    print(result)