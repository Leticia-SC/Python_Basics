arquivo = open('arqtext.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula Prática')
arquivo.close()

leitura = open('arqtext.txt', 'r')
print(leitura.read())
leitura.close()