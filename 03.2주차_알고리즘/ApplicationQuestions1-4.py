
02
    1.middle of a given linked list
    #중간값 찾기
    #투 포인터, slow pointer 한번에 한칸씩 이동, fast pointer 한번에 두칸씩 이동
    #fast pointer가 리스트의 끝(none)에 도달 했을 때, slow pointer는 정확히 리스트의 중간에 위치.     
        class Node():
            def __init__(self, val = 0, next = None): """val은 value데이터=0 인것은 노드를 생성할 때 실수로 데이터를 넣지 않더라도,
                                                        프로그램이 멈추지 않고 숫자 0을 기본 데이터로 가지게 한다. 주로 숫자데이터를 다룰 것이라는 점도 암시.
                                                        next=None은 이 노드가 기차의 마지막 칸임을 나타내는 중요한 신호.
                                                        처음 생성된 노드는 어디에도 연결되어있지 않으므로 아무것도 가리키지 않는 다는 뜻의 None이
                                                        가장 적절한 초기값이다."""
                self.val = val
                self.next = next
                
            def findmiddle(head:Node) -> Node:
                slow = head
                fast = head  #0이 아닌 head로 객체지정하는 것은 LinkedList 의 특성때문.
                            """노드(데이터)들이 메모리 여기저기에 흩어져 있다. 
                            각 노드는 오직 자신이 가진 next포인터를 통해서만 다음 노드가 어디있는지 알수 있다.
                            따라서, 컴퓨터는 0의 위치로 가달라고 하면 알아듣지 못함. 대신
                            기차의 맨 앞칸(head)주소를 줄테니 여기서부터 시작해 라고 알려줘야 함
                            head는 첫번째 노드 객체 그 자체. slow=0 이라 한다면 노드가 아니라 숫자0 이 됨.
                            숫자 0에는 .next라는 속성이 없기 때문에 에러"""
                
                while fast and fast.next:
                    slow = slow.next        #1칸이동
                    fast = fast.next.next   #2칸이동
                
                return slow  #slow가 가리키는 곳이 중간값
     
    2.reverse a given linked list
    #세 개의 포인터
    """링크드리스트를 뒤집으려면 현재 노드뿐만 아니라, 이전 노드와
    다음 노드의 정보가 동시에 필요함, 이전 현재 다음 포인터.prev, curr, next_node"""
    # 기차 칸들의 연결고리를 하나씩 끊어서 반대방향으로 다시 잇는 작업
        class Node():
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
                
            def reverselist(head:Node) -> Node:
                prev = None
                curr = head
                
                while curr:
                    next_node = curr.next """현재 노드의 다음노드 위치를 next_node라는 변수에 잠시 저장
                                            바로 다음 줄에서 현재노드의 다음을 이전 노드로 바꾸면, 다음 칸 포인터를 잃어버림"""
                    curr.next = prev #현재노드 다음을 뒤로 돌림
                    
                    prev = curr #현재노드가 이전노드가 됨
                    curr = next_node #다음 칸으로 넘어가서 다음 작업을 준비
                    
                return prev
                    
    3.detect cycle,circular linked
    #언젠가는 만난다, 투 포인터. 순환한다면 fast pointer는 한 바퀴를 앞질러 slow pointer를 따라잡아 만나게 된다.
        
        class Node():
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
                
            def cycle(head: Node) -> bool:
                if not head or not head.next:  """not head: 연결 리스트에 노드가 하나도 없는상태. 
                                                비교할 대상 자체가 없으므로 당연히 순환이 없다.
                                                not head.next: 첫칸 다음이없다, 노드가 하나뿐인 상태.
                                                자기 자신에게 다시 돌아오는 특수한 경우가 아니라면, 노드가 하나일때는
                                                순환이 만들어지지 않는다
                                                이런 상황들을 미리 걸러내는 예외처리 Guard Clause"""
                    return False
                
                slow = head  #출발선 정렬
                fast = head
                
                while fast and fast.next:
                    slow = slow.next #1칸이동
                    fast = fast.next.next #2칸이동
                    
                    if slow == fast: #둘이 만나면, 사이클 있다!
                        return True
                
                return False #fast가 끝에 도달하면 사이클 없음
    
    
03 괄호 balance
    use stack to check if a string with parantheses is well-formed
    "(3+4)*(2+5)" is well-formed
    "((2*2)*3+1)" is not well-formed
    ")(2+2" is not well-formed
    what if we have more than one types of parentheses?
    "{(2+1)*(3+2)-22}*7" is well-formed
    "{(7+2}*3)" is not well-formed
           
        class Solution:
            def isValid(self, s: str) -> bool:

                # TODO: 여기에 스택 기반 알고리즘을 구현하세요.

                stack = [] #괄호 쌓을 리스트
                pair = { ")" : "(" , "}" : "{", "]" : "[" }  #짝맞출 딕셔너리

                for x in s:   #s를 하나씩 순회해
                    
                    if x in pair:       #   - 닫힌 괄호일 때 pair안에 있으면
                            
                        if not stack:    #   - 스택이 비어있는 경우 False
                            return False  #pop하기 전에 비어있는지 먼저 확인해야한다

                        top = stack.pop()     #stack에 쌓은 마지막것을 꺼내, top이라 하자
                        if top != pair[x]:  #꺼낸 top이, pair의 짝과 안맞으면
                            return False  #False
                            
                    else: #   - 닫힌 괄호가 아닐 때
                        if x in "({[":
                            stack.append(x) #  stack에 append 쌓아놔

                    #   - 반복이 끝난 뒤 스택이 비어 있는지 확인
                return len(stack) == 0

            raise NotImplementedError


    implement queue using two stacks
        main idea : use the first stack for enqueue, and the other for dequeue
        whenever we get a dequeue request but the second stack is empty, pop all elements from the first stack and push them into the second stack.
    
04
    
    
    
    
    problem 1
    given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
    letters are case sensitive, for example, "Aa" is not considered a palindrome.PythonFinalizationError
        ex1:
            input : s = "abccccdd"
            output : 7
            explanation : one longest palindrome that can be built is "dccaccd", whose length is 7.
        
        ex2:
            input : s = "a"
            output : 1
            explanation : the longest palindrome that can be built is "a", whose length is 1.
            
        
    problem 2
    given a list of integers, return the smallest positive integer which is not in that list.
    ex:
        [7,2,3,5,4,1] --> 6
        [-1,5,2,3,9] --> 1
        [17,25,4308,1,99] -->2
        
        #TODO
        def smallest_missing_pos_int(self,list):
            for each item in the list:
                insert into a hash table(hastset)
            for i = 1,2,3, . . .:
                if the hash table contains i : keep going
            else :return i
            
            
    problem 3 two sum
    given an array of integes nums and an integer, return indices of the two numbers such that they add up to target.
    you may assume that each input would have exactly one solution, and you may not use the same element twice.
    you can return the answer in any order.
    
    ex1:
        input: nums = [2,7,11,15], target = 9
        output: [0,1]
        explanation: Beacuse nums[0] + nums[1] == 9, we return [0,1].append
        
    ex2:
        input: nums = [3,2,4], target = 6
        output: [1,2]
        
    ex3:
        input: nums = [3,3], target = 6
        output: [0,1]
        
    brute force
    from typing import List

    def two_sum_bruteforce(nums: List[int], target: int) -> List[int]:
        """Two Sum 문제를 브루트 포스 방식으로 해결합니다.

        시간복잡도: #전체를 비교하기위해 인풋 n개를 n번만큼 n회 비교하니까 시간복잡도가 O(N^2)
            TODO: 왜 이 알고리즘의 시간복잡도가 O(N^2)인지 설명을 적어보세요.
        """

        # TODO: 이중 for 문을 사용해 모든 (i, j) 쌍을 확인하고,
        #       합이 target이 되는 인덱스를 찾아 반환하세요.
        #       정답이 하나만 존재한다고 가정해도 됩니다.
        
        for i in range(len(nums)):  # 첫번째 인덱스 숫자
            for j in range(i + 1, len(nums)): # 두번째 인덱스 숫자
                if nums[i] + nums[j] == target:
                    return(nums[i],nums[j])   #인덱스 반환받아야하니까 return함수 // 출력이 아니라 반환하세요라고함

        #전체를 비교하기위해 인풋 n개를 n번만큼 n회 비교하니까 시간복잡도가 O(N^2)
        raise NotImplementedError
    
    hash map
    def two_sum_hashmap(nums: List[int], target: int) -> List[int]:
        """Two Sum 문제를 해시맵 방식으로 해결합니다.

        시간복잡도: 리스트를 n개만큼 한번씩만 순회하면서 값을 찾으니 O(N)
            TODO: 왜 이 알고리즘의 시간복잡도가 O(N)인지 설명을 적어보세요.
        """
        # TODO: dict를 사용하여, 한 번의 순회로 정답을 찾는 코드를 작성해 보세요.
        # 예시 아이디어:
        #   - seen = {}
        #   - for i, num in enumerate(nums):
        #         need필요한 값 = target - num
        #         need필요한 값이 seen에 있는지 확인 if need in seen :
        #         없다면 현재 값과 인덱스를 seen에 저장 append?, return [seen[need]]
        
        seen = {} # 
        
        for i , num in enumerate(nums): #enumerate로 인덱스와 값을 동시에 순회,
            need = target - num
            if need in seen: #need가 seen에 있는지 확인,있으면
                return [seen[need],i] #있는 그 값의 인덱스, 인덱스 내놔
            seen[num] = i  #없으면 seen에 i인덱스에 need 구할때 넣은 num값을 넣어놔

        
    # 거짓일때는?? 반환 안됨

    #타겟값이 정해져 있어서 가능한거잖음. 값이 정해져 있을때에만 답을 찾는건가.
        #타겟이 주어지지 않는다면 n^2만큼 돌려서 타겟을 만든 다음, 검증해야하는?  
        #????
        # 무얼 찾아야 하는지 타켓이 명확할 때 사용할 수 있는 솔루션이겠다.
        raise NotImplementedError

