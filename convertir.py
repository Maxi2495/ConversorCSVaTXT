import csv
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

# Configuración oculta para que no se abra una ventana vacía de Tkinter
Tk().withdraw()

print("Por favor, selecciona el archivo CSV")

# Ventana flotante. Permite solo csv
ruta_archivo_entrada = askopenfilename(
    title="Seleccionar reporte CSV del laboratorio",
    filetypes=[("Archivos CSV", "*.csv")]
)

# Validacion si eligio archivo o cerro sin seleccionar nada
if ruta_archivo_entrada:
    
    # Genera automaticamente el nombre del archivo (.txt)
    # Mismo nombre, misma ruta pero diferente extension
    ruta_base, _ = os.path.splitext(ruta_archivo_entrada)
    ruta_archivo_salida = ruta_base + ".txt"
    
    try:
        with open(ruta_archivo_entrada, mode='r', encoding='utf-8') as csv_file:
            lector_csv = csv.reader(csv_file, delimiter=',')
            
            with open(ruta_archivo_salida, mode='w', encoding='utf-8') as txt_file:
                escritor_txt = csv.writer(txt_file, delimiter='\t')
                
                for fila in lector_csv:
                    if not fila or "".join(fila).strip() == "":
                        continue
                    
                    fila_limpia = [celda.strip() for celda in fila]
                    escritor_txt.writerow(fila_limpia)
                    
        # Nombre del archivo para mostrar por mensaje
        nombre_txt = os.path.basename(ruta_archivo_salida)
        messagebox.showinfo("Proceso Terminado", f"¡Éxito!\nSe generó el archivo de texto: '{nombre_txt}'")
        print("Lo encontrarás guardado en la misma carpeta donde estaba tu archivo original.")

    except Exception as e:
        print(f"\nOcurrió un error inesperado al procesar el archivo: {e}")
else:
    print("\nOperación cancelada. No se seleccionó ningún archivo.")

