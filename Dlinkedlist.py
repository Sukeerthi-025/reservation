class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.prev=None

class Dlinkedlist:
    def __init__(self):
        self.head=None

    def listprint(self):
        ptr=self.head
        if (ptr is None):
            print("Empty list")
        while ptr is not None:
            print(ptr.data,end="<-->")
            ptr=ptr.next
        print()

    def search(self,key):
        ptr=self.head
        while ((ptr is not None) and (ptr.data != key)):
            ptr=ptr.next
        if (ptr is None):
            print("Key not found")
        else:
            print("Key found")

    def insert(self,value):
        new_node=Node(value)
        if (self.head==None):
            list.head=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node

    def delete(self):
        if (self.head==None):
            print("Empty List")
        else:
            print("Node value deleted is",self.head.data)
            self.head=self.head.next
            self.head.prev=None

list=Dlinkedlist()
n=int(input("how many node you want : "))
for i in range(n):
    value=int(input("Enter the node value : "))
    list.insert(value)
list.listprint()    

print("\nDemonstrating search,Insert and delete operation")
key=int(input("Enter the value to search : "))
list.search(key)
print("\nInserting Node value at the beginning")
value=int(input("Enter the value to insert : "))
list.insert(value)
print("\nList after inserting Node")
list.listprint()
print("\nDeleting Node")
list.delete()
print("\nList after deleting first node : ")
list.listprint()
print("------END------")
