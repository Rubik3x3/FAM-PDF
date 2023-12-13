import os
import PyPDF2
import re
import json
import glob

import textoFAM
import datosFAM
import extrasFAM

carpeta_pdfs = "PDFs/2023"
archivos_pdf = glob.glob(os.path.join(carpeta_pdfs, "*.pdf"))

pdf = "PDFs/2023/Resultados 16-09.pdf"

json_torneo = {}

def main():
    for archivo_pdf in archivos_pdf:
        generarTextos(archivo_pdf)
        obtenerDatos()
    print(f'{"<"*25} PROGRAMA FINALIZADO {">"*25}')
def generarTextos(pdf):
    texto_definitivo = str("")
    texto_definitivo = textoFAM.convertirATexto(pdf)
    texto_definitivo = textoFAM.eliminarEspacios(texto_definitivo)
    textoFAM.duplicarDocumento('TEXTOS/Texto-Sin-Espacios-MAYUS.txt',"TEXTOS/FINAL.txt")
    textoFAM.reemplazarEspaciosPorNada("TEXTOS/FINAL.txt")
    textoFAM.reemplazarCaracter("TEXTOS/FINAL.txt","_______________________________________________________________________________________________________","|||")
    extrasFAM.textoFinalizoTarea("GENERAR TEXTOS","-",30)

def obtenerDatos():
    with open("TEXTOS/FINAL.txt", 'r') as archivo:
        contenido = archivo.read()
    variables_torneo = datosFAM.variablesTorneo(contenido)
    datosFAM.guardarJsonVariables(variables_torneo)
    extrasFAM.textoFinalizoTarea("OBTENER VARIABLES","-",30)
    datosFAM.resultadosAtletas(contenido)

if __name__ == "__main__":
    main()