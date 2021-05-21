class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        currentNode = self.head
        while currentNode is not None:
           print(currentNode.data, end = ' ')
           currentNode = currentNode.next
    
 
                    
    def insert1(self,data,position):
        
        if(position==0):
            newNode=Node(data)   
            nnode=self.head
            self.head=newNode
            newNode.next=nnode
        else:    
            currentNode=self.head
#            previousNode=currentNode
            newNode=Node(data)                  
            curr_pos=0
            while True: 
               previousNode=currentNode
               currentNode=currentNode.next
               curr_pos+=1
               if(curr_pos==position):
                  newNode.next=currentNode
                  previousNode.next=newNode
                 
                  break
                  
              
               
            
a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
print('The linked list: ', end = '')
a_llist.display()
print("")


data1 = int(input('Enter data item: '))
pos = int(input('Enter pos: '))
a_llist.insert1(data1,pos)
a_llist.display()
