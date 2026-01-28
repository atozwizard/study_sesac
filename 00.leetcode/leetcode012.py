"""
Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. 
Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, 
append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, 

for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 
(X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. 
You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.

 

Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII
Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV
 """

 class Solution:
    def intToRoman(self, num: int) -> str:
        class Solution:
    def intToRoman(self, num: int) -> str:
        
        """
Symbol	Value
    I	1
    V	5
    X	10
    L	50
    C	100
    D	500
    M	1000
        """
        #주어진 수를 로마자로 표기하는 것
        #일반적인경우 뺄 수 있는 가장 큰 값의 기호를 먼저 쓰고
        #그 만큼의 수를 뺀 나머지로 반복
        #338 -> CCCXXXVIII
        
        #4와 9의 경우는 예외. 큰기호 앞에 작은기호를 붙여 나타냄
        #5보다 1작음 IV, 10보다 1작음 IX
        #500보다 100작음 CD, 1000보다 100작음 CM
        # 주어지는 수는 1<= NUM <=3999

        #ro_num = (I:1, IV:4, V:5, IX:9, X:10, XL:40, L:50, XC:90, C=100, CD:400, D:500, CM:900, M:1000)
        ro_num=[(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
        
        ro_str=""

        #num = 58;
        # 가장 큰 숫자부터 확인-> num이 그 숫자보다 크거나 같다
        # 58>=50 ->  L추가 , 58-50 = 8,
        # 8>=5 ->  V추가, 8-5 = 3 ,
        # 3>=1 -> I추가, 3-1=2, 
        # 2>=1 -> I추가, 2-1=1,
        # 1>=1 -> I추가, 1-1=0, 종료 
        # return ro_str -> LVIII

        i = 0
        while i < len(ro_num):
            if num < ro_num[i][0]:
                i += 1
            else: #num >= ro_num[i][0]:
                ro_str += ro_num[i][1]
                num -= ro_num[i][0]
                if num == 0:
                    return ro_str
