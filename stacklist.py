# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:29:53 2020

@author: Lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:59:41 2020

@author: Lenovo
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None
        
    def push(self,data):
        if self.head is None:
            NewNode=Node(data)
            self.head=NewNode
        else:
            NewNode=Node(data)
            NewNode.next=self.head
            self.head=NewNode
            
    def display(self):
        current=self.head
        if self.head is None:
             print("Stack Underflow")
        else:
             while current is not None:
                 print(current.data)
                 current=current.next
            
    def pop(self):
            popnode=self.head
            self.head=self.head.next
            popnode=None
    
allist=LinkedList()
allist.push(2)
allist.push(5)
allist.push(10)
allist.display()
allist.pop()
allist.display()