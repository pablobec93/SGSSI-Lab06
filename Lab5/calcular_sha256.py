# Esto es de Ramirín
import hashlib

def calcular_sha256(archivo_path):
    """Calcula el hash SHA-256 de un archivo."""
    sha256 = hashlib.sha256()
    
    with open(archivo_path, 'rb') as f:  # 'rb' para leer en modo binario
        while True:
            bloque = f.read(65536)  # leer en bloques de 64k
            if not bloque:
                break  # salir del bucle si hemos llegado al final del archivo
            sha256.update(bloque)

    return sha256.hexdigest()

def main():
    archivo_path = input("Introduce la ruta del archivo para calcular su SHA-256: ")
    hash_resultado = calcular_sha256(archivo_path)
    print(f"SHA-256 del archivo {archivo_path}: {hash_resultado}")

if __name__ == "__main__":
    main()
