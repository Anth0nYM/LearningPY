#Manuseie a exceção lançada pelo código abaixo usando os blocos try e except.
def firstquestion():
    try:
        for i in ['a','b','c']:
            print(i**2)
    except TypeError:
        print('Tipo de dado inválido')
        
#Manuseie a exceção gerada pelo código abaixo usando os blocos try e except. 
#Em seguida, use um bloco finally para imprimir 'All Done'.'''
def divisao(): 
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

#Escreva uma função que solicite um número inteiro e imprima o quadrado dele. 
#Use um loop while com um try, except e else para contabilizar as entradas incorretas.
def quadrado():
    c = 0
    while True:
        try:
            num = int(input('Digite um número: '))
        except ValueError:
            print('Por favor digite apenas números')
            c += 1
            print('Você errou {} vezes'.format(c))
        else:
            print('A raiz de seu número é {} '.format(num**2))
            break
while True:
    quadrado()
    resp = input('Deseja continuar? [S/N] ')
    if resp in 'Nn':
        break

