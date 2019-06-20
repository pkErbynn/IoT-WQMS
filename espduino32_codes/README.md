# ProjectWQMS readme for the hardware sensors

Water  Quality Monitoring and Notification System
The project monitors physical aspects of water in a given system such as water level, turbidity,temperature and one chemical aspect; the pH of the water.
The WQMS features a web interface as an extra to the physical system.The system components include: 
1. Esp 12e V3.
2. Waterproof temperature sensor(DS18B20).
3. SKU SEN0189.
4.E-201-C pH meter.
The various components are neatly arranged and placed on a PCB. Esp 12e features a WIFI shield which is used to connect to the webserver for data collection
through Http client created on the Esp 12e.
The Esp 12e has a single analog pin, the project includes to sensors that require the use o f two analog pins.Thus,the ADS1115(16 bit I2C) is used to extend the Analog pins 
