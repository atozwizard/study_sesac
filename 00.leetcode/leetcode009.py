"""Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #-(2**31) <= x <= (2**31 - 1)
        # 주어진 정수의 절대값의 팰린드롬 확인 ture
        # if 음수확인: return false
        # s = str(abs(x))
        # for i in range(len(s)) ?
        # 투 포인터, 양 끝에서 하나씩 들어와?
        # if [i] = [len(s)-i]: i += 1
        #       if i = (len(s)-i) return true
        # if [i] != [len(s)-i]: return false break
        # 틀린것만 거르면 나머지 True
        # i range //2

        if (str(x))[0] == "-":
            return False
        strg_x= str(abs(x))
        # for i in range(len(strg_x)//2):
        #    """ # if strg_x[i] == strg_x[(len(strg_x)-1)-i] :
        #     #     # i += 1
        #     #     if i == len(strg_x)-i : #
        #     #         return True
        #     #     elif i == (len(strg_x) / 2) :
        #     #         return True  """
        #     if strg_x[i] != strg_x[(len(strg_x)-1)-i] :
        #         return False
            
        # return True


        # 거꾸로 뒤집은 문자열과 같으면 True 아니면 False
        return strg_x == strg_x[::-1]