from unidecode import unidecode
import io

def nome_maiusculas():
    nome = input("Diga o seu nome:")
    nome = nome.upper()
    return nome

print(nome_maiusculas())

lista = [1,2,3,4,5,6]

def numpares(lista):
    lista = [x for x in lista if x%2 == 0]
    return lista

print(numpares(lista))


def invertetexto():
    nomeficheiro = input("Coloque o caminho para o ficheiro:")
    for line in reversed(io.open(nomeficheiro, "r", encoding="utf-8").readlines()):
        print(line.rstrip())

print(invertetexto())


def contador():
    nomeficheiro = input("Coloque o caminho para o ficheiro:")
    f = io.open(nomeficheiro, "r", encoding="utf-8")
    f = str(f.read())
    f1 = f.split(" ")
    Dict = {}
    for x in range(len(f1)):
        counter = 0
        for i in range(len(f1)):
            if f1[i] == f1[x]:
                counter = counter + 1
            Dict[f1[x]] = counter
    sortlist = sorted((value, key) for (key, value) in Dict.items())
    sortlist = sortlist[:11:-1]
    return sortlist

print(contador())

pontuacao = ["!", "," , ".", ":", ";", "-", "?", "'", '"', '/']
troca = {"à" : "a", "á" : "a", "ã" : "a", "é" : "e", "è" : "e", "í" : "i", "ì" : "i", "ó" : "o", "ò" : "o", "õ" : "o",
         "ú" : "u", "ù" : "u", "ç" : "c", "ñ" : "n"}

def limpatexto(pontuacao, troca):
    nomeficheiro = input("Coloque o caminho para o ficheiro:")
    f = io.open(nomeficheiro, "r", encoding="utf-8")
    f = f.read()
    for letter in f:
        if letter in pontuacao:
            f = f.replace(letter, (" "+letter))
    for word, replacement in troca.items():
        f = f.replace(word, replacement)
    f1 = f.lower()
    f1 = f1.strip()
    #Usando o unidecode em vez de um dicionário
    #f2 = None
    #for x in range(len(f1)):
        #if f2 == None:
            #f2 = unidecode(f1[x])
        #else:
            #f2 = f2 + unidecode(f1[x])
    #return f2
    return f1

print(limpatexto(pontuacao, troca))

s = "Inserir string aleatorio"

def Invertestring(s):
    S = s[::-1]
    return S

print(Invertestring(s))

def contacarateres(s):
    counter = 0
    for x in range(len(s)):
        if s[x] == "a" or s[x] == "A":
            counter +=1
    return counter

print(contacarateres(s))

vogal = "aeiou"

def vogais(s, vogal):
    S = s.lower()
    vogais = [x for x in S if x in vogal]
    return len(vogais)

print(vogais(s, vogal))

def minusculas(s):
    S = s.lower()
    return S

def maisculas(s):
    S = s.upper()
    return S
