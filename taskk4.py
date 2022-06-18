#Manuseie a exceção lançada pelo código abaixo usando os blocos try e except.
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
   print('Tipo de dado inválido')
    
#Manuseie a exceção gerada pelo código abaixo usando os blocos try e except. 
#Em seguida, use um bloco finally para imprimir 'All Done'.'''
try:
    x =int(input('Digite um número: '))
    y =int(input('Digite outro número: '))
    z = x/y
except ZeroDivisionError:
    print('Não é possível dividir por zero')
except TypeError:
    print('Por favor digite apenas números')
else:
    print(z)
finally:
    print('All Done')    

