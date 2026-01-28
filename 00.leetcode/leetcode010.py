"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #정규표현식 " . ", " * "
        # a* = "", "a", "aa", "aaa" 무한대 모두 가능
        # . = 임의의 한 문자
        # for문으로 어렵다 s 와 p의 길이가 다를  수 있음
        strg_p = ""
        # if s == strg_p :return True
        # for i in range(len(s)):
            if p[i] == s[i] : strg_p += s[i]
            if p[i] != s[i] :
                if p[i] =="*" : strg_p += s[i]와 같은 이어진 인덱스 전부 추가
                if p[i] =="." : strg_p += s[i]
            print(strg_p)
        if strg_p == s : return True
        else : False

# class Solution:
    # def isMatch(self, s: str, p: str) -> bool:
        #정규표현식 " . ", " * "
        # a* = "", "a", "aa", "aaa" 무한대 모두 가능
        # . = 임의의 한 문자
        # for문으로 어렵다 s 와 p의 길이가 다를  수 있음-->인덱스에러
        # strg_p = ""
        # if s == strg_p :return True
        # for i in range(len(s)):
        # i = 0 # s
        # j = 0 # p
        # while j <len(p):
        # if j +1 < len(p) and p[j+1] == '*':
            # return self.isMatch(s[i:], p[j+2:]) or (match and self.isMatch(s[i+1:], p[j:]))
                # match = i <len(s) and ((p[j] == s[i]) or p[j] == '.')
                # if match:
                #     i += 1
                # else :
                #     j += 2
                # strg_p += s[i:i+2]
                # i += 2
                # j += 2
        # else:
            # if i < len(s) and (p[j] == s[i] or p[j] == '.'):
                # strg_p += s[i]
                # i += 1
                # j += 1
            # else : break
            # if p[i] == s[i] : strg_p += s[i]
            # if p[i] != s[i] :
            #     if p[i] =="*" : strg_p += s[i] # 같은 이어진 인덱스 전부 추가
            #     if p[i] =="." : strg_p += s[i]
            # print(strg_p)
        # if strg_p == s : return True
        # if strg_p != s : return False
        # return i == len(s) and j == len(p)

                # if i +1 < len(p) and p[i+1] == "*":
                # if len(p) >= 2 and p[1] == "*":


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 1. 종료 조건: 패턴이 비어있으면 문자열도 비어있어야 성공
        if not p:
            return not s

        # 2. 첫 번째 글자가 매칭되는지 확인 (안전장치 포함)
        match = bool(s) and (p[0] == s[0] or p[0] == '.')

        # 3. '*' 처리 (다음 글자가 '*'인 경우)
        if len(p) >= 2 and p[1] == '*':
            # 선택지 1: * 앞글자를 0번 사용 (패턴만 2칸 건너뛰기)
            # 선택지 2: * 앞글자를 1번 이상 사용 (현재가 match라면 s만 한 칸 전진)
            return self.isMatch(s, p[2:]) or (match and self.isMatch(s[1:], p))

        # 4. 일반 문자 혹은 '.' 처리
        else:
            # 현재 match이고, 다음 글자들도 매칭되어야 함
            return match and self.isMatch(s[1:], p[1:])