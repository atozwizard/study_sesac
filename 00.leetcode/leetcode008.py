"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

 
 myAtoi(string s)문자열을 32비트 부호 있는 정수로 변환하는 함수를 구현하세요 .

해당 알고리즘은 myAtoi(string s)다음과 같습니다.

공백 : 앞에 있는 공백( " ")은 무시합니다.
부호 여부 : 다음 문자가 '-'또는 인지 확인하여 부호를 결정합니다 '+'. 둘 다 없으면 긍정으로 간주합니다.
변환 : 숫자가 아닌 문자가 나오거나 문자열의 끝에 도달할 때까지 선행 0을 건너뛰면서 정수를 읽습니다. 숫자가 읽히지 않으면 결과는 0입니다.
반올림 : 정수가 32비트 부호 있는 정수 범위를 벗어나는 경우 , 범위를 유지하도록 정수를 반올림합니다. 구체적으로, 보다 작은 정수 는 로 반올림하고 , 보다 큰 정수 는 로 반올림합니다 .[-231, 231 - 1]-231-231231 - 1231 - 1
최종 결과로 정수를 반환합니다.

 
 
 

Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
Example 5:

Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.

 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""