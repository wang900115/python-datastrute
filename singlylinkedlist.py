#定義節點
class Node:
    def __init__(self,data= None):
        self.data = data
        self.next = None
#定義單向鏈結
class LinkedList:
    def __init__(self):
        self.head = None
    #新增
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    #插入
    def insert(self,data,position):
        new_node = Node(data)
        current = self.head
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            while position>1:
                current = current.next
                position-=1
            next = current.next
            current.next = new_node
            current.next.next = next
            new_node = next
    #反轉
    def reverse(self):
        pre = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        self.head = pre
        print()
    #刪除
    def delet(self,position):
        if position == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(position-1):
                curr = curr.next
            curr.next = curr.next.next
    #打印
    def display(self):
        current = self.head
        while current:
            print(current.data,end= '->')
            current = current.next
        if current==None:
            print('None')

if __name__ == '__main__':
    linklist = LinkedList()
    linklist.append(1)
    linklist.append(2)
    linklist.append(3)
    linklist.append(4)
    linklist.insert(5,1)
    linklist.delet(1)
    linklist.reverse()
    linklist.display()




