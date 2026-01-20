class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 문자열이 반복되어야함,아니 앞에서도 뒤에서도 같아야한다는? 회문,
        # 돌아오는 문자열
        # 예시
        # babad 에서 bab, aba는 true 이고,  ba,ab, bad 는 false 
        # 뒤가 끝에 닿으면 멈춘다.
        # cbbd 에서 cb cbb..
        # 다시,,

        # 가운데로부터 대칭인지-앞에서도 뒤에서도 같으려면 대칭해야 한다. 
        # 찾으면 넣을 리스트 필요
        # 만약 문자열이 2이면? --그대로하는데, 1이면 회문은 회문이므로 리턴 s겠다
        # 주어진 조건이 1<= s <=1000 이므로 0은 고려아님.
   
        # 대칭확인을 어찌하지. 단순히 왼쪽과 오른쪽이 같으면 팰린드롬??
        # ㅇㅇ 기준점부터 동시에 하나씩 옮겨가면서 같은것을 확인하면 대칭.
        # 같을 때 움직이는 것으로해야함
        output = ""

        if len(s) <= 1:
            output = s
            return output

        # a는 중심에서 0까지는 가야하고, b는 길이 끝까지는 가야함,
        # a와 b가 같아야 커짐.
        def palindrome(a,b):
            while a >= 0 and b <= (len(s) - 1) and s[a] == s[b]:
                a -= 1
                b += 1
            return s[a + 1:b]

        # output = ""
            # mid = (a + b) /2 ,짝수면 +1
            # # a=0 , b= (len(s)-1)
            # if (a+b+1) % 2 == 1: #홀수면
            #     a,b = (a+b+1) /2 꼭 가운데가 아니어도 중요한건 대칭이니
            #     와일? a==b 일때
            #     a -= 1, b += 1 #하면서 대칭확인
            #     output.append(a:b) #대칭이면 넣고
            #     a=0 and b=(len(s)-1) #이면 종료
            #     return output 근데 문제는 제일 긴거 하나?
        
        for i in range(len(s)):
            홀 = palindrome(i, i)
            짝 = palindrome(i, i + 1)
                # if len(홀) < 2 and len(짝) <2:
                #     None
                # else:
            if len(홀) >= len(output):
                output = 홀
            if len(짝) >= len(output):
                output = 짝


                # a = (a+b+1) /2 , b = (a+b+1) /2 +1 
                # a -= 1, b += 1 #짝수일때 하면서 대칭확인
                # output.append(a:b) # 대칭이면
                # a=0 and b=(len(s)-1) #이면 종료
        return output