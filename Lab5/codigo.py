import hashlib
import random

def generar_linea_adicional(identificador_estudiante):
    """Genera una línea adicional según las instrucciones"""
    secuencia_hexadecimal = ''.join(random.choices('abcdef', k=8))
    return f"{secuencia_hexadecimal}\t{identificador_estudiante}\t100"

def cumple_requisito_SHA256(hash_val):
    """Verifica si el hash SHA-256 comienza con el carácter hexadecimal “0”"""
    return hash_val[0] == "0"

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

def main():
    identificador_estudiante = input("Introduce el identificador público del estudiante (dos caracteres hexadecimales en minúscula): ")
    
    with open('SGSSI-23.CB.02.txt', 'r') as f:
        contenido_original = f.read()
    
    archivo_modificado_path = 'SGSSI-23.CB.02_modificado.txt'

    while True:
        # Generar la línea adicional y añadirla al contenido modificado
        linea_adicional = generar_linea_adicional(identificador_estudiante)
        contenido_modificado = contenido_original + '\n' + linea_adicional  # Añado el '\n' antes de la línea adicional para separarla del contenido original
        
        with open(archivo_modificado_path, 'w') as f:
            f.write(contenido_modificado)

        # Calcula el hash SHA-256 del archivo recién escrito
        hash_del_archivo = get_sha256_of_file(archivo_modificado_path)

        # Verificar si cumple el requisito
        if cumple_requisito_SHA256(hash_del_archivo):
            break
    
    print(f"Archivo modificado guardado como 'SGSSI-23.CB.02_modificado.txt'. SHA-256: {hash_del_archivo}")

if __name__ == "__main__":
    main()
