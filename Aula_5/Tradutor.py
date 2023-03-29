from deep_translator import GoogleTranslator
import json

trad_txt = open("dicionario_medico_aula.json", encoding="utf-8")
trad = json.load(trad_txt)
trad_txt.close()

dic={}
I = 0
for termo in trad:
    if I < 20:
        dic[termo]={
            "en": GoogleTranslator(source="pt", target="en").translate(termo),
            "de": GoogleTranslator(source="pt", target="de").translate(termo),
            "des": trad[termo]
    }
    I = I + 1
        

trad_pt_en_de = open("dicionario_pt_en_de.json", "w", encoding="utf-8")
json.dump(dic, trad_pt_en_de, ensure_ascii=False, indent=4)
trad_pt_en_de.close()