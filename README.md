# Simulación y Resolución DNS – Packet Tracer + Python

Este proyecto demuestra el funcionamiento de un servidor DNS mediante dos implementaciones distintas:

1. Una simulación en Cisco Packet Tracer.
2. Un script en python que resuelve nombres de dominio y direcciones IP.

Contenido del proyecto

- `servidor_dns.pkt`: archivo de Cisco Packet Tracer que simula una red local con un servidor DNS.
- `ImplementacionDNS.py`: script en Python para resolver dominios e IPs usando la librería dnspython.
  
---

1. Simulación en Cisco Packet Tracer

En el archivo servidor_dns.pkt se encuentra una red compuesta por:

- Un Servidor configurado con servicio DNS y HTTP.
- Una PC configurada con IP y DNS apuntando al servidor.
- Un Switch para interconectar los dispositivos.

Funcionamiento:
La PC puede resolver un nombre de dominio configurado (www.ejemplo.com) usando el servidor DNS de la red. Esto se prueba mediante el comando ping en la terminal.
El servidor tiene activo el servicio HTTP, con una pagina HTML cargada. Desde la PC se puede abrir el Web Browser e ingressar: www.ejemplo.com

---

Script en Python – Resolución de dominios reales

El archivo ImplementacionDNS.py permite:

- Ingresar un dominio (ej: www.google.com) y obtener su IP (registro tipo A).
- Ingresar una IP y obtener el dominio asociado (registro tipo PTR).
- Ejecutar un nslookup para mostrar más información del dominio.

Requisitos:
En la terminal de python
pip install dnspython nslookup
