from functools import reduce


class BigNumber:
    def __init__(self, num):
        self.num = num
        self.tam = len(num)
        assert(isinstance(num,str))
        try:
            float(num)
        except ValueError as e:
            raise Exception("Valor inválido recebido! {} tem caracteres não esperados. Apenas números ou . esperados.\n"
                            "Erro:{}".format(num,e))
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

    def __add__(self,other):
        if not isinstance(other, type(self)):
            raise Exception("Adição mal feita, esperava um objeto do tipo {}, tipo {} recebido".format(BigNumber,
                                                                                                       type(other)))
        maior = lambda values: reduce(lambda bigNumA, bigNumB: bigNumA if len(bigNumA) >= len(bigNumB) else bigNumB,
                                      values)
        menor = lambda values: reduce(lambda bigNumA, bigNumB: bigNumA if len(bigNumA) < len(bigNumB) else bigNumB,
                                      values)

        indexTuples, longestNumber, shortestNumber = self._initSum(maior, menor, other)

        res = self._SumSubsets(indexTuples, longestNumber, shortestNumber)

        end = self._JoinSumWithLeftover(longestNumber, res)
        return BigNumber(end)

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
    
""" retorna 1 se A > B, -1 se A < B e 0 Se A = B"""
def compare(self,other):
	if self.__len__() > other.__len__():
		return 1
	elif self.__len__() < other.__len__():
		return -1
	else:
		a = int(0)
		b = int(0)
		for i in range(self.__len__()):
			if ord(self.num[i]) > ord(other.num[i]):
				a += 1
			elif ord(self.num[i]) == ord(other.num[i]):
				a += 1
				b += 1
			else:
				b += 1
		if a > b:
			return 1
		elif b > a:
			return -1
		else:
			return 0


def main():
    x, y = 1230000,1230000
    a, b = BigNumber(str(x)),BigNumber(str(y))
    print("{} + {} = {}".format(a, b, a+b))
    print("{} + {} = {}".format(x, y, x+y))
    print("{} é menor que {}? {}".format(a,b,compare(a,b)))


if __name__ == "__main__":
    main()
