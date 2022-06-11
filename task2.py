import re
from nltk.tokenize import RegexpTokenizer
import nltk
print('USING THE COUNT FUNCTION')
with open('corpus_teste.txt', 'r',encoding='utf-8') as f:
    txt = f.read()
    tokenizer = RegexpTokenizer(r'\w+')
    texttok = tokenizer.tokenize(txt.lower())
    smiles = ['lol','ah','eh','hi','kkkk','hahaha','rsrsrsrs','ahuahuahuahu','sim','seria']
    for smile in smiles:
        a = texttok.count(smile)
        print(a,smile, 'ocurrences in the corpus') 
print('USING REGEX')
txtbeta = 'k Olha kk que kkk coisa kkkk mais linda,kkkkkkkkkk mais cheia de graça. É ela menina quem vem e que passa, num doce balanço a caminho do mar '
laught1 = re.findall(" lol | ah | eh | hi ", txt.lower())
laught2 = re.findall('kk+kk|haha+ha|rs+rs|hue+hue|aush+aush|ahu+ahu', txt.lower())
expre1 = re.findall('sim', txt.lower())
expre2 = re.findall('seria', txt.lower())
print(len(laught1), len(laught2), len(expre1), len(expre2))
print(laught1,laught2,expre1,expre2)
