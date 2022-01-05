class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_list=[]
        for index1, num_1 in enumerate(nums):
            for index2 , num_2 in enumerate(nums):
                if (num_1 + num_2) == target and (index1!=index2):
                    index_list.append(index1)
                    index_list.append(index2)
                    return index_list
        return index_list
        
