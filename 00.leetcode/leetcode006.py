"""
he string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 지그재그
        # ㅣ /ㅣ
        # ㅣ/ ㅣ
        # ㅣ  ㅣ
        
        #numRows 가 정해져 있다!
        # 각 행에 문자열을 적을 list가 필요하고, 다 끝나면 이것을 행 순서대로 하나의 문자열로 도출한다.
        # row = ['']*numRows, result = ([]*numsrows 전부 순서대로)
        
        # #처음엔 아래로 내려감 row == 1 시작
        # 열을 내려가면서 s의 인덱스[0] 을 빼서 넣는다 (s[0].pop)
        # 이동하면서 적은 글자 Write=[]에 하나씩 넣는다 write.append(s[i+=1])
        # 남은 문자열이 없으면 중지 (len(s) = 0, 중지), 결과도출
        # 방향을 나타낼 변수가 필요? Direct 아래로 +, 위로 -(역방향)
        #    --> row += step  바닥에 닿으면 step = -1, 천장에 닿으면 step = 1  
        
        # for i in len(s):        
        #    -->  for char in s: "문자열 s 를 처음부터 끝까지 한번 훑기, 문자열이 긑나는 순간 자동으로 종료"
        # if 바닥에 닿았을 때 (row = numRows;) , 
        #   남은 문자열 길이(len(s)-numRows)가 0과 같거나 작으면 중지.
        #   (len(s)-numRows) <= 0 ; 중지
        
        # -남은 문자열 있으면 (len(s)-numRows) > 0;
        # len(s) > numRows ; 방향이 위로 바뀜, direct -> (-)
        # numRows만큼 열을 옮겨가며 
        # 한 글자 씩 넣으며 올라감 ((col += 1) <= numrows -> 0< row -=1 ;)
        
        # 다시 위에 닿으면(row = 1 ;) 방향 아래로 direct -> (+), 남은 문자열 길이 없으면 중지
        # 
        
        # if numRows == 1 or numRows >= len(s):
        #     return s
        
        # rows = [""] * numRows
        # curr_row = 0
        # curr_col = 0
        # direct = 1
        
        # for i  in s:
        #     rows[curr_row] += i
        #     if curr_row == 0:
        #         direct = 1
        #         curr_row += direct
        #         return "".append(rows)        끝까지 가야하는데 첫번부터 for문을 빠져나가게됨 xxx
            
        #     elif curr_row == numRows -1:
        #         direct = -1
        #         curr_row += direct
        #         curr_col += 1
        #         return "".append(rows)
        
        # return rows
    
    
    

        # if numRows == 1 or numRows >= len(s):
        #     return s
                
        # rows = [''] * numRows
        # curr_row = 0
        # curr_col = 0
        # direct = 1
                
        # for i  in s:
        #     rows[curr_row] += i
        #     if curr_row == 0:
        #         direct = 1
        #         curr_row += direct               이해가 잘 안됨. 이 구절을 if와 elif 밖에서 하나로 쓰게하니 작동됨 왜지
        #if , elif 밖에서 curr_row가 하나씩 더해져야- 그러니까 curr_row가 0이거나 numRows-1 이 아닐때에 curr_row가 하나씩 더해져야하는데
        # if와 elif 안에만 있으면 curr_row가 0이거나 numRows-1 일 때에만 curr_row가 하나씩 더해지므로 오류이다. 그러므로 아래처럼 고쳤다!!
                
                    
        #     elif curr_row == numRows -1:
        #         direct = -1
        #         curr_row += direct
        #         curr_col += 1
                
                
        # return "".join(rows)


        if numRows == 1 or numRows >= len(s):
            return s
                
        rows = [''] * numRows
        curr_row = 0
        curr_col = 0
        direct = 1
                
        for i  in s:
            rows[curr_row] += i

            if curr_row == 0:
                direct = 1
            elif curr_row == numRows -1:
                direct = -1
                curr_col += 1
                                
            curr_row += direct    
                
        return ''.join(rows)
            