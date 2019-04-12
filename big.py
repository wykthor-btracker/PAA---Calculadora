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
        return chute

def exp(x, n):
    if n == 1:
        return x;
    if n % 2 == 0:
        return exp(x * x, n // 2)
    return x * exp(x * x, n // 2)

def main():
    x, y = 521515, 51252125
    a, b = BigNumber(str(x)), BigNumber(str(y))
    print("a = {} b = {}")
    print("minha soma {}\nsoma python {}".format(a+b,x+y))
    print("{} é igual a {}? {}".format(a, b, a==b))
    print("minha mult {}\nmult python {}".format(a*b,x*y))


if __name__ == "__main__":
    main()
