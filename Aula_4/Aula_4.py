import re
import json

def limpa(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()


ficheiro = open("dicionario_medico.xml", "r", encoding="utf-8")
text = ficheiro.read()
text = re.sub(r"</?page.*>", "", text)
text = re.sub(r"</?text.*?>", "", text)
lista = re.findall(r"<b>(.*)</b>([^<]*)", text)
lista = [(designacao, limpa(descricao))for designacao, descricao in lista]
dicionario = dict(lista)
out =open("dicionario_medico_aula.json", "w", encoding="utf-8")
json.dump(dicionario, out, ensure_ascii=False, indent=4)
out.close()
-----------------------------------------------------------------------------------------------------------------------
pdf = open("LIVRO-Doenças-do-Aparelho-Digestivo.txt", "r", encoding="utf-8")
chave = str(dicionario.keys())
valor = str(dicionario.values())
lista1 = []
for line in pdf:
    words = str(line.split())
    words = re.sub(r"[\[|\]]", "", words)
    words = re.sub(r"[']", "", words)
    words = re.sub(r",\s", " ", words)
    if words in chave:
        words = words + " " + str(dicionario.get(words))
        words = re.sub(r"None", "", words)
    if words is not None:
        lista1.append(str(words))

out =open("dicionario_medico_aula2.json", "w", encoding="utf-8")
json.dump(lista1, out, ensure_ascii=False, indent=4)
out.close()



