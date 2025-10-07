# Importar las cosas necesarias
import os 
import time

# Definir la IP del NAS
ip = "192.168.1.90"

# Variable de contador
error = 0

# Bucle
while True:
    # Hacer ping al servidor
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")

    if response == 0:
        # Si responde, reiniciar el conteo de errores y esperar 1 minuto
        print(f"El servidor {ip} está en línea.")
        error = 0
        time.sleep(60)
    else:
        # Si no responde, incrementar el conteo de errores
        print(f"El servidor {ip} no responde. Error {error + 1}")
        error += 1

        # Si hay 2 errores consecutivos, cerrar los servicios y apagar el sistema
        if error >= 2:
            print("El servidor no responde, cerrando servicios y apagando el sistema.")
            os.system("sudo systemctl stop plexmediaserver")
            os.system("sudo systemctl stop jellyfin")
            os.system("shutdown")
            break
        else:
            # Esperar 1 minuto antes de volver a intentar
            time.sleep(60)