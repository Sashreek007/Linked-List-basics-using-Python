class Node:
    def __init__(self,value):
        self.value = value
        self.next= None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        new_node= Node(value)
        if self.head is None:
            self.head=new_node
            self.tail = new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    def prepend(self,value):
        new_node= Node(value)
        if self.head is None:
            self.head=new_node
            self.tail = new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    def insert(self,index,value):
        new_node= Node(value)
        temp_node=self.head
        if index == 0:
            new_node.next=self.head
            self.head=new_node
        elif self.head is None:
            self.head=new_node
            self.tail = new_node
        elif index<0 or index>self.length:
            return False
        else:
            for _ in range(index-1):
                temp_node= temp_node.next
            new_node.next= temp_node.next
            temp_node.next = new_node
    def __str__(self):
        temp_node=self.head
        result= ' '
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node=temp_node.next
        return result
new_linked_list= LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.prepend(0)
new_linked_list.prepend(40)
new_linked_list.prepend(50)
new_linked_list.insert(1,1)
print(new_linked_list)
