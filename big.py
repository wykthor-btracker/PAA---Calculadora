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


def main():
    pass


if __name__ == "__main__":
    main()
