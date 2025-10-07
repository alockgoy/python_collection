# Pequeño script para hacer de Wake-On-Lan

# Es necesario previamente ejecutar este comando en tu S.O.: pip install wakeonlan

# Importar la librería necesaria
from wakeonlan import send_magic_packet

# Dispositivo(s) a "despertar"
dispositivos = {
   'pc':{'mac':'mac','ip_address':'192.168.1.255'}
}

# Función para mandar el paquete
def despertar_dispositivo(nombre_dispositivo):
   if nombre_dispositivo in dispositivos:
      mac,ip = dispositivos[nombre_dispositivo].values()
      send_magic_packet(mac, ip_address=ip)
      print('Paquete mágico enviado')
   else:
      print('Dispositivo no encontrado')
      
# Ejecutar la función
despertar_dispositivo("pc")