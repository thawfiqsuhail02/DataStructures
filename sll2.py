# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:12:25 2020

@author: Lenovo
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        if self.head is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            newnode=Node(data)
            self.last_node.next=newnode
            self.last_node=self.last_node.next
    def display(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
    def search(self,value):
        current=self.head
        index=0
        while self.head is not None:
            if value==current.data:
                return index
            current=current.next
            index=index+1
        return -1
    def delete(self,p):
        if self.head is None:
            return 
        temp=self.head
        if p==0:
            self.head=self.head.next
            temp=None
            return
        for i in range(p-1):
            temp=temp.next
            if temp is None:
                return
        nextnode=temp.next.next
        temp.next=None
        temp.next=nextnode
    def insertion(self,data,pos):
        current=self.head
        previous=current
        currpos=0
        while self.head is not None:
            previous=current
            current=current.next
            currpos=currpos+1
            if currpos==pos:
                newnode=Node(data)
                previous.next=newnode
                newnode.next=current
                break
    def sortList(self):  
        #Node current will point to head  
        current = self.head;  
        index = None;  
          
        if(self.head == None):  
            return;  
        else:  
            while(current != None):  
                #Node index will point to node next to current  
                index = current.next;  
                  
                while(index != None):  
                    #If current node's data is greater than index's node data, swap the data between them  
                    if(current.data > index.data):  
                        temp = current.data;  
                        current.data = index.data;  
                        index.data = temp;  
                    index = index.next;  
                current = current.next;  
    def middle(allist):
        mid=allist.head
        leng=0
        while mid:
            mid=mid.next
            leng=leng+1
        mid=allist.head
        for i in range((leng-1)//2):
            mid=mid.next
        if mid:
            if leng%2==0:
                print("The middle elemnts are: ",mid.data,mid.next.data)
            else:
                print("The middle element is: ",mid.data)
    def max(self):
        current=self.head
        maximum=self.head.data
        while current:
            if maximum<current.data:
                maximum=current.data
            current=current.next
        print("The maximum in the list is ",maximum)
    def min(self):
        current=self.head
        minimum=self.head.data
        while current:
            if minimum>current.data:
                minimum=current.data
            current=current.next
        print("The minimum in the list is ",minimum)
        
allist=LinkedList()
allist.append(10)
allist.append(20)
allist.append(30)
allist.append(40)
allist.append(85)
allist.append(50)
key=allist.search(30)
if key !=-1:
    print("The key is in index:",key)
else:
    print("sorry not found")
allist.insertion(50,4)
allist.display()
allist.sortList()
allist.display()
allist.max()
allist.min()
allist.middle()