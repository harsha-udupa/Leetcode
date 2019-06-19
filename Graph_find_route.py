

graph={1:[2,3,4],2:[1,4,6],3:[1,5,6,7],4:[1,2],5:[3,6],6:[2,3,5],7:[8,3]}

visited=[]
source=2
dest=7
queue=[source]
while queue:
    cur=queue.pop(0)
    if cur==dest:
        print "True"
        exit()
    if cur not in visited:
        visited.append(cur)

    for i in graph[cur]:
        if i not in visited:
            queue.append(i)

print "False"
