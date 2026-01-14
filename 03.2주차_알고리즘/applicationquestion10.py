class Solution:
    def climbStairs(self, n: int) -> int:
        """
        반복 DP를 사용해 f(n)을 계산하는 함수입니다.
        점화식 기반으로 bottom-up 방식으로 구현하세요.

        요구사항:
        - n=1,2 에 대한 에지 케이스 처리
        - O(n) 반복 DP
        """
        if n <= 2:  ##계단이 1개나 2개 일때는 바로 반환
            return n  ##엣지케이스 처리됨

        dp = [0]*(n + 1) 
        """인덱스 번호를 계단 칸수와 맞추기위해서 n+1,
        0을 n+1번 반복해서 리스트를 만들어놔
        ex>n=5,dp = [0,0,0,0,0,0]
        
        하필 인덱스에 0을 넣어 리스트를 만드는 것은, 
        비어있음, 아직 값이 채워지지 않음을 의미하는 초기값이다!!
        
        나중에, 코드를 실행하면서 dp[3] = 3 처럼 값을 채워넣을 텐데
        만약 값이 안바뀌고 여전히 0 이라면 아직 계산이 안됬거나 방법이
        없구나- 라고 알수있대"""

        dp[1] = 1
        dp[2] = 2  # 초기값처리, f(n) = f(n-1) + f(n-2), n >2 임

        for i in range(3, n + 1):  #n은 값이 주어질거고, 3부터 n+1까지 루프를 돌건데.
            dp[i] = dp[i-1] + dp[i-2]  #n이 3이면 range(3,4) 이고, range는 끝 숫자는 포함하지않으므로
                                        # i는 3 딱 하나만 실행된다

        return dp[n] #원하는 것은 n개의 계단을 오르는 방법의 총 가짓수 이므로
                    #for 반복문이 끝나고나면, 마지막 계산값인 dp[n]값을 출력해야
                    #우리가 원하는 값을 알 수 있다
        
        # TODO: 코드를 완성하세요.
        raise NotImplementedError



def run_tests():
    sol = Solution()
    tests = [1,2,3,10,45]
    for n in tests:
        print(f"n={n}, ways={sol.climbStairs(n)}")

run_tests()