gk = lambda i,j:str(i)+','+str(j)
MAX = 1000000

def memoized_matrix_chain(p):
    n = len(p)-1
    m = {}
    for i in range(1, n+1):
        for j in range (i, n+1):
            m[gk(i, j)] = MAX
    return lookup_chain(m, p, 1, n)

def lookup_chain(m, p, i, j):
    if m[gk(i, j)] < MAX:
        return m[gk(i, j)]
    if i == j:
        m[gk(i, j)] = 0
    else:
        for k in range(i, j):
            q = lookup_chain(m, p, i, k) + lookup_chain(m, p, k+1, j) + p[i-1]*p[k]*p[j]
            if q < m[gk(i, j)]:
                m[gk(i, j)] = q
    return m[gk(i, j)]



p = [50,20,1,10,100]


print("minimum number of operations:", memoized_matrix_chain(p))
#Next step: what was the order of the multiplication?
