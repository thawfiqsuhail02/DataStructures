# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 08:44:27 2020

@author: Lenovo
"""

class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class BinarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self,val):
        if self.root is None:
            self.root=Node(val)
        else:
            current=self.root
            while True:
                if current.data>=val:
                    if current.left is None:
                        current.left=Node(val)
                        break
                    else:
                        current=current.left
                else:
                    if current.right is None:
                        current.right=Node(val)
                        break
                    else:
                        current=current.right
                        
    def inorder(self,node):
        if node==None:
            return
        else:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)
    def preorder(self,node):
        if node==None:
            return
        else:
            print(node.data,end=" ")
            self.inorder(node.left)
            self.inorder(node.right)
    def postorder(self,node):
        if node==None:
            return
        else:
            self.inorder(node.left)
            self.inorder(node.right)
            print(node.data,end=" ")
            
    def search(self,root,key):
       if root==None:
           return False
       if root.data==key:
           return True
       if root.data<key:
           return self.search(root.right,key)
       else:
           return self.search(root.left,key)
tree=BinarySearchTree()
tree.insert(2)
tree.insert(6)
tree.insert(4)
tree.insert(2)
tree.insert(1)
print("Inorder Printing: ")
tree.inorder(tree.root)
print("Preorder Printing: ",end=" ")
tree.preorder(tree.root)
print("Postorder Printing: ",end=" ")
tree.postorder(tree.root)
print("Searching the key: ")
if tree.search(tree.root,4) is not None:
    print("Found")
else:
    print("Not Found")