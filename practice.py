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
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length +=1
    def prepend(self,value):
        new_node= Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    def remove_duplicates(self):
        temp = self.head
        while temp:
            temp2 = temp
            while temp2.next:
                if temp2.next.value == temp.value:  
                    temp2.next = temp2.next.next
                else:
                    temp2 = temp2.next
            temp = temp.next

    def __str__(self):
        temp_node= self.head
        result =' '
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result

new_linked_list= LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.prepend(10)
new_linked_list.prepend(20)
new_linked_list.remove_duplicates()
print(new_linked_list)
        