import json
from deep_translator import GoogleTranslator

dic = open("dicionario_medico_aula.json", encoding="utf-8")
dic1 = json.load(dic)
dic.close()

trad_txt = open("termos_traduzidos.txt", encoding="utf-8")
trad = trad_txt.read().splitlines()
trad_txt.close()

dic_pt_eng = {}
for termo in trad:
    lista = termo.split(" @ ")
    dic_pt_eng[lista[0]] = eng = lista[1]

dic_trad = {}
for termo in dic1.keys():
    if termo in dic_pt_eng.keys():
        dic_trad[termo] = {"en": dic_pt_eng[termo],
                           "desc": dic1[termo]}
    else:
        dic_trad[termo]= {"en": GoogleTranslator(source="pt", target="en").translate(termo),
                          "desc": dic1[termo]}
        
traducoes = open("dicionario_traducoes.json","w" ,encoding="utf-8")
json.dump(dic_trad, traducoes, ensure_ascii=False, indent=4)
traducoes.close()

