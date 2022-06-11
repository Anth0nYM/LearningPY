##Printar apenas as palavras que começam com a letra s.
st = 'Print only the words that start with s in this sentence'
'''for i in st.split():
    if i[0] == 's':
        print(i)
        '''
##Todos os pares de 0 a 10. 
'''pares = [i for i in range(0,11) if i % 2 == 0] 
print(pares)      '''

##Criar uma lista de todos os números entre 1 e 50 que são divisíveis por 3.
'''numlist = [i for i in range(1,51) if i % 3 == 0]
print(numlist)'''

##Percorra a string st e se o comprimento de uma palavra for par imprima "é par!"
'''st = 'Print every word in this sentence that has an even number of letters'
for i in st.split():
    if len(i) % 2 == 0:
        print(i, 'é par!')'''
##Imprima os números inteiros de 1 a 100. Para múltiplos de três imprima "Fizz" ao ivés do número, e para os múltiplos de cinco imprima "Buzz". Para números que são múltiplos de três e cinco imprima "FizzBuzz".
'''for i in range(0,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)'''
##Criar uma lista das primeiras letras de cada palavra na string abaixo:
'''st = 'Create a list of the first letters of every word in this string'
lista = [i[0] for i in st.split()]
print(lista)'''
