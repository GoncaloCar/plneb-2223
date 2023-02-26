from unidecode import unidecode

#nome = input("Qual o seu nome:")
#Nome= nome.upper()
#print(Nome)

lista = [1,2,3,4,5,6]

def numpares(lista):
    lista = [x for x in lista if x%2 == 0]
    return lista

print(numpares(lista))

texto = """Coiso 1
Coiso 2
Coiso 3"""

def invertetexto():
    nomeficheiro = input("Escolha o nome do ficheiro:")
    f = open(nomeficheiro, "r")
    f1 = f[::-1]
    return f1

#print(invertetexto())

#f = str("Coiso coiso coisinha coisinha coisinha")

def contador():
    nomeficheiro = input("Coloque o caminho para o ficheiro:")
    f = open(nomeficheiro, "r")
    f = str(f.readlines())
    f1 = f.split(" ")
    Dict = {}
    for x in range(len(f1)):
        counter = 0
        for i in range(len(f1)):
            if f1[i] == f1[x]:
                counter = counter + 1
        if f1[x] not in Dict:
            Dict[f1[x]] = counter
    sortlist = sorted((value, key) for (key, value) in Dict.items())
    sortlist = sortlist[:11:-1]
    return sortlist

#print(contador())

def limpatexto():
    nomeficheiro = input("Escolha o nome do ficheiro:")
    f = open(nomeficheiro, "r")
    f = str(f.readlines())
    f1 = f.lower()
    f2 = None
    for x in range(len(f1)):
        if f2 == None:
            f2 = unidecode(f1[x])
        else:
            f2 = f2 + unidecode(f1[x])
    f3 = f2.split(" ")
    return str(f3)

print(limpatexto()) #ainda não funciona

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
    counter = 0
    S = s.lower()
    vogais = [x for x in s if x in vogal]
    return len(vogais)

print(vogais(s, vogal))

def minusculas(s):
    S = s.lower()
    return S

def maisculas(s):
    S = s.upper()
    return S
