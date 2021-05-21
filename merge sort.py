# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:31:57 2020

@author: Lenovo
"""

def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        mergesort(L)
        mergesort(R)
        
        i=j=k=0
        
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i=i+1
            else:
                arr[k]=R[j]
                j=j+1
            k=k+1
            
        while i<len(L):
            arr[k]=L[i]
            i=i+1
            k=k+1
        while j<len(R):
            arr[k]=R[j]
            j=j+1
            k=k+1
    
    
arr=[5,2,4,7,1,3,2,6]
print("THe given array is: ",arr)
mergesort(arr)
print("THe array after sorting is: ",arr)