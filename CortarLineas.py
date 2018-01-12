nLines, nWords = 0,0

ruta = raw_input("Ruta del archivo a cortar: ")

while True:
    palabras = raw_input("Palabra a buscar: ")
    InputStream = open(ruta,'r')
    for currLine in InputStream:
        if (not currLine.find(palabras)):
            print(currLine)
    respuesta = raw_input("Otra palabra? y/n: ")
    if respuesta == "n":
        break
    elif respuesta == "y":
        True
    else:
        break            