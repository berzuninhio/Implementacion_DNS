import dns.resolver
import dns.reversename
import subprocess
def resolver_dominio():
    dominio = input("Ingresá el nombre de dominio (ej: www.google.com): ")
    try:
        respuesta = dns.resolver.resolve(dominio, "A")
        for rdata in respuesta:
            print(f"La IP de {dominio} es: {rdata.address}")
    except Exception as e:
        print(f"Error al resolver el dominio: {e}")
def resolver_ip():
    ip=input("Ingrese la ip: ")
    try: 
        rev_name = dns.reversename.from_address(ip)
        respuesta = dns.resolver.resolve(rev_name, "PTR")
        for rdata in respuesta: 
            dominio = str(rdata.target).rstrip(".")
            print(f"El dominio de {ip} es: {rdata.target}")
            hacer_nslookup(dominio)
    except Exception as e:
        print(f"Error al resolver el dominio: {e}")
def hacer_nslookup(direccion):
    print(f"\nEjecutando nslookup para {direccion}...\n")
    resultado = subprocess.run(["nslookup", direccion], capture_output=True, text=True)
    print(resultado.stdout if resultado.returncode == 0 else "❌ Error ejecutando nslookup")
    
resolver_dominio()
resolver_ip()