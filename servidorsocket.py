import socket
import sys
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('', 10000)
print >>sys.stderr, 'empezando a levantar %s puerto %s' % server_address
sock.bind(server_address)

st="ifconfig "+sys.argv[1]
os.system(st)

# Escuchando conexiones entrantes
# Pone al script en modo servidor
sock.listen(1)
 

while True:
    # Esperando conexion
    print >>sys.stderr, 'Esperando para conectarse'
    connection, client_address = sock.accept()
 
    try:
        print >>sys.stderr, 'concexion desde', client_address
 
        # Recibe los datos en trozos y reetransmite
        while True:
            data = connection.recv(1000)
            print >>sys.stderr, 'recibido "%s"' % data
            #if data:
             #   print >>sys.stderr, 'enviando confirmacion'
              #  connection.sendall("recivido")
            #else:
             #   print >>sys.stderr, 'no hay mas datos', client_address
              #  break
             
    finally:
        # Cerrando conexion
        connection.close()