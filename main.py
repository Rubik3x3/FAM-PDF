import os
import PyPDF2
import re
import json

import textoFAM
import datosFAM
import extrasFAM


pdf = "PDFs/torneog.pdf"

def main():
    generarTextos()
    obtenerDatos()

def generarTextos():
    texto_definitivo = str("")
    texto_definitivo = textoFAM.convertirATexto(pdf)
    texto_definitivo = textoFAM.eliminarEspacios(texto_definitivo)
    textoFAM.duplicarDocumento('TEXTOS/Texto-Sin-Espacios-MAYUS.txt',"TEXTOS/FINAL.txt")
    textoFAM.reemplazarCaracter("TEXTOS/FINAL.txt","_______________________________________________________________________________________________________","|||")
    extrasFAM.textoFinalizoTarea("GENERAR TEXTOS","-",30)

def obtenerDatos():
    with open("TEXTOS/FINAL.txt", 'r') as archivo:
        contenido = archivo.read()
        
    variables_torneo = datosFAM.variablesTorneo(contenido)
    print(variables_torneo)
    extrasFAM.textoFinalizoTarea("OBTENER DATOS","-",30)

if __name__ == "__main__":
    main()
