#!/bin/bash



ip=$1

chmod 777 /home/pi/testbedCodes/ 
mkdir /home/pi/testbed-v2
mkdir /home/pi/testbed-v2/Scenario-IoTs
mkdir /home/pi/testbed-v2/Scenario-IoTs/TrafficLight
mkdir /home/pi/testbed-v2/Scenario-IoTs/Traffic
mkdir /home/pi/testbed-v2/Scenario-IoTs/StreetLight
cp /home/pi/testbedCodes/util.py /home/pi/testbed-v2/Scenario-IoTs/TrafficLight/
cp /home/pi/testbedCodes/util.py /home/pi/testbed-v2/Scenario-IoTs/Traffic/
cp /home/pi/testbedCodes/util.py /home/pi/testbed-v2/Scenario-IoTs/StreetLight/
cp /home/pi/testbedCodes/gestion_semaforos.py /home/pi/testbed-v2/Scenario-IoTs/TrafficLight/
cp /home/pi/testbedCodes/gestion_farolas.py /home/pi/testbed-v2/Scenario-IoTs/StreetLight/
cp /home/pi/testbedCodes/gestion_trafico.py /home/pi/testbed-v2/Scenario-IoTs/Traffic/

echo "Testbed engegat"



