#-*-coding:utf8;-*-
#qpy:2
#qpy:console
 
print "This is a gps app"
 
import androidhelper, time
droid = androidhelper.Android()
droid.startLocating()
time.sleep(30)
c = 0
while c<50:
 
  l = droid.readLocation()
  R =l.result
  try:
    R =R["gps"]
    Lat= R["latitude"]
    Lon=R["longitude"]
    #R1 =R["network"]
    #Lat1=R1["latitude"]
    #Lon1=R1["longitude"]
    outstr = str(Lat) +","+ str(Lon)
    droidfile = '/sdcard/posiciones.txt'
    print outstr#, str(Lat1) , str(Lon1)
    fh = open(droidfile,'a')
    res= fh.write(outstr +'\n' )
    res = fh.close()
    time.sleep(10)
    c+=1
    print c
  except:
    time.sleep(10)
    print c
    print R
    c+=1