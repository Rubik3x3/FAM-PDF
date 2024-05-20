import pandas as pd
import tabula

# Ruta al archivo PDF
pdf_path = "PDFs/2023/Resultados 16-09.pdf"

# Lee el PDF en un DataFrame
dfs = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

# Concatena todos los DataFrames en un solo DataFrame
df = pd.concat(dfs)

# Exporta el DataFrame a un archivo CSV
ruta_csv = "datos_extraidos.csv"
df.to_csv(ruta_csv, index=False)

print(f"Los datos han sido exportados correctamente a '{ruta_csv}'.")
