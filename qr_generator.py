# Generador de códigos QR con python

# Tener la librería previamente instalada en el SO, el comando es: pip install qrcode[pil]

# Importar la librería
import qrcode

# Variable con el dato a convertir
dato = "https://short.do/67U3sD"

# Generar el qr
qr = qrcode.make(dato)

# Guardar la imagen (atención, se guarda en la carpeta en que se ejecuta el script)
qr.save("codigo.png")