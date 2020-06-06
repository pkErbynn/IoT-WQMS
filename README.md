# IoT-Based Water Quality Monitoring System(WQMS) for Aquaculture.



#### The purpose of this project is to design and implement a portable and low-cost water monitoring system to consistently monitor the status of water to be quality and conducive for fish farming in aquaponic tanks at the aquaculture sector.

- Since the composition of pond water is continuously affected by environmental changes making it difficult for the farmers to consistently monitor the status of water therefore our WQMS was developed to monitor the variations.
- Water quality test can be done at source other than shipping water samples to laboratory reducing traditional laboratory testing.
Why our system is different from other systems:
    1. Measures the temperature, turbidity, pH and water level, of the pond to maintain and control the water quality.
    2. Quickly identifies specific parameter change in water
    3. Generates visual information(line chart)
    4. Sends notification alert

## System operation
- Measures water temperature, depth, turbidityand pH of water with optimum ranges
            Turbidity(Nephelometric Turbidity Units or Jackson Turbidity Unit) 0-5
            pH  4-10
            Water level 5-27 (based on site)
- Processes data on microcontroller using Espduino#2 
- Sends data to cloud sever 
- And publishes the data on webpage 

## Hardware Implementation
- Espduino-32
- Waterproofed temperature sensor DS18B20
- pH sensor- E-201-C
- Turbidity Sensor- SKU SEN0189
- Ultrasonic Sensor- HC-SR04

## Software Implementation
- Front-end
    - HTML/CSS/ 
    - Bootstrap
    - Jinja
    - Chartjs
- Backend
    - Python: logic
    - Flask: server
    - SMTP: messaging 
    - SQLite: DB
    - C program: sensor program on Esp32
    - HTTP
    - Heroku
   
   
 ## Getting Started
 ### Prerequisites
 - Clone repo
 - Add Esp32 packages to enable board  
 - Sensor codes link at
    ```
       github.com/joewzy/WaterQualityMS.git
    ```
 
 ### Installation
 - Install modules in requirement file 


## Usage:
 1. Connect esp32 to network
 2. Clone the repository::
   ```
   git clone https://github.com/Erbynn/IoT-WQMS.git
        cd IoT-WQMS
   ```
 3. Create and activate a virtual environment::
    ```
    virtualenv env
        source env/bin/activate
    ```
  4. Install requirements::
   
    pip install -r 'requirements.txt'
        
  5. Run the application::
     ```
        python app.py
     ```
        
  6. Data is published on [http://wqms.herokuapp.com/dashboard](wqms.herokuapp.com/dashboard)

  6. Enjoy :+1:
 
 ## Sample Images
 ![](images/fullsetup.png)
  
  
## Authors/Team::
   - John PK Erbynn [send mail](john.erbynn@gmail.com)
   - Josiah Kotey [send mail](josiahkotey13@gmail.com)
   - Isaac Agyen Duffour [Send mail](izagyen96@gmail.com)
   
## Acknoledgement
   - Project Supervisor, Mr. Isaac A. Mensah
   - Denis Effa Amposah
   - Dawud Ismail
   - Josiah Terkper
  
 ## Deployment 
This extension is a project to improve our software development skills. Any suggestions, or tips as well as Pull Requests are welcome.
Thank you.


   



