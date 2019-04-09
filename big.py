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

def exp(x, n):

    if n < 0:
        return exp(1 / x, -n);
    elif n == 0:
        return  1;
    elif n == 1:
        return  x ;
    elif n // 2 == 0:
        return exp(x * x,  n // 2);
    elif n // 2 == 1:
        return x * exp(x * x, (n - 1) // 2);
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

def main():
    a = int(input(''))
    b = int(input(''))
    print(exp(a,b))
    print(root(a,b))
	
if __name__ == "__main__":
	main()