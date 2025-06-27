registro =[]

#generos validos

generos_validos = ["f","femenino","m","masculino"]

def validar_contraseña(contraseña):
    return (
        len(contraseña) >= 8 and
        any(c.isalpha() for c in contraseña) and
        any(c.isdigit() for c in contraseña) and
        " " not in contraseña
    )

def ingresar_persona():
    nombre= input("ingrese nombre de la persona:").lower()

    if any(p["nombre"] == nombre for p in registro):
        print("nombre ya existente.")
        return
    
    contraseña=input("ingrese_contraseña: ")
    if not validar_contraseña(contraseña):
        print("contraseña inválido. Debe tener mínimo 8 caracteres, al menos una letra, un número y sin espacios.")
        return
    
    genero = input("Ingrese genero: ").lower()
    if genero not in generos_validos:
        print("los generos validos son F de femenino y M de masculino")
        return
    
    registro.append({
        "nombre":nombre,
        "contraseña":contraseña,
        "genero":genero
        })
    print("persona registrada con exitó")

def buscar_nombre():
    nombre = input("Ingrese nombre a buscar: ").lower()
    for p in registro:
        if p["nombre"] == nombre:
            print(f"la persona es: {p['genero']} y su contraseña es: {p['contraseña']}")
            return
    print("La persona no se encuentra.")

def eliminar_registro():
    nombre = input("Ingrese usuario a buscar: ").lower()
    for i, p in enumerate(registro):
        if p["nombre"] == nombre:
            del registro[i]
            print("Usuario eliminado con éxito!")
            return
    print("No se pudo eliminar usuario!")

def listar_nombres():
    if not registro:
        print("No hay nombres registrados.")
    else:
        for p in registro:
            print(f"Nombre: {p['nombre']} | genero: {p['generos']} | contraseña: {p['contraseña']}")

def main():
    while True:
        print("\nMENU PRINCIPAL")
        print("1.- Ingresar persona: ")
        print("2.- Buscar persona: ")
        print("3.- Eliminar persona: ")
        print("4.- Salir.")

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            ingresar_persona()
        elif opcion == "2":
            buscar_nombre()
        elif opcion == "3":
            eliminar_registro()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Debe seleccionar una opción válida.")

# Ejecutar el programa
if __name__ == "__main__":
    main()