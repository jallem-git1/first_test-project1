# 싱글 링크드 리스트


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)


# 링크드 리스트 생성
my_list = LinkedList()

# 데이터 추가
my_list.append(1)
if my_list.is_empty() :
    print(my_list.is_empty())
else:
    print("Not empty")

my_list.display() 
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

# 데이터 출력
my_list.display()  # 출력: [1, 2, 3, 4, 5]

# 데이터 검색
print(my_list.search(2))  # 출력: True
print(my_list.search(6))  # 출력: False

# 데이터 삭제
my_list.delete(2)
my_list.display()  # 출력: [1, 3]






