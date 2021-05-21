# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 13:14:26 2020

@author: Lenovo
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
class stack:
    def __init__(self):
        self.head=None
        self.tail=None
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def display(self):
            current=self.head
            while self.head is not None:
                print(current.data,end=" ")
                current=current.next
    def pop(self):
        if self.head is None:
            print("Stack Underflow")
        else:
            popnode=self.head
            self.head=self.head.next
            popnode=None
            
s=stack()
choice=int(input("select 1 to push and 2 to pop"))
if choice==1:
    element=int(input("Enter the no of elements"))
    for i in range(element):
        data=int(input("Enter the data elements"))
        s.push(data)
        break
else:
    s.pop()
        
s.display()         
            
            
            
            
            
            
            
            