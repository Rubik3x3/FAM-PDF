import re

texto = """
RESULTADOS TORNEO JOSE DE SAN MARTÍN FECHA: 12/08/2023 - 12/08/2023 SIGLAS-LUGAR: FAMCEN120823 PAIS: ARG ORGANIZA: FAM FISCALIZA: FAM MAYORES-M ||| 200 ELECTRONICO : MAYORES -M FINAL_A FECHA: 12/8/2023 HORA: 12.15 VIENTO: 0 MTS./SEG ||| 01 DIAMANTE BAUTISTA 28/2 /2003 SAVB - FAM ARG 21.80 -1.3 02 MANUEL FEDERICO ROBLES / /2004 AAPCH - FAM ARG 22.34 -1.3 03 HARTE FELIPE 8 /8 /2002 MSI - FAM ARG 22.58 -1.3 04 ERIC PATRICIO GILL / /2002 SGLZ - FAM ARG 23.00 -1.1 05 MATEO DURAN - /- /2004 CHAMA - FAM ARG 23.12 -1.3 06 ELIAN BAUTISTA SEMIENCHUK VALLEJOS - /- /2000 MFV - FAM ARG 23.32 -1.3 07 FEDERICO GADDI - /- /2003 QUIRO - FAM ARG 23.45 -1.3 08 NICOLAS CASTRO - /- /2002 QUIRO - FAM ARG 23.71 -1.1 09 AGUSTIN MAYO / /2008 QUIRO - FAM ARG 23.90 -2.0 10 OBREGON ISAAC YAIR 30/6 /1995 MM - FAM ARG 23.92 -1.3 11 JOAQUIN CRISTIAN RAMALLO / /2002 QUIRO - FAM ARG 24.01 -2.0 12 CUEVAS BRIZUELA MANUEL ALEJANDRO 16/8 /1997 AAMT - FAM ARG 24.23 -2.0 13 PEDRO SOMMA / /2005 SAVB - FAM ARG 24.28 -1.1 14 MILTON MARTINEZ / /2008 FCMAX - FAM ARG 24.29 -2.0 15 ANAKIN LORAN - /- /2002 ET - FAM ARG 24.31 -1.1 16 BRUNO CARRASC O MARTINEZ / /2006 CHAMA - FAM ARG 24.33 -0.5 16 IVO TOBIAS AYALA / /2004 MLAM - FAM ARG 24.33 -0.5 17 CHAPARRO RODRIGO 19/12/2000 LIBRE - ---- ARG 24.39 -1.1 18 DARÃ O ANDRÃ©S CACCIATORE - /- /1996 EMA - FAM ARG 24.41 -0.5 18 FEDERICO ALFONSO LABONIA - /- /2003 QUIRO - FAM ARG 24.41 -1.1 19 KELMANOWICS IAN 13/8 /2000 - - FABPA ARG 24.42 -1.5 20 JORGE LUIS SILVERA - /- /2005 MLAM - FAM ARG 24.52 -1.1 21 PEDRO LABRADOR 29/7 /1996 OTRA FE - FABPA ARG 24.61 -2.0 22 NAHUEL LEGUIZA - /- /2004 LTFAM - FAM ARG 24.62 -1.3 23 GIANLUCA ALEJANDRO CHUMBITA / /2008 MMA - FAM ARG 24.66 -0.5 24 ELIAS TOMAS GUERRA - /- /2002 MLAM - FAM ARG 24.68 -1.1 24 LAUTARO DAVID VA RGAS / /2005 MLAM - FAM ARG 24.68 -1.5 25 SANTIAGO MOURE / /2004 MSI - FAM ARG 24.70 -1.5 26 FACUNDO GALVAN / /2004 GARIN - FAM ARG 24.74 -0.8 27 AGUSTÃ N ASCUNE / /2006 CADAF - FAM ARG 24.87 -0.8 28 KAPRIEL CORTEZ - /- /2008 CHAMA - FAM ARG 24.90 -0.8 29 FELIPE FOLATELLI / /2009 MSI - FAM ARG 24.91 -1.5
"""
patron_nombre_fecha = r'\d+\s([A-Z\s]+)\s+(\d+/\d+\s*/\d+)'
coincidencias = re.findall(patron_nombre_fecha, texto)
for coincidencia in coincidencias:
    print("Nombre:", coincidencia[0])
    print("Fecha de nacimiento:", coincidencia[1])
    print()
