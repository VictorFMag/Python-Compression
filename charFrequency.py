def cleanArchive(archive):
    with open(archive, 'w') as file:
        file.truncate()

def compact(archiveToCompact):
    cleanArchive("output.txt")

    with open(archiveToCompact, 'r') as archive:
        line = archive.readline()    
        while line:
            charCount = 1  # Inicializa com 1, pois sempre tem pelo menos 1 caractere
            indiceAtual = 0
            while indiceAtual < len(line) - 1:
                if line[indiceAtual] == line[indiceAtual + 1]:
                    charCount += 1
                else:
                    with open("output.txt", 'a') as output:
                        if line[indiceAtual].isspace() or line[indiceAtual].isnumeric():
                            if charCount>1:
                                output.write(str(charCount) + "@" + line[indiceAtual])
                            else:
                                output.write("@" + line[indiceAtual])
                        else:
                            if charCount>1:
                                output.write(str(charCount) + line[indiceAtual])
                            else:
                                output.write(line[indiceAtual])
                    charCount = 1  # Reinicia a contagem para o novo caractere
                indiceAtual += 1

            # Trata o último caractere da linha
            with open("output.txt", 'a') as output:
                if line[-1].isspace() or line[-1].isnumeric():
                    if charCount>1:
                        if line[-1] == "\n":
                            output.write("\n")
                        else:
                            output.write(str(charCount) + "@" + line[-1])
                    else:
                        if line[-1] == "\n":
                            output.write("\n")
                        else:
                            output.write("@" + line[-1])
                else:
                    if charCount>1:
                        output.write(str(charCount) + line[-1])
                    else:
                        output.write(line[-1])

            line = archive.readline()