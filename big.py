class BigNumber:
    def __init__(self, num):
        self.num = num
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

def main():
	linha = input('')
	a = BigNumber(linha)
	print(a)
	
if __name__ == "__main__":
	main()
