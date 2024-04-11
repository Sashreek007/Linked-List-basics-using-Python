class Node:
    def __init__(self,value):
        self.value= value
        self.next= None
 
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail= new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail= new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length +=1
    
    def traversal(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    
    def serching(self,target):
        current= self.head
        index= 0
        while current is not None:
            if current.value == target:
                return True,index+1
            current= current.next
            index+=1
        return False
    def get2(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def get1(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.value
            current = current.next
            count += 1
        return None
    def set_value(self,index,value):
        current= self.head
        new_node =Node(value)
        for _ in range(index):
            current = current.next
        current.value =new_node.value 

    def set2(self, index, value):
        current = self.get2(index)
        if current:
            current.value = value
            return True
        return False

    def __str__(self):
        temp_node=self.head
        result=' '
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node= temp_node.next
        return result



   
        
        
new_linked_list =LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.prepend(40)
new_linked_list.prepend(50)
new_linked_list.prepend(60)
new_linked_list.traversal()
new_linked_list.set2(1,2)
new_linked_list.set_value(0,9)
print(new_linked_list.serching(60))
print(new_linked_list.get2(5))
print(new_linked_list.get1(5))
print(new_linked_list)