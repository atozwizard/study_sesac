"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #1. 결과를 담을 가짜(Dummy) 노드를 하나 만듭니다. (결과 리스트의 시작점 역할)
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        # 2. 현재 어느 위치에 노드를 만들지 가리킬 'curr' 포인터를 만듭니다.
        # 3. 올림수를 저장할 변수 'carry'를 0으로 초기화합니다.

        # 4. 루프를 시작합니다 (l1이 존재하거나, l2가 존재하거나, carry가 남아있는 동안)
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else: val1 = 0
            if l2:
                val2 = l2.val
            else: val2 = 0
            # 4-1. l1에서 값을 가져옵니다 (더 이상 없으면 0)
            # 4-2. l2에서 값을 가져옵니다 (더 이상 없으면 0)
            
            # 4-3. 합계(sum) 계산: l1값 + l2값 + carry
            sum = val1 + val2 + carry #자리수 더하고 올림수carry까지 더하기
            carry = sum // 10 #10으로 나눈 몫이 다음자리로 넘길 값이되고
            val = sum % 10 #10으로 나눈 나머지가 남을 값. 

            # 4-4. 새로운 carry 계산: sum // 10
            # 4-5. 현재 자리에 남을 값 계산: sum % 10
            
            # 4-6. 계산된 값을 가진 새 노드를 만들어 curr.next에 연결합니다.
            curr.next = ListNode(val)
            curr = curr.next

            if l1: 
                l1 = l1.next #다음 노드로 넘어가자, 다음노드도 계산해야하니
            if l2: 
                l2 = l2.next

            # 4-7. curr, l1, l2 포인터를 다음으로 이동시킵니다.

        # 5. dummy 노드의 다음 노드(진짜 결과의 시작)를 반환합니다.
        return dummy.next