# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:27:09 2020

@author: Lenovo
"""

arr=[10,15,42,32,56,80,12]
for i in range(0,len(arr)):
    smallest=min(arr[i:])
    min_index=arr.index(smallest)
    arr[i],arr[min_index]=arr[min_index],arr[i]
    
print("Sorted array: ",arr)