def linear_search(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i
    return -1

def binary_search(list, value):
    first = 0
    last = len(list) -1
    
    while first <= last:
        mid = (first + last) // 2
        if list[mid] == value: #찾는 값이 중간값과 같다, 찾았다
            return mid  #찾은 중간인덱스 반환
        elif list[mid] < value: #중간값이 찾는 값보다 작으면
            first = mid + 1 #중간인덱스의 오른쪽1칸을 시작점으로 옮겨서 다시 서치
        else:   #중간값이 찾는 값보다 크면
            last = mid -1 #중간인덱스 한칸 앞의 인덱스를 끝점으로 두고 다시 서치
    return -1

"""
1. does the binary search work when the list contains duplicates?
    - to make it retrun any of those duplicates?
     >>지금의 코드가, 중복 데이터 중 탐색 과정에서 가장 먼저 mid로 잡힌 위치가 반환된다
   
    - to make it return the leftmost one?
    >>가장 왼쪽 인덱스 반환
    
    result = -1 #찾지못하면 -1 반환시킬 기본값
    while fist <= last:
        mid = (first + last) //2
        if list[mid] == value:
            result = mid  #같은 값을 찾으면 일단 기록
            last = mid -1 #왼쪽을 더 확인
        ...
    return result
    
    - to make it return the rightmost one?
    >>>가장 오른쪽 인덱스 반환
    
    result = -1 #찾지못하면 -1 반환시킬 기본값
    while fist <= last:
        mid = (first + last) //2
        if list[mid] == value:
            result = mid  #같은 값을 찾으면 일단 기록
            last = mid +1 #오른쪽을 더 확인
        ...
    return result
    
2. find the first element greater than or equal to the query
>>>크거나 같은 첫번째 원소 찾기

result = -1 #찾지못하면 -1 반환시킬 기본값
    while fist <= last:
        mid = (first + last) //2
        ## 현재 중간값이 query보다 크거나 같으냐
        if list[mid] >= value:
            result = mid  #그렇다면 저장해라
            last = mid -1 #더 작은 인덱스에도 있는지 확인
        else:             #아니다 더 작다
            first = mid + 1     #그러면 중간인덱스의 오른쪽 1칸부터 시작점으로 다시 서치
    return result
"""

"""
result = -1, 또는 return -1 왜???

**찾는 조건에 맞는 데이터가 리스트에 단 하나도 존재하지 않을 겅우**
를 처리하기 위한 표준적인 약속이에요

파이썬을 포함, 대부분 프로그래밍 언어에서 리스트의 인덱스는 0부터 시작.
0이상의 정수: 리스트 내에 실제로 존재하는 위치를 의미
-1: 리스트에 존재할 수 없는 인덱스. 탐색이 끝났는데 결과값이 -1이라면,
    모든 칸을 다 뒤져봤지만 조건에 맞는 값을 찾지 못했다 는 신호.
    

루프 종료 후 상태를 판별하기 위해서도 쓰여요
위의 이진탐색은 while first <= last 조건이 깨져야 종료되요.
만약 result를 설정하지 않고 mid를 그대로 쓰려고하면, 루프가 끝난 시점의
mid값은 마지막으로 검사했던 위치일뿐, 우리가 찾던 정답인지는 보장할 수 없음.

반면 result = -1로 시작해서 조건을 만족할 때만 result = mid로 업데이트 하면,
루프가 끝난 후 result값이 변했는지(-1이 아닌지)만 보고 성공여부를 알 수 있음???
"""




#problem 1 binary search
"""search insert position
given a sorted array of distinct integers and a target value, 
return the index if the target is found. if not return the index
where it would be if it were inserted in order.

you must write an algorithm with O(logn) runtime complexity


ex1>>
input: nums = [1,3,5,6], target = 5
output: 2

ex2>>
input: nums = [1,3,5,6], target = 2
output: 1

ex3>>
input: nums = [1,3,5,6], target = 7
output: 4
"""
def insert(nums, target):
    first = 0
    last = len(nums) -1 
    result = len(nums)
    
    while first <= last:
        mid = (first + last) //2
        
        if nums[mid] == target:
            return mid #찾으면 인덱스 반환
        
        elif nums[mid] < target:
            first = mid +1
            
        else: #nums[mid] > target
            result = mid
            last = mid -1
    return result



#problem 2 recursion
"""fibonacci number
the fibonacci numbers, commonly denoted F(n) form a sequence,
called the Fibocacci sequence, such that each number is the sum of two
preceding ones, starting from 0 and 1. that is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

given n, calculate F(n)

ex1>>>
input: n=2
output: 1
explanation: F(2) = F(1) + F(0) = 1+0 = 1

ex2>>>
input: n=3
output: 2
explanation: F(3)=F(2) +F(1) = 1+1 = 2

ex3>>>
input: n=4
output: 3
explanation: F(f) = F(3)+F(2) = 2+1 = 3"""

def fib(n):
    if n <=1:
        return n
    return fib(n-1) + fib(n-2)



from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """회전된 정렬 배열에서 target의 인덱스를 찾습니다.

        아이디어:
            - 매 반복마다 mid를 기준으로 왼쪽/오른쪽 중 어느 쪽이 정렬 구간인지 판별합니다.
            - target이 정렬된 구간 안에 속하는지에 따라 탐색 범위를 절반으로 줄입니다.

        시간복잡도:
            - 매 단계마다 탐색 범위를 절반으로 줄이므로 O(log n) 입니다.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[left] <= nums[mid]:
                    if nums[left]<= target < nums[mid]:
                        right = mid - 1
                    else: left = mid + 1
                                            
                else: # nums[right] >= nums[mid]
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else: right = mid - 1
        return -1
        # TODO: while 루프 안에서 mid를 계산하고,
        #       정렬된 구간을 판별한 뒤, target의 위치에 따라
        #       left/right 를 조정하는 로직을 작성해 보세요.
        # 힌트:
        #   - if nums[mid] == target: 바로 mid 반환
        #   - elif 왼쪽 구간이 정렬되어 있다면:
        #        target이 왼쪽 구간에 속하는지 비교 후, left/right 이동
        #   - else: 오른쪽 구간이 정렬되어 있는 경우
        #        target이 오른쪽 구간에 속하는지 비교 후, left/right 이동

        raise NotImplementedError
