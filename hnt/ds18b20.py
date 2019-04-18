
#!/usr/bin/env python
import os
import time
 
def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20
 
def read(ds18b20):
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit
 
def loop(ds18b20):
    while True:
        if read(ds18b20) != None:
            localtime = time.asctime( time.localtime(time.time()) )
            f = open("soilTempCollector.txt","a")
            print ("Soil temperature : %f C" % read(ds18b20)[0])
            f.write(str(localtime)+ '\t')
            f.write(str(read(ds18b20)[0])+ '\n')
            time.sleep(10)
            
            
          # print ("Current temperature : %0.3f F" % read(ds18b20)[1])
 
def kill():
    quit()
  
if __name__ == '__main__':
    try:
        serialNum = sensor()
        loop(serialNum)
    except KeyboardInterrupt:
        kill()
