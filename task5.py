#Resolvendo problemas com 1 única linha
from functools import reduce

# Encontrar o tamanho de cada palavra na frase (quebrado por espaços) e retornar os valores em uma lista.
def word_lengths(phrase):
    return list(map(len, phrase.split()))

# Pegar uma lista de dígitos e retornar o número que eles correspondem a "digitos([3,4,3,2,1]) = 34321."
def digits(numbers):
    return reduce(lambda x,y: x*10+y, numbers)

# Retornar as palavras de uma lista de palavras que começam com uma letra especificada.
def wordsFilter(wordsList, letter):
    return list(filter(lambda x: x[0].lower() == letter,wordsList))

# Retornar uma lista do mesmo comprimento
# onde cada valor é as duas cadeias de caracteres de L1 e L2 concatenados juntos com o conector entre eles
def concatenate(List1, List2, connector):
    return [word1+connector+word2 for (word1,word2) in zip(List1,List2)]

# Retornar um dicionário que tenha os valores da lista como chaves e o índice como o valor
def d_list(L):
    return {key:value for value,key in enumerate(L)}

# Retornar a contagem do número de itens na lista cujo valor é igual ao seu índice.
def count_match_index(L):
    return len([num for count,num in enumerate(L) if num == count])