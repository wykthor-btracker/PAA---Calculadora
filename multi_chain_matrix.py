def f(i,j):
    return (str(i)+","+str(j))

def matrix_chain_order(p): #a entrada p é caracterizada como o exemplo: matrizes 50x20, 20x1, 1x10, 10x100= (50, 20, 1, 10, 100)
    n = len(p)-1 # numero de matrizes a serem multiplicadas
    m, s = {}, {} # m[i,j] guardará o menor numero de operacoes para se multiplicar as matrizes de i a j;
    for i in range(1, n+1):
        m[f(i, i)] = 0 #salva em m[i,i] o numero de operacoes com uma unica matriz = 0
    for l in range(2, n+1): # inicia com cadeia de duas matrizes: l=2 e vai aumentando
        for i in range(1, n-l+2):
            j = i+l-1
            m[f(i, j)] = 100000000 
            for k in range(i, j): # obtencao de m[i,j] 
                q = m[f(i, k)]+m[f(k+1, j)]+p[i-1]*p[k]*p[j] #aqui entra programacao dinamica, pois varios valores da arvore de recursao ja foram calculados e sao trazidos de m
                if q<m[f(i, j)]:
                    m[f(i, j)] = q #obtencao de m otimo para multiplicacao da cadeia de matrizes de i a j
                    s[f(i, j)] = k #onde ocorreu a divisao otima da cadeia de matrizes de i a j
    return m, s

def get_optimal_order(s, i, j): 
    res = ""
    if i == j:
        return ("A"+str(j))
    else:
        res += "("
        res += get_optimal_order(s, i, s[f(i, j)])
        res += get_optimal_order(s, s[f(i, j)]+1, j)
        res +=  ")"
        return res



p = [50,20,1,10,100]
m, s = matrix_chain_order(p)
print ("number operations：", m[f(1, len(p)-1)])
print ("best order of matrix multiplication:", get_optimal_order(s, 1, len(p)-1))
