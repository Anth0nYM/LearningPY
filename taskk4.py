#Manuseie a exceção lançada pelo código abaixo usando os blocos try e except.
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('Tipo de dado inválido')
