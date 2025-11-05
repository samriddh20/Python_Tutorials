from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

def build_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

if __name__ == "__main__":
    s = Solution()
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])


    result = s.addTwoNumbers(l1, l2)
    print_list(result)  # Output: [7, 0, 8]

# # # a = 7%10
# # # print(a)


# a = ListNode(val=2, next=ListNode(4, next=ListNode(3)))
# print_list(a)

