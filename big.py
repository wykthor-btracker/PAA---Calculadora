class BigNumber:
    def __init__(self, num):
        self.num = num

    def mostrar(self):
        print(self.num)


def main():
	linha = input('');
	a = BigNumber(linha);
	a.mostrar();

main();