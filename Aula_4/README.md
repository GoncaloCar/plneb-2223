﻿Ficheiros da aula 4
 
 Além dos ficheiros correspondentes à aula 4, também está presente o ficheiro pdf correspondente ao livro de doenças, assim como o txt correspondente.
 Depois de aberto o ficheiro txt, foram separados os termos e as designações do dicionario criado na aula e por fim foi criada uma lista para colocar os termos.
 Depois, o ficheiro aberto é iterado linha a linha. As linhas são separadas em conjuntos de carateres com o uso de split(), procedendo-se à eliminação de virgúlas ou parentesis criados pela passagem a lista. 
 Depois é verificado se o termo se encontra no dicionário, e, se sim, é-lhe adicionada a sua descrição somando os dois strings. Se a palavra for "None", esta é removida (pois neste caso, é um artefacto da comparação).
 Por fim, assegura-se que o tipo do que queremos juntar à lista não é None, e, caso isto se verifique, adiciona-mos à lista. Depois procedemos a escrever isto num ficheiro em formato .json.
