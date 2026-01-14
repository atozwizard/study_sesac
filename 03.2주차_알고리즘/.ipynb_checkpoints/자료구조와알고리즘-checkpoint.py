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
    