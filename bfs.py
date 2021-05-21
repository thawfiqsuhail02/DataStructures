# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:27:42 2020

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
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s,end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited,graph,"A")