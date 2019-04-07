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

def somar(a,b): #só funciona pra um caso, falta implementar o segundo de numero positivo e tratar os numeros negativos
    tam_a = a.__tam__();
    tam_b = b.__tam__();
    c = ''
    aux = int()
    if tam_a <= tam_b:
        for i in reversed(range(tam_a)):
            aux = int(a.num[i]) + int(b.num[tam_b-1])
            c = str(aux) + c[0:]
            tam_b -= 1
        for i in reversed(range(tam_b)):
            c = b.num[i] + c[0:]
    return c
            

def main():
    linha = input('')
    a = BigNumber(linha)
    linha = input('')
    b = BigNumber(linha)
    print(somar(a,b))
	
if __name__ == "__main__":
	main()
