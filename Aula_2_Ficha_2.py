import re
texto = """A 03/01/2022, Pedro viajou para a praia com a sua família.
Eles ficaram hospedados num hotel e aproveitaram o sol e o mar durante toda a semana.
Mais tarde, no dia 12/01/2022, Pedro voltou para casa e começou a trabalhar num novo projeto.
Ele passou muitas horas no escritório, mas finalmente terminou o projeto a 15/01/2022."""

def iso_8601(texto):
    data = re.sub(r'(\d{2})/(\d{2})/(\d{4}\b)', r'\3-\2-\1', texto)
    return data

print(iso_8601(texto))

file_names = [
  "document.txt", # válido
  "file name.docx", # inválido
  "image_001.jpg", # válido
  "script.sh.txt", # válido
  "test_file.txt", # válido
  "file_name.", # inválido
  "my_resume.docx", # válido
  ".hidden-file.txt", # válido
  "important-file.text file", # inválido
  "file%name.jpg" # inválido
]



def files(file_names):
    ficheiros = re.findall(r'\.*[\w|-]+\.+[\w|.|-]+', str(file_names))
    print(ficheiros)
    lista= []
    for x in ficheiros:
        if x in file_names:
            lista.append(x)
    for file_name in lista:
        match = re.search(r'^(.+)\.([^.]+)$', file_name)

        if match:
            dict = { match.group(1) : match.group(2)}
            print(dict)
        else:
            continue

files(file_names)

texto = """Este texto foi feito por Sofia Guilherme Rodrigues dos Santos, com 
base no texto original de Pedro Rafael Paiva Moura, com a ajuda
dos professores Pedro Rangel Henriques e José João Antunes Guimarães Dias De Almeida.
Apesar de partilharem o mesmo apelido, a Sofia não é da mesma família do famoso
autor José Rodrigues dos Santos."""

#ainda não funciona
def conversao_nomes(texto):
    print(re.sub(r'(([A-Z]\w+)\s?((?:[A-Z]\w+\s?|d[oae]s?\s?)*)\s[A-Z]\w+)', r"\3, \1", texto))
conversao_nomes(texto)




codigo = [
    "4700-000", # válido
    "9876543", # inválido
    "1234-567", # válido
    "8x41-5a3", # inválido
    "84234-12", # inválido
    "4583--321", # inválido
    "9481-025" # válido
]
def codigos_postais(codigo):
    validos = re.findall(r'[\d]{4}-[\d]{3}', str(codigo))
    if validos != None:
        validos = re.split("-", str(validos))
    return validos


print(codigos_postais(codigo))

abreviaturas = {
    "UM": "Universidade do Minho",
    "LEI": "Licenciatura em Engenharia Informática",
    "UC": "Unidade Curricular",
    "PL": "Processamento de Linguagens"
}

texto = "A /abrev{UC} de /abrev{PL} é muito fixe! É uma /abrev{UC} que acrescenta muito ao curso de /abrev{LEI} da /abrev{UM}."

def abrev(abreviaturas, texto):
    matches = re.findall(r'/abrev{[A-Z]*}', texto)
    for match in matches:
        abbreviation = re.search(r'{([A-Z]+)}', match).group(1)
        if abbreviation in abreviaturas:
            value = abreviaturas[abbreviation]
            texto = re.sub(re.escape(match), value, texto)

    return texto

print(abrev(abreviaturas, texto))
matriculas = [
    "AA-AA-AA", # inválida
    "LR-RB-32", # válida
    "1234LX", # inválida
    "PL 22 23", # válida
    "ZZ-99-ZZ", # válida
    "54-tb-34", # inválida
    "12 34 56", # inválida
    "42-HA BQ" # válida, mas inválida com o requisito extra
]

def matricula_valida(matriculas):
    match = re.findall(r'([A-Z]{2}|\d{2})(-| )(\d{2}|[A-Z]{2})(-| )([A-Z]{2}|\d{2})', str(matriculas))
    valid_match = []
    for x in match:
        if len(re.findall(r'[A-Z]+', str(x))) > 2 or len(re.findall(r'[A-Z]+', str(x))) < 1:
            continue
        elif len(re.findall(r'\d+', str(x))) < 1 or len(re.findall(r'\d+', str(x))) > 2:
            continue
        else:
            valid_match.append(x)
    return valid_match

print(matricula_valida(matriculas))


texto = """Num lindo dia de [ESTAÇÃO DO ANO], [NOME DE PESSOA] foi passear com o seu [EXPRESSÃO DE PARENTESCO MASCULINA]. 
Quando chegaram à [NOME DE LOCAL FEMININO], encontraram um [OBJETO MASCULINO] muito [ADJETIVO MASCULINO].
Ficaram muito confusos, pois não conseguiam identificar a função daquilo.
Seria para [VERBO INFINITIVO]? Tentaram perguntar a [NOME DE PESSOA FAMOSA], que também não sabia.
Desanimados, pegaram no objeto e deixaram-no no [NOME DE LOCAL MASCULINO] mais próximo. 
Talvez os [NOME PLURAL MASCULINO] de lá conseguissem encontrar alguma utilidade para aquilo."""
#def mad_libs(texto):
    #espacos = re.findall(r'\[[\w\s]+\]', texto)
    #for espaco in espacos:
        #resposta = str(input(f"{espaco}: "))
        #texto = re.sub(r"\[[\w\s]+\]", resposta, texto, 1)
    #return texto

#print(mad_libs(texto))

def remocao(texto):
    palavras = re.sub(r"\b(?<!-)(\S+)(\s\1)+\b", r"\1", texto)
    return palavras

print(remocao(texto))


