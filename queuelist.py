# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 10:31:33 2020

@author: Lenovo
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
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
           self.rear=self.rear.next
        
    def Dequeue(self):
        if self.front is None:
            return
        temp=self.front
        self.front=temp.next
        temp=None
            
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
q.Dequeue()
c=q.transversal()
