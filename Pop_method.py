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
    
    def pop_first(self):
        value = self.head
        if self.length==1:
            self.head= None
            self.tail=None
        elif self.head is None:
            return None
        else:
            self.head=self.head.next
            value.next= None
        self.length-=1
        return value.value

    def pop_method(self):
        popout=self.tail
        temp_node=self.head
        if self.length==1:
            self.head= None
            self.tail=None
        elif self.head is None:
            return None
        else:
            while temp_node.next is not self.tail:
                temp_node= temp_node.next
            self.tail= temp_node
            temp_node.next= None
        self.length-=1
        return popout.value
    def remove(self,index):
        prev= self.head
        popped= self.head
        if index == 0:
            return self.pop_first()
        elif index == -1 or self.length-1:
            return self.pop_method()
        elif index >= self.length:
            return None
        else:
            for _ in range(index):
                popped=popped.next
            prev.next = popped.next
            popped.next=None
            self.length -= 1
        return popped.value
    def remove2(self,index):
        popped_node=self.head
        prev=self.head
        if index==0:
            popped_node = self.head
            self.head=self.head.next
            popped_node.next= None
        elif index== self.length-1 or -1:
            popped_node=self.tail
            temp_node=self.head
            while temp_node.next is not self.tail:
                temp_node= temp_node.next
            self.tail= temp_node
            temp_node.next= None
        else:
            popped_node=self.head
            prev=None
            for _ in range(index):
                prev=popped_node
                popped_node=popped_node.next
            prev.next=popped_node.next
            popped_node.next=None
        self.length-=1
        return popped_node.value
    def delete_All(self):
        self.head = None
        self.tail= None 
        self.length= 0

    def reverse(self):
        current=self.head
        prev= None
        while current is not None:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head,self.tail=self.tail,self.head
    
    def middle(self):
        temp_node = self.head
        middle_index = self.length // 2  
        for _ in range(middle_index):
            temp_node = temp_node.next
        return temp_node.value
    
    def remove_duplicates(self):
        temp = self.head
        while temp:
            temp2 = temp
            while temp2.next:
                if temp2.next.data == temp.value:  
                    temp2.next = temp2.next.next
                else:
                    temp2 = temp2.next
            temp = temp.next

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
new_linked_list.append(10)
new_linked_list.prepend(40)
new_linked_list.prepend(0)
new_linked_list.prepend(60)
print(new_linked_list.middle())
print(new_linked_list)
new_linked_list.traversal()
new_linked_list.set2(1,2)
new_linked_list.reverse()
print(new_linked_list)
new_linked_list.set_value(0,9)
print(new_linked_list.pop_first())
print(new_linked_list.serching(60))
print(new_linked_list.get2(5))
print(new_linked_list.get1(5))
print(new_linked_list.pop_first())
print(new_linked_list.pop_method())
print(new_linked_list.remove(-1))
print(new_linked_list)
print(new_linked_list.remove2(1))
print(new_linked_list.length)
print(new_linked_list)

