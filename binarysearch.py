# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:26:27 2020

@author: Lenovo
"""
def binarysearch(arr,l,h,x):
    if h>=l:
        mid=(h+l)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarysearch(arr,l,mid-1,x)
        elif arr[mid]<x:
            return binarysearch(arr,mid+1,h,x)
        else:
            return -1
            
arr=[10,20,30,40,50,60]
x=10
result=binarysearch(arr,0,len(arr)-1,x)
if result!=-1:
    print("Element is on index ",result)
else:
    print("Element is not present in the array")