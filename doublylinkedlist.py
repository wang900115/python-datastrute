#定義節點
class Node:
    def __init__(self,data = None):
        self.data = data
        self.prev = None
        self.next = None
#定義雙向鏈結
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    #新增
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev= current
    #插入
    def insert(self,data,position):
        new_node = Node(data)
        current = self.head
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node

        else:
            while position>1 and current.next:
                current = current.next
                position-=1
            if current.next:
                new_node.next = current.next
                current.next.prev = new_node
            current.next =new_node
            new_node.prev = current
    #反轉
    def reverse(self):

        tmp = None
        curr = self.head

        while curr:
            tmp = curr.prev
            curr.prev = curr.next
            curr.next = tmp
            curr = curr.prev
        if tmp:
            self.head = tmp.prev


    #打印
    def display(self):
        current = self.head
        while current:
            print(current.data,end = '->')
            current = current.next
        print('None')
    #打印反轉
    def display_reverse(self):
        current = self.head
        while current.next:
            current = current.next

        while current:
            print(current.data,end='<-')
            current = current.prev
        print('None')
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.insert(4,0)
print('左至右:')
dll.display()
print('右至左:')
dll.reverse()
dll.display()
dll.display_reverse()

