import functools
#Calcular o volume de uma esfera dado seu raio.
from calendar import c


def vol(rad):
    volume = (4/3) * 3.14 * (rad**3)
    return volume
    
#Verificar se um número está em um determinado intervalo (inclusive o máximo e mínimo)
def ran_check(num,low,high):
    if num in range (low,high+1):
        return True
    
#Calcule o número de maiúsculas e minúsculas em uma string.
def up_low(s):
    result = []
    token = [i for i in s]
    for i in token:
        if i.isupper():
            result.append('upper')
        elif i == i.lower():
            result.append('lower')
        else:
            continue    
    return result.count('upper'), result.count('lower')

#Recebe uma lista e retorna uma nova lista com elementos exclusivos da primeira lista.
def unique_list(l):
    return list(set(l))

#Multiplicar todos os números em uma lista.
def multiply(numbers):  
    result = 1
    for i in numbers:
        result *=i
    print(result)
        
#Testando Map
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)

def mapteste():
    
    temp = [0, 22.5, 40,100]

    F_temps = list(map(fahrenheit, temp))

    # Converte devolta
    list(map(celsius, F_temps))

    # Combinando Map com lamdba
    list(map(lambda x: (5.0/9)*(x - 32), F_temps))

    #map com vários argumentos
    a = [1,2,3,4]
    b = [5,6,7,8]
    c = [9,10,11,12]

    list(map(lambda x,y:x+y,a,b))

    list(map(lambda x,y,z:x+y+z, a,b,c))
def reduceteste():
    lst =[47,11,42,13]
    anth = functools.reduce(lambda x,y: x+y,lst)
    print(anth)
    
def filterteste():
    lista = [i for i in range(101)]
    a = list(filter(lambda x: x%2==0, lista))
    print(a)
    
def zipteste():
    lista = [i for i in range(1,101)]
    lista2 = [i for i in range(101,201)]
    a = list(zip(lista,lista2))
    return a

#zip em dicionários
d1 = {'a':1,'b':2,'c':3}
d2 = {'d':4,'e':5,'f':6}
def zipemdict():
    a = list(zip(d1.values(),d2.values()))
    return a

def switcharoo(d1,d2):
    dout = {}
    
    for d1key,d2val in zip(d1,d2.values()):
        dout[d1key] = d2val
    
    return dout
print(switcharoo(d1,d2))


