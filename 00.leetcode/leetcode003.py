"""Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces."""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0  #계속 +1
        left = 0   #문자중복되면 +1
        save = {} #위치저장용
        maxlen = 0

        for right in range(len(s)):
            if s[right] in save and save[s[right]] >= left: #문자가 중복이면
                left = save[s[right]] + 1 #갈때마다 save에 위치와 문자저장
            save[s[right]] = right # 중복된 글자가 save에 있더라도, 그 위치가 현재 left보다 크거나 같을 때만 : left + i ,문자저장하고      
            maxlen = max(maxlen,right - left + 1)
            
         #오른쪽 왼쪽 인덱스가 0 일때 문자열은 1이므로
        return maxlen     

""""내가 만난 글자와 그 위치를 기억하려면 어떤 자료구조(딕셔너리, 배열 등)를 쓰는 게 가장 편할까요?"
딕셔너리?
"Left를 옮길 때, 이전에 이미 지나간 중복 글자를 무시하기 위한 조건은 무엇일까요? i를 더한다

"""