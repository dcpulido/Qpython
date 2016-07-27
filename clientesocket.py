#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Cliente
# www.pythondiario.com
 
import socket
import sys
import time
import androidhelper
import os
 

ip_defecto="127.0.0.1"
puerto_defecto="10000"
ip_defecto_pokemon=""
puerto_defecto_pokemon=""
# Creando un socket TCP/IP
droid=androidhelper.Android()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con=False
ip=""
# Conecta el socket en el puerto cuando el servidor esté escuchando

wifi_info=""
gps_info=""
#Aplicacion de uso
flag=True
while flag:
	print "\n"
 	print "APP CLIENTE"
	print "0_Escaneo wifi"
	print "1_Escaneo gps"
	print "2_Enviar Informacion a server"
	print "3_Escaneo Pokemon"
	print "4_Cerrar aplicacion"
	op=input()
	

	if op==0:
		if droid.checkWifiState().result == True:
			os.system("clear")
			resultados=droid.wifiGetConnectionInfo()
			res=resultados[1]
			print "CONEXION ACTUAL"
			print time.strftime("%I:%M:%S")
			wifi_info+=str.format("{0}\n",time.strftime("%I:%M:%S"))
			wifi_info+=str.format("ssid: {0}    ip_addres: {1} \n",res["ssid"],res["ip_address"]) 
			print str.format("ssid: {0}    ip_addres: {1}",res["ssid"],res["ip_address"]) 
			print "\n"

			print "ESCANEADO"
			escaneos = droid.wifiGetScanResults()
			scan=escaneos[1]
			y=0
			for sc in scan:
				wifi_info+=str.format("{0}, {1}, {2}\n",y,sc["ssid"],sc["capabilities"]) 
				print str.format("{0}, {1}, {2}",y,sc["ssid"],sc["capabilities"]) 
				y=y+1

			wifi_info+="::::\n"
	if op==1:
		droid.startLocating()
		y=0
		print"ESCANEANDO GPS\n"
		while y<10:
			sys.stdout.write('.')
			time.sleep(1)
			y=y+1

		l = droid.readLocation()
		try:
			print "\n"
			print "GPS"
			R =l.result
			R =R["gps"]
			Lat= R["latitude"]
			Lon=R["longitude"]
			outstr = str(Lat) +","+ str(Lon)
			print outstr
		except:
			pass
		try:
			print "\n"
			print "NETWQORK"
			R1 =R["network"]
			Lat1=R1["latitude"]
			Lon1=R1["longitude"]
			outstr = str(Lat1) +","+ str(Lon1)
			print outstr

		except:
			pass
	if op==2:
		try:

			os.system("clear")
			if con==False:
				if len(sys.argv)==1:
					if ip=="":
						ip=raw_input("introduce la ip ")
						puerto=input("puerto")
				else:
					ip=sys.argv[1]
				if ip=="":
					ip=ip_defecto_pokemon
				if puerto=="":
					puerto=puerto_defecto_pokemon
				server_address = (ip, puerto)

				print >>sys.stderr, 'conectando a %s puerto %s' % server_address
				sock.connect(server_address)
				con=True

			message = wifi_info
			print >>sys.stderr, 'enviando "%s"' % message
			sock.sendall(message)
		finally:
			pass

	if op==3:
		droid.startLocating()
		print"ESCANEANDO GPS\n"
		y=0
		while y<10:
			sys.stdout.write('.')
			time.sleep(1)
			y=y+1

		l = droid.readLocation()
		pos=""
		try:
			print "\n"
			print "GPS"
			R =l.result
			R =R["gps"]
			Lat= R["latitude"]
			Lon=R["longitude"]
			pos = str(Lat) +","+ str(Lon)

		except:
			pass
		try:
			print "\n"
			print "NETWQORK"
			R1 =R["network"]
			Lat1=R1["latitude"]
			Lon1=R1["longitude"]
			pos = str(Lat1) +","+ str(Lon1)
		except:
			pass

		if pos!="":
			print pos
		else:
			print "mala lectura gps"

		try:

			os.system("clear")
			if con==False:
				if len(sys.argv)==1:
					if ip=="":
						ip=raw_input("introduce la ip ")
						puerto=input("puerto")
				else:
					ip=sys.argv[1]

				if ip=="":
					ip=ip_defecto_pokemon
				if puerto=="":
					puerto=puerto_defecto_pokemon
				server_address = (ip, puerto)

				print >>sys.stderr, 'conectando a %s puerto %s' % server_address
				sock.connect(server_address)
				con=True

			message = "P"+pos
			print >>sys.stderr, 'enviando "%s"' % message
			sock.sendall(message)	
	if op==4:
		flag=False

print >>sys.stderr, 'cerrando socket'
sock.close()
