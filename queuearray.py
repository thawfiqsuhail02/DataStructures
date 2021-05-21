# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:52:13 2020

@author: Lenovo
"""
from collections import deque
queue=deque(["Ram","KaNan","Akbar","Birbal"])
print(queue)
queue.append("Lohith")
queue.popleft()
print(queue)