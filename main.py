import PyPDF2

textoDef = ""


def generarTXT(texto, nombre):
    archivo = open(""+nombre+".txt", "w")
    archivo.write(texto)
    archivo.close
    print(f'Archivo {nombre} generado.')


def generarTextoMAYUS(texto, nombre):
    textoMayus = texto.upper()
    generarTXT(textoMayus, nombre+"-MAYUS")


def convertirATexto(archivo):
    with open(archivo, 'rb') as pdf:
        reader = PyPDF2.PdfFileReader(pdf, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)
        textoFin = ' '.join(pdf_text)
        generarTXT(textoFin, "Texto-Original")
        generarTextoMAYUS(textoFin, "Texto-Original")
        return textoFin


def eliminarCaracter(texto, char):
    palabras = texto.split()
    nuevas_palabras = []
    for palabra in palabras:
        result = palabra.replace(char, '')
        nuevas_palabras.append(result)
    texto_final = ' '.join(nuevas_palabras)
    generarTXT(texto_final, "Texto-Sin-Caracter-Y-Espacios")
    generarTextoMAYUS(texto_final, "Texto-Sin-Caracter-Y-Espacios")
    return texto_final


def eliminarEspacios(texto):
    palabras = texto.split()
    texto_final = ' '.join(palabras)
    generarTXT(texto_final, "Texto-Sin-Espacios")
    generarTextoMAYUS(texto_final, "Texto-Sin-Espacios")
    return texto_final


def main():
    textoDef = convertirATexto("fam.pdf")
    textoDef = eliminarEspacios(textoDef)
    textoDef = eliminarCaracter(textoDef, "_")


if __name__ == "__main__":
    main()
