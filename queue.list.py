# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:49:10 2020

@author: Lenovo
"""
class LinkedList:
    def __init__(self):
        self.front=None
        self.rear=None
        
    def Enqueue(self,data):
        NewNode=Node(data)
        if self.rear is None:
            self.front=NewNode
            self.rear=self.front
        else:
           self.rear.next=NewNode
           self.rear=NewNode
        
    def Dequeue(self):
        if self.front is None:
            return
        temp=self.front
        self.front=temp.next
            
    def transversal(self):
        current=self.front
        while current is not None:
            print(current.data)
            current=current.next
    
    def copylist(self,c):
        list2=c[:]
        return list2

q=LinkedList()    
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Dequeue()
c=q.transversal()
print(q.copylist(c))
S
