# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:21:51 2020

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
        
    def append(self,data):
        if self.head is None:
            NewNode=Node(data)
            self.head=NewNode
            self.last_node=self.head
        else:
            NewNode=Node(data)
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
            self.last_node.next=self.head
            
    def display(self):
         current=self.head
         while current is not None:
             print(current.data,end=" ")
             current=current.next
             if current==self.head:
                 break
    
    def find_index(self,key):
        current=self.head
        index=0
        while current:
            if current.data==key:
                return index
            current=current.next
            index=index+1
            
        return -1
    def deletenode(self,position):
        if self.head is None:
            return
        temp=self.head
        if position==0:
            self.head=temp.next
            
    
allist=LinkedList()
n=int(input("How many elements u would like to add"))
for i in range(n):
    data=int(input("Enter the data values"))
    allist.append(data)
allist.display()
key=int(input("Enter the key u want to search for: "))
index=allist.find_index(key)
if index==-1:
    print(str(key) + 'was not found')
else:
    print(str(key) + " is at index "+str(index))