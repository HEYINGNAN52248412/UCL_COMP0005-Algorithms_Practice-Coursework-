id=list(range(10))

def root (i):
    while id[i] != i:
        i = id[i]
    return i

def find (u,v):
    u_root = root(u)
    v_root = root(v)

    return u_root == v_root

def union (u,v):
    u_root = root(u)
    v_root = root(v)

    id[u_root] = v_root

#max depth: N(array)

