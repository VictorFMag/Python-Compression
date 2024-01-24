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

def converteBinario(caminho_arquivo_compactado):
        arquivo_entrada = open(caminho_arquivo_compactado, "r")

        # Lê o conteúdo do arquivo de texto
        data = arquivo_entrada.read().strip()

        # Converte a sequência de 0s e 1s para uma representação binária
        binary_data = ''.join('1' if bit == '1' else '0' for bit in data)

        # Adiciona zeros à direita para garantir que a quantidade total de bits seja múltiplo de 8
        while len(binary_data) % 8 != 0:
            binary_data += '0'

        # Converte a sequência de bits para bytes
        byte_array = bytearray()
        for i in range(0, len(binary_data), 8):
            byte = int(binary_data[i:i+8], 2)
            byte_array.append(byte)

        # Escreve os dados binários em um novo arquivo
        with open('arquivo_binario.bin', 'wb') as file:
            file.write(byte_array)