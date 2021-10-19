# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merge_list = ListNode()
        print(l1.val)
        print(l1.next)

        # while (l1.next is not None):
        #     if l1.val <= l2.val:
        #         merge_list.val = l1.val
        #         l1.next
        #     else:
        #         merge_list = l2.val
        #         l2.next
        # return merge_list

if __name__ == '__main__':
    sol = Solution()
    sol.mergeTwoLists()