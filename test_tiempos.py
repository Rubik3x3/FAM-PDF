import pandas as pd

# Los datos proporcionados
datos = """
01 DIAMANTE BAUTISTA 28/2 /2003 SAVB - FAM ARG 21.80 -1.3
02 MANUEL FEDERICO ROBLES / /2004 AAPCH - FAM ARG 22.34 -1.3
03 HARTE FELIPE 8 /8 /2002 MSI - FAM ARG 22.58 -1.3
04 ERIC PATRICIO GILL / /2002 SGLZ - FAM ARG 23.00 -1.1
05 MATEO DURAN - /- /2004 CHAMA - FAM ARG 23.12 -1.3
06 ELIAN BAUTISTA SEMIENCHUK VALLEJOS - /- /2000 MFV - FAM ARG 23.32 -1.3
07 FEDERICO GADDI - /- /2003 QUIRO - FAM ARG 23.45 -1.3
08 NICOLAS CASTRO - /- /2002 QUIRO - FAM ARG 23.71 -1.1
09 AGUSTIN MAYO / /2008 QUIRO - FAM ARG 23.90 -2.0
10 OBREGON ISAAC YAIR 30/6 /1995 MM - FAM ARG 23.92 -1.3
11 JOAQUIN CRISTIAN RAMALLO / /2002 QUIRO - FAM ARG 24.01 -2.0
12 CUEVAS BRIZUELA MANUEL ALEJANDRO 16/8 /1997 AAMT - FAM ARG 24.23 -2.0
13 PEDRO SOMMA / /2005 SAVB - FAM ARG 24.28 -1.1
14 MILTON MARTINEZ / /2008 FCMAX - FAM ARG 24.29 -2.0
15 ANAKIN LORAN - /- /2002 ET - FAM ARG 24.31 -1.1
16 BRUNO CARRASC O MARTINEZ / /2006 CHAMA - FAM ARG 24.33 -0.5
"""

# Dividir los datos en líneas
lineas = datos.strip().split('\n')

# Organizar los datos en listas
posiciones = []
nombres = []
fechas_nacimiento = []
clubes = []
federaciones = []
paises = []
tiempos = []
vientos = []

# Iterar sobre las líneas para extraer los datos
for linea in lineas:
    campos = linea.split()
    posiciones.append(campos[0])
    
    # Unir el nombre completo
    nombre_completo = ' '.join(campos[1:])
    fecha_index = nombre_completo.rfind('/')  # Encontrar el último '/' para separar la fecha de nacimiento
    nombres.append(nombre_completo[:fecha_index].strip())
    fechas_nacimiento.append(nombre_completo[fecha_index:].strip())  # Obtener la fecha de nacimiento
    
    clubes.append(campos[-6])
    federaciones.append(campos[-5])
    paises.append(campos[-4])
    tiempos.append(campos[-3])
    vientos.append(campos[-2])

# Crear el DataFrame de Pandas
data = {
    'Posición': posiciones,
    'Nombre': nombres,
    'Fecha de Nacimiento': fechas_nacimiento,
    'Club': clubes,
    'Federación': federaciones,
    'País': paises,
    'Tiempo': tiempos,
    'Viento': vientos
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)