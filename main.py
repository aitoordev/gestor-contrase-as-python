import json
import os

print("--------------------------")
print(" GESTOR DE CONTRASEÑAS")
print("--------------------------")

print("[1] - Guardar una contraseña")
print("[2] - Ver una contraseña")

opcion = int(input("Que opcion quieres?"))


if opcion == 1:
    os.system("cls")
    
    guardarapp = input("Para que app es la contraseña?: ")
    guardarmail = input("Tu email: ")
    guardaruser = input ("Tu nombre de usuario: ")
    guardarcontra = input("Contraseña a guardar: ")

    datos = {
    "App": guardarapp,
    "Correo": guardarmail,
    "Nombre": guardaruser,
    "Contraseña": guardarcontra,
    }


    with open("contraseñas.json" , "w")as archivo:
        json.dump(datos,archivo,indent=4)


elif opcion == 2:
   with open("contraseñas.json" , "r")as archivo:
    resultado = json.load(archivo)

    print(resultado)

else:
   print("Opcion no valida")