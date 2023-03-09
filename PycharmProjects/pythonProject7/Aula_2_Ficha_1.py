import re
lines = ["hello world", "goodbye world", "hi, hello there"]

def ex_1(lines):
    for line in lines:
        print(re.match(r'hello', line))
ex_1(lines)

def ex_2(lines):
    for line in lines:
        print(re.search(r'hello', line))

ex_2(lines)

f = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"

def ex_3(f):
    print(re.findall(r'[hH]ello|HELLO' , f))

ex_3(f)

def ex_4(f):
    print(re.sub(r'[hH]ello|HELLO', "*YEP*", f))

ex_4(f)

x = "bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."

def ex_5(x):
    print(re.split(r',' ,x))

ex_5(x)

frase = "Posso ir à casa de banho, por favor?"

def palavra_magica(frase):
    print(re.search(r'por favor?', frase)) #testardepois

palavra_magica(frase)

linha = "Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou."

def narcissismo(linha):
    print(len(re.findall(r'[eE][uU]', linha)))

narcissismo(linha)

linha = "LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei."

novo_curso = "Something"

def troca_curso(linha, novo_curso):
    print(re.sub(r'LEI', novo_curso, linha))

troca_curso(linha, novo_curso)

linha = "1,2,3"

def soma_string(linha):
    sum = 0
    linhas = (re.sub(r',', '', linha))
    for x in linhas:
        sum = sum + float(x)
    return sum

print(soma_string(linha))

pronomes_validos = "eu tu ele ela nos vos eles"


def pronomes (example):
    print(re.findall(r'([eE][uU]\s*|[tT][uU]\s*|[eE][lL][eE]\s*|[eE][lL][aA]\s*|[nN][oO][sS]\s*|[vV][oO][sS]\s*|[eE][lL][eE][sS]\s*)' , example))

pronomes(pronomes_validos)

def variavel_valida():
    variavel = input("Escolha uma variavel")
    if re.findall(r'[a-zA-Z0-9]+', variavel) != variavel :
        print("Variavel ilegal")
    else:
        print("Aceitavel")

variavel_valida()

texto = "coiso   Sim , talvez"
def underscores(texto):
    novo= re.sub(r' +', "_", texto)
    return novo

print(underscores(texto))

def codigos_postais():
    codigo = input("Insira o código postal:")
    print(codigo)
    if re.findall(r'[\d]{4}-[\d]{3}', codigo) == None:
        print("Codigo inválido")
    else:
        novo_codigo= re.split("-", codigo)
        if novo_codigo == codigo:
            print("código válido, a iniciar a operação")
        else:
            print("Codigo inválido")
print(codigos_postais())