#### Doubly linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
#creating a linked list
class dLinkedList:
    def __init__(self):
        self.headval=None
    def insert(self,data):
        if self.headval is None:
            new_node=Node(data)
            self.headval=new_node
        else:
            print("List is not empty")
   #Inserting the item at the beginning of the list
    def insert_beginning(self, data):
        if self.headval is None:
            new_node=Node(data)
            self.headval= new_node
            print("Node inserted")
            return
        new_node=Node(data)
        new_node.next=self.headval
        self.headval.prev=new_node
        self.headval=new_node
    #Inserting the item at the end of the list
    def insert_end(self,data):
        if self.headval is None:
            new_node=Node(data)
            self.headval=new_node
            return 
        n=self.headval
        while n.next is not None:
            n=n.next
        new_node= Node(data)
        n.next=new_node
        new_node.prev=n
    #Insert the element after the item in the list
    def insert_after(self, x, data):
        if self.headval is None:
            print("Empty List")
            return
        else:
            n=self.headval
            while n is not None:
                if n.data==x:
                    break
                n=n.next
            if n is None:
                print("Data is not present in list")
            else:
                new_node=Node(data)
                new_node.prev=n
                new_node.next=n.next
                if n.next is not None:
                    n.next.prev=new_node
                n.next=new_node
    #insert the element before the item in the list
    def insert_before(self,x,data):
        if self.headval is None:
            print("Empty List")
            return 
        else:
            n=self.headval
            while n is not None:
                if n.data==x:
                    break
                n=n.next
            if n is None:
                print("Item found")
            else:
                new_node=Node(data)
                new_node.next=n
                new_node.prev=n.prev
                if n.prev is not None:
                    n.prev.next=new_node
                n.prev=new_node
    #to traverse the list
    def traverse(self):
        if self.headval is None:
            print("Empty List")
            return
        else:
            n=self.headval
            while n is not None:
                print(n.data,"")
                n=n.next
    #to delete the item at the start 
    def delete_start(self):
        if self.headval is None:
            print("Empty list")
            return 
        if self.headval.next is None:
            self.headval =None
            return 
        self.headval=self.headval.next
        self.headval.prev=None
    #to delete the item at the end of the list
    def delete_end(self):
        if self.headval is None:
            print("Empty List")
            return
        if self.headval.next is None:
            self.headval= None
            return
        n=self.headval
        while n.next is not None:
            n=n.next
        n.prev.next=None
    #to delete an item
    def delete_item(self, x):
        if self.headval is None:
            print("Empty list")
            return 
        if self.headval.next is None:
            if self.headval.data==x:
                self.headval=None
            else:
                print("Item not present")
            return 
        if self.headval.data==x:
            self.headval=self.headval.next
            self.headval.prev=None
            return
        n=self.headval
        while n.next is not None:
            if n.data==x:
                break
            n=n.next
        if n.next is not None:
            n.prev.next=n.next
            n.next.prev=n.prev
        else:
            if n.data==x:
                n.prev.next=None
            else:
                print("Item not present")
    #TO reverse the list
    def reverse(self):
        if self.headval is None:
            print("Empty List")
            return
        p=self.headval
        q=p.next
        p.next=None
        p.prev=q
        while q is not None:
            q.prev=q.next
            q.next=p
            p=q
            q=q.prev
        self.headval=p
