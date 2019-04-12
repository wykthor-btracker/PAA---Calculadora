from functools import reduce


class BigNumber:
    def __init__(self, num):
        self.num = num
        self.tam = len(num)
        assert (isinstance(num, str))
        try:
            float(num)
        except ValueError as e:
            raise Exception("Valor inválido recebido! {} tem caracteres não esperados. Apenas números ou . esperados.\n"
                            "Erro:{}".format(num, e))
        except Exception as e:
            raise Exception("Exceção inesperada: {}".format(e))

    def __int__(self):
        return int(self.num)

    def __str__(self):
        return self.num

    def __repr__(self):
        return "BigNumber({})".format(self.num)

    def __len__(self):
        return len(self.num)

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise Exception("Adição mal feita, esperava um objeto do tipo {}, tipo {} recebido".format(BigNumber,
                                                                                                       type(other)))
        res = self.performAddition(other)
        return BigNumber(res)

    def __mul__(self, other):

        """Multiplica um BigNumber pelo outro"""

        return BigNumber(str(self.recursiveMult(self,other)))

    def performAddition(self, other):
        maior = lambda values: reduce(lambda bigNumA, bigNumB: bigNumA if len(bigNumA) >= len(bigNumB) else bigNumB,
                                      values)
        menor = lambda values: reduce(lambda bigNumA, bigNumB: bigNumA if len(bigNumA) < len(bigNumB) else bigNumB,
                                      values)
        indexTuples, longestNumber, shortestNumber = self._initSum(maior, menor, other)
        res = self._SumSubsets(indexTuples, longestNumber, shortestNumber)
        end = self._JoinSumWithLeftover(longestNumber, res)
        return end

    @staticmethod
    def _JoinSumWithLeftover(longestNumber, res):
        leftover = longestNumber[:-len(res)]
        result = "".join(map(lambda x: str(x), res))
        end = leftover + result
        return end

    @staticmethod
    def _SumSubsets(indexTuples, longestNumber, shortestNumber):
        carry = 0
        res = []
        for indexA, indexB in indexTuples:
            unitSum = int(longestNumber[indexA]) + int(shortestNumber[indexB])
            if carry:
                unitSum += carry
                carry = 0
            if unitSum > 9:
                unitSum = unitSum % 10
                carry = 1
            res.insert(0, unitSum)
        return res

    def _initSum(self, maior, menor, other):
        cutOff = min(len(self.num), len(other.num))
        longestNumber = maior([self.num, other.num])
        shortestNumber = menor([self.num, other.num])
        indexListLargest = list(reversed(range(len(longestNumber))))[:cutOff]
        indexListSmallest = list(reversed(range(cutOff)))
        indexTuples = [(indexListLargest[index], indexListSmallest[index]) for index in range(cutOff)]
        return indexTuples, longestNumber, shortestNumber

    def __eq__(self,other):
        return self.num == other.num

    def __lt__(self, other):
        if len(self) < len(other):
            return True
        elif len(self) == len(other):
            if self == other:
                return False
            else:
                for index in range(len(self)):
                    if self.num[index] < other.num[index]:
                        return True
                    elif self.num[index] > other.num[index]:
                        return False

    @staticmethod
    def _zeroPad(numberString, zeros, left=True):

        """Return the string with zeros added to the left or right."""

        for i in range(zeros):

            if left:

                numberString = '0' + numberString

            else:

                numberString = numberString + '0'

        return numberString

    def recursiveMult(self, x, y):
        x, y = str(x), str(y)
        # base case for recursion
        if len(x) == 1 and len(y) == 1:
            return int(x) * int(y)

        if len(x) < len(y):

            x = self._zeroPad(x, len(y) - len(x))

        elif len(y) < len(x):

            y = self._zeroPad(y, len(x) - len(y))
        n = len(x)
        j = n // 2
        # for odd digit integers
        if (n % 2) != 0:
            j += 1
        BZeroPadding = n - j
        AZeroPadding = BZeroPadding * 2
        a = int(x[:j])
        b = int(x[j:])
        c = int(y[:j])
        d = int(y[j:])
        # recursively calculate
        ac = self.recursiveMult(a, c)
        bd = self.recursiveMult(b, d)
        k = self.recursiveMult(a + b, c + d)
        A = int(self._zeroPad(str(ac), AZeroPadding, False))
        B = int(self._zeroPad(str(k - ac - bd), BZeroPadding, False))
        return A + B + bd
    
def root(x, n): 

    x = float(x) 
    n = int(n) 
    if (x >= 0 and x <= 1): 
        menor = x 
        maior = 1
    else: 
        menor = 1
        maior = x         
    e = 0.00000001 
    chute = (menor + maior) / 2
    while abs(chute ** n - x) >= e: 
        if chute ** n > x: 
            maior = chute 
        else: 
            menor = chute
        chute = (menor + maior) / 2
    return round(chute, 2)

def exp(x, n):
    if n == 1:
        return x;
    if n % 2 == 0:
        return exp(x * x, n // 2)
    return x * exp(x * x, n // 2)

def check(str1, str2): 
  
    n1 = len(str1)  
    n2 = len(str2) 
   
    if (n1 < n2): 
        return True
    if (n2 < n1): 
        return False
   
    for i in range(n1): 
        if (str1[i] < str2[i]): 
            return True
        elif (str1[i] > str2[i]): 
            return False
   
    return False

def subt(str1, str2): 
  

    if (check(str1, str2)): 
        aux = str1 
        str1 = str2 
        str2 = aux 
   
   
    str3 = "" 
   
    n1 = len(str1)  
    n2 = len(str2) 
   
 
    str1= str1[::-1] 
    str2 = str2[::-1] 
  
    carry = 0


    for i in range(n2): 
      

           
        sub = ((ord(str1[i])-ord('0'))-(ord(str2[i])-ord('0'))-carry) 
          
        if (sub < 0): 
          
            sub = sub + 10
            carry = 1
              
        else: 
            carry = 0
  
        str3 = str3+str(sub ) 
          
    
    for i in range(n2,n1): 
      
        sub = ((ord(str1[i])-ord('0')) - carry) 
           
      
        if (sub < 0): 
          
            sub = sub + 10
            carry = 1
          
        else: 
            carry = 0
               
        str3 = str3+str(sub) 
   
  
    str3= str3[::-1] 
   
    return str3 




def matrix_chain_order(p): #a entrada p é caracterizada como o exemplo: matrizes 50x20, 20x1, 1x10, 10x100= (50, 20, 1, 10, 100)
    n = len(p)-1 # numero de matrizes a serem multiplicadas
    m, s = {}, {} # m[i,j] guardará o menor numero de operacoes para se multiplicar as matrizes de i a j;
    for i in range(1, n+1):
        m[(i, i)] = 0 #salva em m[i,i] o numero de operacoes com uma unica matriz = 0
    for l in range(2, n+1): # inicia com cadeia de duas matrizes: l=2 e vai aumentando
        for i in range(1, n-l+2):
            j = i+l-1
            m[(i, j)] = 100000000 
            for k in range(i, j): # obtencao de m[i,j] 
                q = m[(i, k)]+m[(k+1, j)]+p[i-1]*p[k]*p[j] #aqui entra programacao dinamica, pois varios valores da arvore de recursao ja foram calculados e sao trazidos de m
                if q<m[(i, j)]:
                    m[(i, j)] = q #obtencao de m otimo para multiplicacao da cadeia de matrizes de i a j
                    s[(i, j)] = k #onde ocorreu a divisao otima da cadeia de matrizes de i a j
    return m, s

def get_optimal_order(s, i, j): 
    res = ""
    if i == j:
        return ("A"+str(j))
    else:
        res += "("
        res += get_optimal_order(s, i, s[(i, j)])
        res += get_optimal_order(s, s[(i, j)]+1, j)
        res +=  ")"
        return res


def main():
    x, y = 521515, 51252125
    a, b = BigNumber(str(x)), BigNumber(str(y))
    #print("a = {} b = {}")
    print("minha soma {}\nsoma python {}".format(a+b,x+y))
    #print("{} é igual a {}? {}".format(a, b, a==b))
    print("minha mult {}\nmult python {}".format(a*b,x*y))

    #Numeros para subtraçao#
    n1 = "1230434"
    n2 = "12303940394"
    print("subtração: ",subt(n1, n2)) 

    #Numeros para raiz#
    c = 4
    d = 2
    print("Raiz com radicando", c, "e indice", d, " é:",root(c, d))
    #Numeros para exponeciacao#
    e = 3
    f = 2
    print("exponenciação de ", e, "elevado a", f, " é: ",exp(e, f))

    #Multiplicação de Cadeia de matrizes
    p = [50,20,1,10,100]
    m, s = matrix_chain_order(p)
    print ("number operations：", m[(1, len(p)-1)])
    print ("best order of matrix multiplication:", get_optimal_order(s, 1, len(p)-1))


    
if __name__ == "__main__":
    main()

