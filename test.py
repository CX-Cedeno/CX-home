import os

def read_file(filename):
    # Vulnerabilidad de path traversal
    with open(filename, 'r') as f:
        return f.read()

def insecure_password_storage(password):
    # Almacenamiento inseguro de contraseñas
    with open('passwords.txt', 'a') as f:
        f.write(password + '\n')

def main():
    filename = input("Ingrese el nombre del archivo a leer: ")
    
    # Se asume que el archivo ya existe en el mismo directorio
    try:
        content = read_file(filename)
        print("Contenido del archivo:")
        print(content)
    except FileNotFoundError:
        print("Archivo no encontrado.")

    password = input("Ingrese su contraseña: ")
    insecure_password_storage(password)
    print("Contraseña almacenada.")

if __name__ == "__main__":
    main()
