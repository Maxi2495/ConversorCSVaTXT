import csv

archivo_entrada = 'datos.csv'
archivo_salida = 'datos.txt'

try:
    with open(archivo_entrada, mode='r', encoding='utf-8') as csv_file:
        lector_csv = csv.reader(csv_file, delimiter=',')
        
        with open(archivo_salida, mode='w', encoding='utf-8') as txt_file:
            escritor_txt = csv.writer(txt_file, delimiter='\t')
            
            for fila in lector_csv:
                # Prevencion 1: Ignora filas completamente vacías o que solo tienen comas
                if not fila or "".join(fila).strip() == "":
                    continue
                
                fila_limpia = []
                for celda in fila:
                    # Prevencion2: Quita espacios  al principio y al final de cada dato
                    dato = celda.strip()
                    
                    # Prevencion 3: Estandarizar decimales (Opcional)
                    # Si el dato tiene un punto y es un número, podríamos reemplazarlo por coma.
                    # Por ahora lo dejamos genérico, pero si Luminex te pide comas, activaríamos esto:
                    # if "." in dato y es numérico -> dato = dato.replace(".", ",")
                    
                    fila_limpia.append(dato)
                
                # Escribimos la fila ya procesada y limpia en el archivo de texto
                escritor_txt.writerow(fila_limpia)
                
    print(f"¡Éxito! El archivo '{archivo_entrada}' fue limpiado y convertido a '{archivo_salida}'.")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_entrada}'.")