# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 12:17:01 2020

@author: Lenovo
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
        self.tail=None
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            Newnode=Node(data)
            Newnode.next=self.head
            self.head=Newnode
    def pop(self):
        if self.head is None:
            return
        else:
            temp=self.head
            self.head=temp.next
            temp=None
    def display(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
    
    def reverse(self): 
        current, temp, prev = self.head, None, None
        while current != None: 
            temp = current.next
            current.next = prev 
            prev = current 
            current = temp 
              
        self.top = prev 
      
    def isEmpty(self): 
        return self.top == None
            
s=Stack()
dest=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.pop()
s.display()
s.reverse()

# Pop the values from source and push into destination stack 
while s.isEmpty() != True: 
    dest.push(s.pop())
    
print("Destination Stack:") 
dest.display() 