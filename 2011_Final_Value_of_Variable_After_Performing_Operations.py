#https://leetcode.com/problems/final-value-of-variable-after-performing-operations/


from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0

        for elem in operations:
            if elem in ("--X", "X--"):
                result -= 1
            else:
                result += 1

        return result

if __name__ == '__main__':

    solution = Solution()

    input = ["--X","X++","X++"]
    result = solution.finalValueAfterOperations(input)
    print("result: ", result)


