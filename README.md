# Projeto de PAA - Calculadora

## Interface:

Todas as funcionalidades implementadas receberão dois inteiros(as vezes instâncias da classe BigNumber, que representam inteiros maiores que o computador pode armazenar em um registrador de 32 ou 64 bits) ou duas matrizes, uma exceção deve ser levantada quando o tipo errado de dado for enviado para a funcionalidade, por exemplo:
```python
somarInteiro(matrizA,matrizB)
ExceptionTraceback (most recent call last)
<ipython-input-6-7af3bab93e8a> in <module>
----> 1 raise Exception("Tipo de {} inválido, {} esperado".format(int,str))

Exception: Tipo de <class 'int'> inválido, <class 'str'> esperado
```

A funcionalidade retornará um valor do tipo equivalente à operação, retornando um valor inteiro quando possível, e um float quando necessário.

Nas funcionalidades que necessitam de BigNumber, utilizar-se-á instâncias da classe BigNumber, 
Não foi possível fazer uma interface para o projeto. No arquivo Big estão as funciconalidades: soma, subtração e multiplicação de bigNumbers. E por fim a cadeia de multiplicação de matrizes, que dá a melhor sequência para multiplicar várias matrizes com menor número de operações. 
