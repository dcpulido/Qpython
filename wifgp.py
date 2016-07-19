import androidhelper
import time
import os
droid=androidhelper.Android()

print "aplicacion de prueba"

if droid.checkWifiState().result == True:
	resultados=droid.wifiGetConnectionInfo()
	res=resultados[1]
	print "CONEXION ACTUAL"
	print str.format("ssid: {0}    ip_addres: {1}",res["ssid"],res["ip_address"]) 
	print "\n"

	print "ESCANEADO"
	escaneos = droid.wifiGetScanResults()
	scan=escaneos[1]
	y=0
	for sc in scan:
		print str.format("{0}, {1}, {2}",y,sc["ssid"],sc["capabilities"]) 
		y=y+1

	print "POSICION"
	while 1:
		posicion=droid.readLocation()
		print posicion
		print posicion.result
		os.system("clear")
		time.sleep(2)
