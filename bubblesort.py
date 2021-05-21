# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:36:44 2020

@author: Lenovo
8"""

def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
arr=[64,34,25,12,22,11,90]
bubblesort(arr)
print("The Sorted array is: ",arr)