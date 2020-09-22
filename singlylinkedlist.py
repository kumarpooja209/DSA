##Single Linked list

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
#Creating linked list
class LinkedList:
    def __init__(self):
        self.headval=None
    #to traverse the list
    def traverse(self):
        if self.headval is None:
            print("List is Empty")
            return 
        else:
            n = self.headval
            while n is not None:
                print(n.data, "")
                n= n.next
    #to insert the item at the beginning
    def insert_beginning(self, data):
        new_node= Node(data)
        new_node.next= self.headval 
        self.headval=new_node
    #to insert the item at the end
    def insert_end(self, data):
        new_node=Node(data)
        if self.headval is None:
            self.headval=new_node
            return
        n=self.headval
        while n.next is not None:
            n=n.next
        n.next= new_node
    #to insert the element after the item 
    def insert_item_after(self, x, data):
        n=self.headval
        print(n.next)
        while n is not None:
            if n.data==x:
                break
            n=n.next
        if  n is None:
            print("Item not present in the list")
        else:
            new_node=Node(data)
            new_node.next= n.next
            n.next=new_node
     #to insert the element before the item 
    def insert_item_before(self, x , data):
        if self.headval is None:
            print("List is empty")
            return 
        if x==self.headval.data:
            new_node=Node(data)
            new_node.next=self.headval
            self.headval=new_node
            return 
        n=self.headval
        print(n.next)
        while n.next is not None:
            if n.next.data==x:
                break
            n=n.next
        if n.next is None:
            print("item is not in list")
        else:
            new_node=Node(data)
            new_node.next=n.next
            n.next=new_node
    #to insert the item at particular index
    def insert_index(self, index, data):
        if index==1:
            new_node=Node(data)
            new_node.next= self.headval
            self.headval=new_node
        i=1
        n=self.headval
        while i<index-1 and n is not None:
            n=n.next
            i=i+1
        if n is None:
            print("Index out of bound")
        else:
            new_node=Node(data)
            new_node.next=n.next
            n.next=new_node
    #to count number of element in the list
    def count(self):
        if self.headval is None:
            return 0
        n=self.headval
        count=0
        while n is not None:
            count=count+1
            n=n.next
        return count
    #to search an element in the list
    def search(self, x):
        if self.headval is None:
            print("List is empty")
            return
        n=self.headval
        while n is not None:
            if n.data==x:
                print("Found")
                return True
            n=n.next
        print("Not found")
        return False
    # to create the list with particular item 
    def createlist(self):
        nums=int(input("How many nodes"))
        if nums==0:
            return 
        for i in range(nums):
            value=int(input("Enter the value"))
            self.insert_end(value)
    #to delete the item at the beginning
    def delete_beginning(self):
        if self.headval is None:
            print("List is Empty")
            return 
        self.headval=self.headval.next
    #to delete the item at the end
    def delete_end(self):
        if self.headval is None:
            print("List is empty")
            return
        n=self.headval
        while n.next.next is not None:
            n=n.next
        n.next=None
    #to delete the particular item 
    def delete_item(self, x):
        if self.headval is None:
            print("List is Empty")
            return
        if self.headval.data==x:
            self.headval=self.headval.next
            return
        n=self.headval
        while n.next is not None:
            if n.next.data==x:
                break
            n=n.next
        if n.next is None:
            print("Item not present in list")
        else:
            n.next=n.next.next
    #to reverse the list
    def reverse_list(self):
        prev=None
        n=self.headval
        while n is not None:
            next=n.next
            n.next=prev
            prev=n
            n=next
        self.headval=prev
linklist=LinkedList()
