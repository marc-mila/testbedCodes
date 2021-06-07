import os
import sys

os.system('python /home/pi/testbed-v2/Scenario-IoTs/TrafficLight/gestion_semaforos.py ip=' + sys.argv[1] + ' port=5000 & python /home/pi/testbed-v2/Scenario-IoTs/StreetLight/gestion_farolas.py ip=' + sys.argv[1] + ' port=5002 & python /home/pi/testbed-v2/Scenario-IoTs/Traffic/gestion_trafico.py ip='+ sys.argv[1] + ' port=5004')
