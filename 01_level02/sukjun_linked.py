### 연결 리스트

# 배열 : 메모리가 연속적이며, 추가 및 수정에 오버헤드(컴퓨터가 힘들어해요)가 발생한다.
# 연결 리스트 : 메모리 주소는 상관 없이, 서로가 서로를 가르켜 연결하는 방식, 수정 및 추가, 삭제 등이 매우 간단하고 편리하다.



# 챌린지 1.

# 아래는 제가 구현한 연결리스트 클래스 입니다.
# 한줄 한줄 주석을 달아서 이게 뭔지, 어떤 동작인지 설명해보세요.

class LinkedList: # LinkedList 클래스
    def __init__(self): # 생성자 메서드
        self.head = None # 머리는 None이다
        self.nodes = [] # 리스트 생성

    class Node: # 노드 클래스
        def __init__(self, data): # 생성자 메서드
            self.data = data # 노드에 들어갈 데이터지정
            self.prev = None # 이전노드를 가리키는 포인터
            self.next = None # 다음노드를 가리키는 포인터  

        def __str__(self): # 객체를 문자열로 변환하는 메서드
            return f"{self.data}" # 노드의 데이터를 반환

    def push_back(self, data): # 매개변수 설정?
        new_node = self.Node(data)  # 뉴노드에 노드의 데이터를 넣는다
        if not self.head: # 머리가 아니면
            self.head = new_node  # self.head는 new_node가 된다
            prevNode = None # prev노드는 None이다
        else: # 머리가 맞으면
            self.nodes[-1].next = new_node 
            prevNode = self.nodes[-1]
        self.nodes.append(new_node)  
        self.nodes[-1].prev = prevNode
    
    def insert(self,find_data,insert_data):
        new_node = self.Node(insert_data)
        isFind = False
        for node in self.nodes:
            if node.data == find_data:
                curNode = node
                isFind = True
                break
        if isFind == False: return    

        if curNode.prev != None: # 만약 curNode.prev가 None이 아니라면
            new_node.prev = curNode.prev # new_node.prev가 curNode.prev로 바뀜
            curNode.prev.next = new_node # curNode.prev.next가 new_node가 됨
            curNode.prev = new_node
            new_node.next = curNode
        else : 
            self.head = new_node
            new_node.prev = None
            new_node.next = curNode
            curNode.prev = new_node

    def delete(self,del_data):
        for node in self.nodes:
            if node.data == del_data:
                delData = node
                break
        if self.head == delData:
            self.head = delData.next
        elif delData.next == None:
            delData.prev.next = None
        else:
            delData.prev.next = delData.next
            delData.next.prev = delData.prev
        del(delData)

    def find(self,find_data):
        findNode = None
        for node in self.nodes:
            if node.data == find_data:
                findNode = node
                break
        return findNode 
        
    def print_list(self,reverse = False):
        current = self.head
        if reverse == False:
            print('정방향 출력 : ', end = '')
            while current:
                print(current, end=" -> ")
                current = current.next
            print("None")
        else :
            print('역방향 출력 : ', end = '')
            while True:
                if current.next != None:
                    current = current.next
                else: break
            while True:
                print(current, end = ' --> ')
                current = current.prev
                if current == None:
                    break
            print("None")

    

list1 = LinkedList()
list1.push_back('김씨')
list1.push_back('왕씨')
list1.push_back('철씨')
list1.print_list(True)
list1.insert('왕씨','옹씨')
list1.print_list()

list2 = LinkedList()
list2.push_back('굼씨')
list2.push_back('진씨')
list2.print_list()
list2.insert('굼씨','주씨')
list2.print_list()