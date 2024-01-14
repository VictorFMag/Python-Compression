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

def decompress(compactedFile):
    cleanArchive("decompressedFile.txt")

    with open(compactedFile, 'r') as compressed:
        with open("decompressedFile.txt", 'a') as decompressed:
            line = compressed.readline()

            while line:
                indiceAtual = 0
                for char in line:
                    #3 casos -> char isdigit seguido de char nao digito
                    #char is digit seguido de @
                    #char is not digit
                    if char.isdigit() and line[indiceAtual+1] != "@":
                        for i in range (int(char)):
                            decompressed.write(line[indiceAtual+1])
                            print("escrevendo:",line[indiceAtual+1])
                    elif char.isdigit() and line[indiceAtual+1] == "@":
                        for i in range (int(char)):
                            decompressed.write(line[indiceAtual+2])
                            print("escrevendo:",line[indiceAtual+2])
                    else:
                        if line[indiceAtual-1] == "@" or line[indiceAtual-1].isdigit():
                            print("escrevendo: nada")
                            pass
                        else:
                            decompressed.write(char)
                            print("escrevendo:",char)
                    indiceAtual+=1
                line = compressed.readline()