# coding=utf-8
# !/usr/bin/python3
import os
import time


def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input(":--------------: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


salir = False
opcion = 0

while not salir:

    print(" 1. Registrar Cuenta")
    print(" 2. Eliminar Cuenta")
    print(" 3. Buscar Presencia")
    print(" 4. Enviar Mensaje")
    print(" 5. Iniciar Chat")
    print(" 6. Entrar a Conferencia")
    print(" 7. Enviar Archivos")
    print(" 8. Recibir Archivos")
    print(" 9. Set Avatars")
    print("10. Download Avatar ")
    print("11. Migrar Roster ")
    print("12. Ping JID ")
    print("13. Salir")

    print ("Protocolo XMPP")


    opcion = pedirNumeroEntero()
    os.system("cls")
    if opcion == 1:
        print ("Registrar Cuenta")
        os.system("/Users/Saucer/PycharmProjects/final/registrar_cuenta_01.py")
        os.system("Pause")
        time.sleep(3)
        os.system("cls")
    elif opcion == 2:
        print ("Eliminar Cuenta")
        os.system("/Users/Saucer/PycharmProjects/final/eliminar_cuenta_01.py")
        os.system("Pause")
        time.sleep(3)
        os.system("cls")
    elif opcion == 3:
        print("Buscar Presencia")
        os.system("/Users/Saucer/PycharmProjects/final/buscar_presencia.py")
        os.system("Pause")
        time.sleep(3)
        os.system("cls")
    elif opcion == 4:
        print("Enviar Mensaje")
        os.system("/Users/Saucer/PycharmProjects/final/send_client_01.py")
        os.system("Pause")
        time.sleep(3)
        os.system("cls")
    elif opcion == 5:
        print("Iniciar Chat")
        os.system("/Users/Saucer/PycharmProjects/final/iniciar_sesion_y_chat_01.py")
        os.system("Pause")
        time.sleep(3)
        os.system("cls")
    elif opcion == 6:
        print("Entrar a Conferencia")
        os.system("/Users/Saucer/PycharmProjects/final/muc_chat_01.py")
        os.system("Pause")
        time.sleep(3)
        os.system("cls")
    elif opcion == 7:
        print("Enviar Archivo")
        os.system("/Users/Saucer/PycharmProjects/final/file_sender.py")
        os.system("Pause")
        time.sleep(3)
        os.system("cls")
    elif opcion == 8:
        print("Recibir Archivo")
        os.system("/Users/Saucer/PycharmProjects/final/file_receiver.py")
        os.system("Pause")
        time.sleep(3)
        os.system("cls")
    elif opcion == 9:
        print("Set Avatar")
        os.system("/Users/Saucer/PycharmProjects/final/set_avatar.py")
        os.system("Pause")
        time.sleep(3)
        os.system("cls")
    elif opcion == 10:
        print("Download Avatar")
        os.system("/Users/Saucer/PycharmProjects/final/download_avatars.py")
        os.system("Pause")
        time.sleep(3)
        os.system("cls")
    elif opcion == 11:
        print("Migrar Roster")
        os.system("/Users/Saucer/PycharmProjects/final/migrate_roster.py")
        os.system("Pause")
        time.sleep(3)
        os.system("cls")
    elif opcion == 12:
        print("Ping JID")
        os.system("/Users/Saucer/PycharmProjects/final/ping.py")
        os.system("Pause")
        time.sleep(3)
        os.system("cls")
    elif opcion == 13:
        salir = True
    else:
        print("Introduce un numero entre 1 y 3")

print("Fin")
os.system("cls")