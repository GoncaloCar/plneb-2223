import re

file = open("dicionario_medico.txt", encoding = "utf8")
text = file.read()
text = re.sub(r"\f", "", text)
remove_term_ff = re.sub(r"\f(.+\n[A-ZÁÉÍÓÚÀÂÊÔÃÕÇ])", r"\1", text)
remove_definition_ff = re.sub(r"\n\f+", "", remove_term_ff)
mark_term = re.sub(r"\n\n(.+)", r"\n\n#\1", remove_definition_ff)
mark_definition = re.sub(r"\n([^#\s].+)", r"\n?\1", mark_term)
join = re.sub(r"(\n\?.+)\n\?(.+)",r"\1 \2", mark_definition)
remove = re.sub(r"[#|?]", r"", join)
entries = re.findall(r"\n\n(.+)\n(.+)", remove)


file.close()
texto = open('dicionario_medico_teste.txt', 'w', encoding='utf8')
texto.write(remove)
texto.close()
html = open('dicionario_medico.html', 'w', encoding='utf8')

header = '''<html>
    <head>
        <meta charset = 'utf-8'/>
        <style>
            table, td, th {
                border: 1px solid;
        }

            table {
                width: 100%;
                border-collapse: collapse;
        }
    </style>
    </head>
'''
body = """
    <body>
        <table>
            <tr>
                <th>Termo</th>
                <th>Definição</th>
            </tr>
"""
for entry in entries:
    body += f"""
            <tr>
                <td>{entry[0]}</td>
                <td>{entry[1]}</td>
            </tr>
"""

body += """
        </table>
    </body>
"""

footer = """
</html>
"""

html.write(header+body+footer)
html.close()