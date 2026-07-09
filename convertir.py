import csv

#Nombres de archivos
archivo_entrada = 'datos.csv'
archivo_salida = 'datos.txt'

try:
    #Abre el archivo CSV para leerlo
    with open(archivo_entrada, mode='r', encoding='utf-8') as csv_file:
        # Uso "mode=r" para leer. El "reader" interpreta el archivo usando la coma como separador
        lector_csv = csv.reader(csv_file, delimiter=',')
        
        # Apertura del archivo .txt para escribir
        with open(archivo_salida, mode='w', encoding='utf-8') as txt_file:
            # modo "w" es 'writer'. Escribirá en el TXT usando tabulaciones (\t)
            escritor_txt = csv.writer(txt_file, delimiter='\t')
            
            #Iteracion fila por fila y la escritura en el nuevo formato
            for fila in lector_csv:
                escritor_txt.writerow(fila)
                
    print(f"¡Éxito! El archivo '{archivo_entrada}' se convirtió a '{archivo_salida}'.")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_entrada}' en esta carpeta.")