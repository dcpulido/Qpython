import socket
import sys
import os


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('', 10000)

flag=True
while flag:
    print "\n"
    print "APP CLIENTE"
    print "0_levantar escucha"
    op=input()


    if op==0:   
        print >>sys.stderr, 'empezando a levantar %s puerto %s' % server_address
        sock.bind(server_address)
        st="ifconfig "+sys.argv[1]
        os.system(st)
        sock.listen(1)

        toret=""
        print >>'Esperando para conectarse'
        connection, client_address = sock.accept()
        try:
            toret+=str.format("concexion desde {0} \n",client_address)
            print >>sys.stderr, 'concexion desde', client_address
            while True:
                data = connection.recv(1000)
                toret += str.format("{0}",data)
                print >>sys.stderr, 'recibido "%s"' % data
                if data:
                    print >>sys.stderr, 'enviando confirmacion'
                    connection.sendall("recivido")
                    if toret[len(toret)-3:len(toret)]=="FIN":
                        print "envio finalizado"
                        print toret
                        break
                else:
                    print >>sys.stderr, 'no hay mas datos', client_address
                    print toret
                    break
                 
        finally: 
            outfile = open('salida.txt', 'w') # Indicamos el valor 'w'.
            outfile.write(toret)
            outfile.close()      
            connection.close() 
    if op==4:
        flag=False    
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)



