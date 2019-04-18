import smbus
import time

counter = 1
while(counter ==1 ):
        bus = smbus.SMBus(1)
        bus.write_byte(0x40, 0xF5)

        time.sleep(0.3)

        data0 = bus.read_byte(0x40)
        data1 = bus.read_byte(0x40)

        humidity = ((data0 * 256 + data1)*125 / 65536.0)-6
        localtime = time.asctime( time.localtime(time.time()) )
        f = open("humidityCollector.txt","a")
        print('Humidity is %f%%'%(humidity))
        f.write(str(localtime)+ '\t')
        f.write(str(humidity)+'\n')
        time.sleep(1)


