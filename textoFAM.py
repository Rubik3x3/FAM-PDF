import os
import PyPDF2

def generarTXT(texto, nombre):
    if not os.path.exists("TEXTOS"):
        os.makedirs("TEXTOS")
        print(f'Se ha creado la carpeta')
    else:
        pass
    
    
    archivo = open("TEXTOS/"+nombre+".txt", "w")

    archivo.write(texto)
    archivo.close

    #print(f'Archivo {nombre} generado.')


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

def duplicarDocumento(viejo, nuevo):
    nombre_archivo = viejo

    try:
        with open(nombre_archivo, 'r') as archivo_original:
            contenido_original = archivo_original.read()

        with open(nuevo, 'w') as archivo_duplicado:
            archivo_duplicado.write(contenido_original)

        #print("Archivo duplicado correctamente.")

    except FileNotFoundError:
        print("El archivo original no fue encontrado.")
    except Exception as e:
        print(f"Error al duplicar el archivo: {e}")

def reemplazarCaracter(archivo,palabra,palabraNueva):
    palabra_a_reemplazar = palabra
    nueva_palabra = palabraNueva

    archivoFINAL = archivo

    with open(archivoFINAL, 'r') as archivo:
        contenido = archivo.read()

    contenido_modificado = contenido.replace(palabra_a_reemplazar, nueva_palabra)

    with open(archivoFINAL, 'w') as archivo:
        archivo.write(contenido_modificado)