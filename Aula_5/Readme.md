No primeiro caso, ou seja, tradução de portugês/inglês/alemão, nós abrimos o dicionário de termos da aula em formato json e prosseguimos a lê-lo. De seguida, utilizamos as chaves do nosso dicionário, ou seja, a designação dos nossos termos, e traduzi-mo-las para inglês e alemão. De seguida os termos são escritos num dicionário acompanhados das suas traduções, e da sua descrição. Por razões de economização de tempo tendo em conta a demora quando utilizados todos os termos, utilizaram-se apenas os primeiros 20.



O ficheiro dicionario_traducoes começa por abrir dois ficheiros: O dicionario que contem todos os termos e as suas definições em formato json, assim como o ficheiro termos_traduzidos.
Depois disto, primeiro partimos of ficheiro termos_traduzidos, usando "@" como parâmetro para tal, ficando assim com outro dicionario de termos, um contendo os termos em português e outro contendo os termos em inglês.
De seguida começamos a iterar por todas as chaves presentes no nosso dicionário inicial e a compara-las com as presentes chaves presentes no nosso segundo dicionario. Quando isto se verificar, vamos adicionar a um terceiro dicionário o termo que corresponde à chave, adicionando também o termo em inglês e por fim, o valor que a chave teria no dicionário, ou seja o seu significado.
Caso o termo não esteja presente, traduzimos o termo de português para inglês e depois continuamos como acima referido.
Por fim, escreve-se num ficheiro json os resultados.