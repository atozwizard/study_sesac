"""
부호 있는 32비트 정수가 주어졌을 때 x, x해당 정수의 자릿수를 반전시켜 반환합니다 . 반전 후 x값이 부호 있는 32비트 정수 범위를 벗어나는 경우 , 0을 반환합니다 .[-231, 231 - 1]0

사용 환경에서 64비트 정수(부호 있는 정수 또는 부호 없는 정수)를 저장할 수 없다고 가정해 보겠습니다.

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-2^31 <= x <= 2^31 - 1
"""
# x=123 ,x=120 ,x=-123

class Solution:
    def reverse(self, x: int) -> int:
        -2**31 <= x <= 2**31 - 1
        if x == 0:
            return x
        #문자열로변환 역순?
        # strg = str(x)
        # if x < 0 :
        #     strg = str(x)
        #     rev = strg[0] + strg[:0:-1]
        #     return rev == int(rev)  # x=123 이면, rev=321
        if -(2**31)<= x < 0 :
            strg = str(x)
            rev = strg[0] + strg[:0:-1]
            result = int(rev)  # x=123 이면, rev=321
            # result = rev
            if result < -(2**31):
                return 0
            else : 
                return result
            
        elif 0 < x <= (2**31 - 1):
            strg = str(x)
            rev = strg[::-1]
            result = int(rev)  # x=123 이면, rev=321  
            if result > (2**31 - 1):
                return 0
            else: 
                return result


class Solution:
    def reverse(self, x: int) -> int:    
        if x == 0: return 0
        if -2**31 >= x or x >= 2**31 - 1:
            return 0
        strg = str(abs(x))
        rev = strg[::-1]
        result = int(rev)
        
        if result >= 2**31 -1 :
            return 0
        if x < 0:
            return result * -1
        else: return result