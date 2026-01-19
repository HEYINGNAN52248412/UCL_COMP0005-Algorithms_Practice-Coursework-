id = list(range(10))
size = [1]*10
no_union=10
max_element=list(range(10))

def root (i):
    while id[i] != i:
        id[i] = id[id[i]]
        i = id[i]
    return i

def find (u,v):
    u_root = root(u)
    v_root = root(v)

    return u_root == v_root

def union (u,v):
    global no_union

    u_root = root(u)
    v_root = root(v)

    if u_root == v_root:
        return

    if size[u_root] > size[v_root]:
        id[v_root] = u_root
        max_element[u_root] = max(max_element[u_root], max_element[v_root])
        size[u_root]+=size[v_root]
    else:
        id[u_root] = v_root
        max_element[v_root] = max(max_element[u_root], max_element[v_root])
        size[v_root]+=size[u_root]
    
    no_union-=1

def find_max_element(i):
    return max_element[root(i)]


def find_earliest_connectivity(log_file):
    for timestamp, u, v in log_file:
        union(u, v)
        if no_union == 1:
            return timestamp
            
    return "Not all connected"

#O