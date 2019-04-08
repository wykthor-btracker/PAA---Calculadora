class BigNumber:
    def __init__(self, num):
        self.num = num
        self.tam = len(num);
        assert(isinstance(num,str))
        try:
            float(num)
        except ValueError as e:
            raise Exception("Valor inválido recebido! {} tem caracteres não esperados. Apenas números ou . esperados.\nErro:{}".format(num,e))
        except Exception as e:
            raise Exception("Exceção inesperada: {}".format(e))
    def __str__(self):
        return self.num

    def __repr__(self):
        return "BigNumber({})".format(num)

    def __tam__(self):
        return self.tam

def exp_by_squaring(x, n):
    if n.num < str(0):
        return exp_by_squaring(1 / x, -n);
    elif n == 0:
        return  1;
    elif n == 1:
        return  x ;
    elif n.num // 2 == 0:
        return exp_by_squaring(x * x,  n // 2);
    elif n.num // 2 == 1:
        return x * exp_by_squaring(x * x, (n - 1) // 2);

def main():
    linha = input('')
    a = BigNumber(linha)
    linha = input('')
    b = BigNumber(linha)
    print(exp_by_squaring(a,b))
	
if __name__ == "__main__":
	main()
