import os
import PyPDF2
import glob

carpeta_pdfs = "PDFs/2023"
archivos_pdf = glob.glob(os.path.join(carpeta_pdfs, "*.pdf"))

for archivo_pdf in archivos_pdf:
    nombre_archivo = os.path.basename(archivo_pdf)
    nombre_sin_extension = os.path.splitext(nombre_archivo)[0]
    nombre_txt = nombre_sin_extension + ".txt"
    ruta_salida_txt = os.path.join(carpeta_pdfs, nombre_txt)

    with open(archivo_pdf, "rb") as f_pdf:
        pdf = PyPDF2.PdfReader(f_pdf)
        texto = ""
        for pagina in range(len(pdf.pages)):
            texto += pdf.pages[pagina].extract_text()

    texto_en_mayusculas = texto.upper()

    with open(ruta_salida_txt, "w", encoding="utf-8") as f_txt:
        f_txt.write(texto_en_mayusculas)

print("Conversiones completadas.")
