def cleanArchive(archive):
    with open(archive, 'w') as file:
        file.truncate()

def compress(archiveToCompact):
    cleanArchive("compressedFile.txt")

    with open(archiveToCompact, 'r') as archive:
        line = archive.readline()    
        while line:
            charCount = 1  # Inicializa com 1, pois sempre tem pelo menos 1 caractere
            indiceAtual = 0
            
            while indiceAtual < len(line) - 1:
                if line[indiceAtual] == line[indiceAtual + 1]:
                    charCount += 1
                else:
                    with open("./compressedFile.txt", 'a') as compressed:
                        if line[indiceAtual].isnumeric():
                            if charCount>1:
                                compressed.write(str(charCount) + "@" + line[indiceAtual])
                            else:
                                compressed.write("@" + line[indiceAtual])
                        else:
                            if charCount>1:
                                compressed.write(str(charCount) + line[indiceAtual])
                            else:
                                compressed.write(line[indiceAtual])
                    charCount = 1  # Reinicia a contagem para o novo caractere
                indiceAtual += 1

            # Trata o último caractere da linha
            with open("compressedFile.txt", 'a') as compressed:
                if line[-1].isnumeric():
                    if charCount>1:
                        if line[-1] == "\n":
                            compressed.write("\n")
                        else:
                            compressed.write(str(charCount) + "@" + line[-1])
                    else:
                        if line[-1] == "\n":
                            compressed.write("\n")
                        else:
                            compressed.write("@" + line[-1])
                else:
                    if charCount>1:
                        compressed.write(str(charCount) + line[-1])
                    else:
                        compressed.write(line[-1])

            line = archive.readline()