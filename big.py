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

def somar(a,b):
    tam_a = a.__tam__();
    tam_b = b.__tam__();
    c = ''
    aux = int()
    if tam_a <= tam_b:
        while tam_a > 0:
            aux = int(a.num[tam_a-1]) + int(b.num[tam_b-1])
            c = str(aux) + c[0:]
            print(c)
            tam_a -= 1
            tam_b -= 1
        while tam_b > 0:
            c = b.num[tam_b-1] + c[0:]
            tam_b -= 1
    return c
            

def main():
    linha = input('')
    a = BigNumber(linha)
    linha = input('')
    b = BigNumber(linha)
    print(somar(a,b))
	
if __name__ == "__main__":
	main()
