graph ={
        
        'A':['B','C','G'],
        'B':['A','C','D'],
        'C':['A','B','D','E'],
        'D':['B','C','F'],
        'E':['C','F','G'],
        'F':['D','E'],
        'G':['A','E']
        
        }
    
def f(graph,node):
    invite = graph[node]+[]
    for i in graph [node]: 
        for theirfriends in graph[i]:
            if theirfriends not in invite:
                invite.append(theirfriends)
    print(invite)
f(graph,'A')  

 