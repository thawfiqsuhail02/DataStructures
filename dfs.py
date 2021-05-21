# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:08:17 2020

@author: Lenovo
"""
graph={
       "A":["B","C"],
       "B":["A","D","E"],
       "C":["F"],
       "D":[],
       "E":["F"],
       "F":[]
}

visited=[]

def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)


dfs(visited,graph,'A')