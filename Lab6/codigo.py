import hashlib
import os

def es_hexadecimal(s):
    """Verifica si una cadena es hexadecimal"""
    return all(c in '0123456789abcdef' for c in s)

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
    # Leer el fichero de entrada
    with open('SGSSI-23.CB.03.txt', 'r') as f:
        contenido_original = f.read()
    
    directorio = 'SGSSI-23.S.6.2.CB.03.Candidatos'
    ficheros = os.listdir(directorio)
    
    mejor_cantidad_de_ceros = 0
    mejor_fichero = ''
    
    for fichero in ficheros:
        with open(os.path.join(directorio, fichero), 'r') as f:
            contenido = f.read()
        
        ultima_linea = contenido.split('\n')[-1]
        partes = ultima_linea.split('\t')
        
        # Comprobar las condiciones
        if contenido.startswith(contenido_original) and \
           len(partes) == 3 and \
           len(partes[0]) == 8 and es_hexadecimal(partes[0]):
            hash_del_fichero = get_sha256_of_file(os.path.join(directorio, fichero))
            ceros_actuales = cantidad_ceros_al_inicio(hash_del_fichero)
            print(f"Fichero: {fichero}, Ceros al inicio: {ceros_actuales}")

            # Actualizar el mejor fichero si es necesario
            if ceros_actuales > mejor_cantidad_de_ceros:
                mejor_cantidad_de_ceros = ceros_actuales
                mejor_fichero = fichero

    print(f"El fichero con la mayor secuencia de ceros es: {mejor_fichero}")

if __name__ == "__main__":
    main()
