class Node():
    def __init__(self,x):
        self.item = x
        self.next = None

class LinkedList():
    def __init__(self):
        self.first = None
        self.size = 0 #처음 사이즈 0으로 지정
    
    def insert(self, x, i):
        #insert x at [i]
        
        # new_node = Node(x)
        # pos = 0
        # curr = self.first
        # while pos < i - 1:
        #     curr = curr.next
        #     pos += 1
        # new_node.next = curr.next
        # curr.next = new_node
        # 엣지케이스 발생, 제일 왼쪽에 넣을때-제일 앞에 넣을때    
        
        if i < 0 or i > self.size:  #제미니 
            return  #범위 밖이면 무시
        
        new_node = Node(x)
        
        if i == 0:
    
            new_node.next = self.first
            self.first = new_node
            self.size += 1  #넣을 때마다 사이즈 1씩 커짐
            
        else:
            
            i <= self.size
    
            pos = 0
            curr = self.first
            while pos < i - 1:
                curr = curr.next
                pos += 1
            new_node.next = curr.next
            curr.next = new_node    
            self.size += 1  #넣을 때마다 사이즈 1씩 커짐, 인서트를 할 때마다 사이즈가 유동적으로 바뀜, 시간복잡도 O(1)안에 i가 이 안에 있는지 해결.
    
    
    def get(self,i):  #제미니
        #get item at [i]
        #TODO
        if i < 0 or i >= self.size:
            return None
        
        curr = self.first
        for _ in range(i): #i번 점프하면 i번째 노드 도착
            curr = curr.next
        return curr.item
    
    
    def delete(self, i):
        #delete item at [i]
        
        #1. 인덱스 범위 확인
        if i < 0 or i >= self.size:
            return None #혹은 에러메시지출력
        
        #2. 첫번째 노드 삭제 ( i == 0)
        if i == 0:
            self.first = self.first.next
        
        #3. 중간 또는 마지막 노드 삭제
        else:
            pos = 0
            curr = self.first
            #삭제할 노드의 '직전'까지 이동 
               
            while pos <i - 1:
                curr = curr.next
                pos += 1
            #'직전' 노드의 손을  '다음다음'노드와 연결(중간 노드 건너뛰기)
            curr.next = curr.next.next
        #4. 공통작업 : 사이즈 감소
        self.size -= 1

    #스택에서 데이터가 비었냐고 물어볼 때 필요        
    def is_empty(self):
        return self.size == 0
        
    #LinkedList() 한 방향으로만 간다
    # insert와 delete: "위치만 알면" $O(1)$이지만, 그 위치까지 찾아가야 하므로 결과적으로 $O(N)$이 걸립니다
    # 배열과 차이점: 배열은 get(i)가 $O(1)$이지만, 연결 리스트는 앞에서부터 하나씩 세어야 하므로 get(i)도 $O(N)$입니다.
    # 작성하신 코드에서 self.size를 관리하신 건 아주 훌륭한 전략입니다! 덕분에 get이나 insert 시에 리스트 끝까지 가보지 않고도 유효한 인덱스인지 $O(1)$만에 판단할 수 있게 되었네요.

class Stack(): #array,list
    def __init__(self):
        self.data = []
        self.top = -1
        
    def push(self,x):
        self.data.append(x)
        self.top += 1
        
    def peek(self):
        if not self.is_empty():
            return self.data[self.top]
        else: return None
        
    def pop(self):
        if not self.is_empty():
            del self.data[self.top]
            self.top -= 1            
        else: return None
    
    def is_empty(self):
        return (self.top == -1)

class Stack():  #LinkedList 
    
    def __init__(self):
        self.data = LinkedList()
        
    def push(self,x):
        self.data.insert(x,0)
        #--------위에서 적용함 "self.data = LinkedList()"
        
    def peek(self):
        return self.data.get(0)
    
    def pop(self):
        self.data.delete(0)
        
    def is_empty(self):
        return self.data.is_empty()
    
    #맨 앞에 넣고 빼는 작업이 항상 O(1)로 일정
    #배열 기반 리스트처럼 메모리를 미리 크게 잡거나, 꽉찼을때 resizing 이사 하는 과정이 필요없다. 노드만 추가하면 무한히 늘어남
    
class Queue():  #array,list
    def __init__(self):
        self.data = []
        self.last = -1
    
    def enqueue(self,x):
        #insert
        self.data.append(x)
        self.last += 1
    
    def peek(self):
        if not self.is_empty():
            return self.data[0]
        else: return None
        
    def dequeue(self):
        if not self.is_empty():
            del self.data[0]
            self.last -= 1
            
    def is_empty(self):
        retrun (self.last == -1)
        
class Queue():  #LinkedList
    def __init__(self):
        self.data = LinkedList()
        self.last = None    #꼬리(마지막노드)를 기억하는 포인터
     
    def enqueue(self,x):
        #self.data.insert(x, ?)
        
        new_node = Node(x)
        
        if self.is_empty(): 
            #큐가 비어있다면 머리와 꼬리가 모두 새 노드일 테니
            self.data.first = new_node
            self.last = new_node
        else:
            #꼬리의 다음에 새 노드를 붙이고, 꼬리포인터 갱신해라
            self.last.next = new_node
            self.last = new_node
                
        self.data.size += 1
                
    
    def peek(self):
        return self.data.get(0)
        
    def dequeue(self):
        if self.is_empty():
            return None
        
        #1. 맨 앞의 데이터 지워
        removed_item = self.data.delete(0)
        #2. 하나 남았던걸 지워서 비게되면 last도 비움
        if self.is_empty():
            self.last = None
        return removed_item
    
    def is_empty(self):
        return self.data.is_empty()
    
    
##Tree

class TreeNode():
    def __init__(self,x):
        self.item = x
        self.left = None
        self.right = None
        
class BinaryTree():
    def __init__(self, node=None):
        self.root = node
        
    def preorder(self, node):
        if node is not None:
            print(node.item,end = " ")
            self.preorder(node.left)
            self.preorder(node.right)
        
    
    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print(node.item, end = " ")
            self.inorder(node.right)
        
        
    def search(self, root, key):
        if root is None:
            return None #not found 
        """base case, empty BST : Not found  키가 없으면 없다고 리턴"""
        
        if key == root.item :
            return root #found
            
        if key < root.item :
            return self.search(root.left, key)
        
        else : #key > root.item
            return self.search(root.right, key)
            
    def insert(self, root, item):
        if root is None:
            new_node = TreeNode(item)
            return new_node
        elif item == root.item:
            #error : already exists
            """base case : create now node"""
        elif item < root.item:
            new_subtree = self.insert(root.left, item)
            root.left = new_subtree
            return root
        else: #key > root.item
            new_subtree = self.insert(root.right, item)
            root.right = new_subtree
            return root
        
    def delete(self, root, key):
        if root is None:
            return root
        
        if key < root.item:
            root.left = self.delete(root.left, key)
            
        elif key > root.item:
            root.right = self.delete(root.right, key)
            
        else:
            if root.left is None:
                new_root = root.right
                root = None
                return new_root
            
            elif root.right is None:
                new_root = root.left
                root = None
                return new_root
            
            else:
                im_su = self.get_immediate_successor(root)
                root.item = im_su.item
                root.right = self.delete(root.right. im_su.item)
                
            return root
        
    def get_immediate_successor(target):
        curr = target.right
        while curr.left is not None:
            curr = curr.left
        return curr
    
    
##graph G=(V,E) V:vertices(nodes)하나의 분기점  E:edge 노드와 노드를 연결하는 선, 길

"""undirected graph -> adjacency List ; function"""
class undirected_graph():
    def __init__(self, nodes, edges):  #노드 리스트 복사
        self.v = nodes[:]  #인접 리스트 초기화(딕셔너리 생성)
        self.e = {}
        
        for node in nodes:
            self.e[node] = []
            
        for (u,v) in edges:  #edge추가 : 무방향이므로 양쪽 모두에 추가
            self.e[v].append(u) #v에서 u로 가는 길
            self.e[u].append(v) #u에서 v로 가는 길
            
#input
v = ['a', 'b', 'c']
e = [('a','b'), ('b','c')]
graph = undirected_graph(v,e)
print(graph.e)

#output
{'a':['b'], 'b':['a','c'], 'c':['b']}
        ## 각 노드를 키로 하고 그 노드와 직접 연결된 이웃 노드들을 리스트에 담는 방식
        ## undirected 양방향 통행, 그래서 양쪽에 서로 등록해주어야함
        ## 연결된 간선 수만큼 메모리를 쓰므로 효율적 O(V+E)
        ## 특정 녿의 이웃이 누구인가를 물었을 때 즉시 도출이 됨
        

###DFS
##수도코드
def dfs(self):
    unvisted = self.v.copy()
    stack = stack()

    while not unvisited.is_empty():
        visit(unvisited[0]) #visit origin
        stack.push(unvisted[0])
        del unvisted[0]
        
        while not stack.is_empty():
            curr = stack.peek()
            if there remains an unvisited city from curr:
                next = select an unvisited city from curr
                visit(next)
                stack.push(next)
                delete next from unvisited
                
            else:
                stack.pop() #backtracking


##DFS python
class undirected_graph():
    def __init__(self, nodes, edges):
        self.v = nodes[:] # 1. 노드 목록('a','b' 등)을 복사해서 저장합니다.
        self.e = {node: [] for node in nodes} # 2. 각 노드별로 연결된 이웃을 담을 빈 리스트를 만듭니다.
        for (u, v) in edges:
            self.e[u].append(v) # 3. u의 이웃 목록에 v를 추가합니다.
            self.e[v].append(u) # 4. v의 이웃 목록에 u를 추가합니다. (무방향이므로 양쪽 처리)

    def dfs(self):
        unvisited = self.v[:] # 5. '아직 안 가본 곳' 목록에 모든 노드를 넣습니다.
        visited_order = []    # 6. 방문한 순서대로 노드를 저장할 결과 바구니입니다.
        stack = []            # 7. 되돌아올 길을 기억할 '스택' 공간입니다.

        while unvisited: # 8. 아직 안 가본 곳이 하나라도 있다면 계속 반복합니다.
            start_node = unvisited[0] # 9. 목록의 맨 앞에 있는 노드를 시작점으로 잡습니다.
            
            visited_order.append(start_node) # 10. 결과 바구니에 시작점을 넣습니다.
            stack.append(start_node)         # 11. 스택에 시작점을 넣습니다. (이제 여기서부터 탐색 시작)
            unvisited.remove(start_node)     # 12. 방문했으니 '안 가본 곳' 목록에서 지웁니다.
                
            while stack: # 13. 스택에 노드가 남아있는 동안(되돌아올 길이 있는 동안) 반복합니다.
                    curr = stack[-1] # 14. 현재 위치를 스택의 가장 위(최근 방문지) 노드로 설정합니다. (peek)
                    
                    found_next = False # 15. 다음으로 갈 곳을 찾았는지 표시하는 깃발입니다.
                    for neighbor in self.e[curr]: # 16. 현재 노드의 이웃들을 하나씩 검사합니다.
                        if neighbor in unvisited: # 17. 만약 그 이웃이 아직 안 가본 곳이라면?
                            visited_order.append(neighbor) # 18. 즉시 방문 순서에 기록합니다.
                            stack.append(neighbor)         # 19. 스택에 넣어서 더 깊이 들어갈 준비를 합니다.
                            unvisited.remove(neighbor)     # 20. 안 가본 곳 목록에서 지웁니다.
                            found_next = True # 21. 갈 곳을 찾았다고 표시합니다.
                            break # 22. 중요! '깊이 우선'이므로 더 찾지 않고 바로 다음 노드로 점프합니다.
                
                    if not found_next: # 23. 만약 현재 위치에서 더 이상 갈 수 있는 안 가본 이웃이 없다면?
                        stack.pop() # 24. 스택에서 현재 노드를 뺍니다. (즉, 한 칸 뒤로 되돌아갑니다.)
                        
        return visited_order
                
                
###BFS
##수도코드
def bfs(self):
    unvisited = self.v.copy()
    queue = Queue()
    while not unvisited.is_empty():
        queue.enqueue(some unvisited node)
        
        while not queue.is_empty():
            curr = queue.dequeue()
            visit(curr)
            delete curr from unvisited
            
            for city in all unvisited cities connected from curr:
                queue.enqueue(city)
                
                
##BFS python
from collections import deque

class UndirectedGraph:
    def __init__(self, nodes, edges):
        self.v = nodes[:]
        self.e = {node: [] for node in nodes}
        for u, v in edges:
            self.e[u].append(v)
            self.e[v].append(u)

    def bfs(self):
        unvisited = self.v[:]  # 1. 아직 방문하지 않은 전체 노드 목록 복사
        visited_order = []     # 2. 방문이 완료된 순서대로 기록할 리스트
        queue = deque()        # 3. 먼저 들어온 것을 먼저 처리할 큐(FIFO) 생성

        while unvisited:       # 4. 전체 노드 중 아직 방문 안 한 곳이 있다면 반복
            start_node = unvisited[0] # 5. 방문하지 않은 노드 중 하나를 시작점으로 선택
            queue.append(start_node)  # 6. 시작 노드를 큐에 삽입
            unvisited.remove(start_node) # 7. 큐에 들어간 순간 '방문 예정'이므로 목록에서 제거

            while queue:       # 8. 큐에 처리할 노드가 남아있는 동안 반복
                curr = queue.popleft() # 9. 큐의 맨 앞에서 노드를 추출 (가장 먼저 들어온 노드)
                visited_order.append(curr) # 10. 추출된 노드를 방문 완료 목록에 추가

                for neighbor in self.e[curr]: # 11. 현재 노드와 연결된 모든 이웃 노드를 검사
                    if neighbor in unvisited: # 12. 이웃 중 아직 방문 예정 목록(unvisited)에 있는 경우
                        queue.append(neighbor) # 13. 해당 이웃을 큐의 맨 뒤에 삽입
                        unvisited.remove(neighbor) # 14. 큐에 삽입되었으므로 중복 방지를 위해 목록에서 제거
        
        return visited_order


###테스트코드
# 1. 그래프 데이터 준비
# 노드: a, b, c, d (서로 연결됨) / e, f (둘이서만 연결됨)
nodes = ['a', 'b', 'c', 'd', 'e', 'f']
edges = [
    ('a', 'b'), ('a', 'c'), 
    ('b', 'd'), ('c', 'd'),
    ('e', 'f')
]

# 2. 그래프 객체 생성
graph = UndirectedGraph(nodes, edges)

# 3. DFS 실행
dfs_result = graph.dfs()
print(f"DFS 방문 순서: {dfs_result}")

# 4. BFS 실행
bfs_result = graph.bfs()
print(f"BFS 방문 순서: {bfs_result}")


class MinHeap:
    def __init__(self):
        self.heap = []
        
    def insert(self, value):
        #add the new value to the end of the heap
        self.heap.append(value)
        #perform heapify-up to maintain the heap property
        self.heapify_up(len(self.heap) - 1)
        
    def heapify_up(self,index):
        #move the element at index up until the heap property is restored
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            #swap if the current node is smaller than its parent
            self.heap[index], self.heap[parent_index] =  self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2
            
    def delete_min(self):
        if len(self.heap) == 0:
            return None
        #replace the root of the heap with the last element
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop() #remove the last element
        #perform heapify-down to maintain the heap property
        self.heapify_down(0)
        return min_value
    
    def heapify_down(self,index):
        #move the element at index down until the heap property is restored
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        #find the smallest of index, left child, and right child
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        
        #if the smallest isnt the paresnt node, swap and continue heapifying
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down[smallest]
            
import heapq


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
        if list[mid] == value:
            return mid
        elif list[mid] < value:
            first = mid + 1
        else:
            last = mid -1
    return -1

"""1. does the binary search work when the list contains duplicates?
    - to make it retrun any of those duplicates?
    - to make it return the leftmost one?
    - to make it return the rightmost one?
2. find the first element greater than or equal to the query"""

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

def binary_search(list, value, first, last): #recursive version
    if first > last :  #base case
        return -1
    
    else : #general case
        mid = (first + last) //2
        if list[mid] ==value:
            return mid
        elif list[mid] < value:
            return binary_search(list, value, mid +1, last)
        else: #list[mid] > value:
            return binary_search(list, value, first, mid - 1)
        
binary_search(list, value, 0, len(list)-1)


# reversing a string
#non-recursive version
def reverse(str):
    output = ""
    for i in range(len(str)):
        output += str[-i-1]
    return output
#recursive version
def reverse(str):
    if not str:
        return str
    else:
        return str[-1] + reverse(str[:-1])


###sorting
##insertion_sort ;; 삽입 정렬  ;; 삽입하려고 정렬시킬것이다
def insertion_sort(list):
    #두 번째 인덱스(1)부터 마지막 인덱스까지(리스트의 길이) 반복할거야
    for i in range(1, len(list)):
        key = list[i] #현재 정렬할 기준 인덱스값을 key에 복사
        j = i-1 #j는 이미 정렬된 sorted region 영역의 인덱스 
        #i가 비교할 인덱스이니까(정렬안된 unsorted region), 비교할 대상은(정렬된 sorted region) i보다 하나 전의 인덱스로

        while j >=0 and key < list[j]: #j가 0보다 작아지거나(맨 앞도달), key보다 작거나 같은 값을 만날 떄까지 반복, 정렬중임을 잊지말자
            list[j+1] = list[j] #작거나 같은값의 인덱스를 만나면 스왑??
                                #더 작으니까 더 작은것을 뒤로 보내고
                                #내 키를 앞에 넣을게
            j -=1 #j = j-1, 더 왼쪽카드와 비교하기위해 j를 하나 줄여??///왜지?
        
        list[j + 1] = key #while문이 멈춘 위치가 key 자리


##selection sort ;;;선택 정렬 ;;가장 작은놈 하나만 골라서 앞으로 보내
def selection_sort(list):
    for i in range(len(list)):
        smallest = i  #현재 자리가 가장 작다고 가정하고, 다음칸부터 끝까지 훑으면서, 진짜 가장 작은것을 찾아내
        for j in range(i+1, len(list)):
            if list[j] < list[smallest]: #만약 더작은게 나타나면
                smallest = j  #그것을 가장 작은것으로 업데이트
        
        list[i], list[smallest] = list[smallest], list[i]   #한 바퀴 다 돌았으면, 원래 i 와 찾아낸 진짜 제일 작은 smallest의 위치를 바꿔(swap)

        

##merge sorting ;; 병합 정렬, 합병 정렬 
def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2 #round down
        left = list[:mid]
        right = list[mid:]
        
        merge_sort(left)
        merge_sort(right)
    
    #todo : merge left & right in the list    
        i = j = k = 0 #셋다 0부터 시작
        
        # left, right 두 리스트를 비교하며 작은 값을 원본 리스트로 덮어쓰기
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else : # len(left) > len(right)
                list[k] = right[j]
                j += 1
            k += 1
            
        #한쪽 리스트가 먼저 끝나면, 남은 값들을 덮어씀
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    
    
def counting_sort(list):
    output = [0]* (len(list)) 
    #원본 리스트를 바로 수정하는게 아니라 정해진 자리에 하나씩 숫자를 옮겨 담을 거야
    
    count = [0]*(max(list)+1) 
    #리스트에 숫자5가 있다면 count배열의 인덱스 5를 찾아가야하니까 '가장큰수 +1' (0부터 시작하기때문)
    
    for i in range(len(list)): # 숫자세기 count! 숫자가 몇번 나왔는지 셈
        count[list[i]] += 1
        
        
    #자리 예약cumulative sum누적합,전체 줄에서 몇번째 칸까지 차지할지를 매기는 과정    
    for i in range(1, len(count)): 
        count[i] += count[i-1] #내 칸의 숫자에 앞칸의 숫자를 계속더해
                                # 0번 동네 사람이 2명이고 1번 동네 사람이 3명이면, 1번 동네 사람은 전체 줄에서 5번자리까지 차지해! 라고 정해주는 것
                                
    #실제 자리에 앉히기 placement                            
    for i in range(len(list)):
        j = len(list) - 1 - i  #원본 리스트를 맨 뒤에서부터 거꾸로 읽어낸다
        count[list[j]] -= 1 ##count[list[j]] = count[list[j]] - 1 을 줄여쓴것
        ##예, 숫자2는 전체 줄에서 4번째자리까지 차지해!--> 4번째 자리면 인덱스로는 3이네?? 0부터 시작하니까! >>그래서 -1 을 함
        index = count[list[j]]  #-1 한 count[list[j]]를 output의 인덱스로 가져간다
        output[index] = list[j] # 그 자리에 list[j]의 값을 넣어
    
    return output