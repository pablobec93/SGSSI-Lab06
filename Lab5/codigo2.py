import hashlib
import random
import time

def generar_linea_adicional(identificador_estudiante):
    """Genera una línea adicional según las instrucciones"""
    secuencia_hexadecimal = ''.join(random.choices('abcdef', k=8))
    return f"{secuencia_hexadecimal}\t{identificador_estudiante}\t100"

def get_sha256_of_file(file_path):
    """Calcula el hash SHA-256 de un archivo"""
    hash_obj = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # leer en bloques de 64k
            if not data:
                break
            hash_obj.update(data)
    return hash_obj.hexdigest()

def cantidad_ceros_al_inicio(s):
    """Retorna la cantidad de ceros al inicio de una cadena"""
    return len(s) - len(s.lstrip('0'))

def main():
    identificador_estudiante = input("Introduce el identificador público del estudiante (dos caracteres hexadecimales en minúscula): ")
    
    with open('SGSSI-23.CB.02.txt', 'r') as f:
        contenido_original = f.read()
    
    archivo_modificado_path = 'SGSSI-23.CB.02_modificado.txt'
    mejor_cantidad_de_ceros = 0
    mejor_hash = ''
    fin_tiempo = time.time() + 60  # Establecer un límite de 1 minuto para la ejecución

    while time.time() < fin_tiempo:
        # Generar la línea adicional y añadirla al contenido modificado
        linea_adicional = generar_linea_adicional(identificador_estudiante)
        contenido_modificado = contenido_original + '\n' + linea_adicional  # Añado el '\n' antes de la línea adicional
        
        with open(archivo_modificado_path, 'w') as f:
            f.write(contenido_modificado)

        # Calcula el hash SHA-256 del archivo recién escrito
        hash_del_archivo = get_sha256_of_file(archivo_modificado_path)
        ceros_actuales = cantidad_ceros_al_inicio(hash_del_archivo)

        # Si el hash actual tiene más ceros al principio que el mejor hash encontrado hasta ahora, actualizar el mejor hash
        if ceros_actuales > mejor_cantidad_de_ceros:
            mejor_cantidad_de_ceros = ceros_actuales
            mejor_hash = hash_del_archivo

    print(f"Archivo modificado guardado como 'SGSSI-23.CB.02_modificado.txt'. SHA-256: {mejor_hash}")

if __name__ == "__main__":
    main()
