id=list(range(10))
def find(u,v):
    return id[u]==id[v]

def union(u,v):
    uid=id[u]
    vid=id[v]
    for i in range (len(id)):
        if id[i] == uid:
            id[i]=vid


