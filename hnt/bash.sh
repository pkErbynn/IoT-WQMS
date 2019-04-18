#!/bin/sh


#the statement below puts the temp from ming and puts it into lov.
#it is form the lov that we will feed the flask app with

#similar implementation can be done for the other columns and the other sensors

while true;do
    echo "Reading Temp"
    tail -20 collector.txt | awk '{printf substr($4,1,5) " \t"  $6 " \n"}' > ./readings/atmp1h.embs
    tail -20 soilTempCollector.txt | awk '{printf substr($4,1,5) " \t"  $6 " \n"}' > ./readings/stmp1h.embs 
    tail -20 humidityCollector.txt | awk '{printf substr($4,1,5) " \t"  $6 " \n"}' > ./readings/humidity1h.embs 
    sleep 60
done
