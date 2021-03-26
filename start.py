import os
import sys
import subprocess
import shlex

#comprovar si existeix fitxers

cmd1 = 'python /home/pi/testbed-v2/Scenario-IoTs/TrafficLight/gestion_semaforos.py ip=' + sys.argv[1] + ' port=5000' 
cmd2 = 'python /home/pi/testbed-v2/Scenario-IoTs/StreetLight/gestion_farolas.py ip=' + sys.argv[1] + ' port=5002'
cmd3 = 'python /home/pi/testbed-v2/Scenario-IoTs/Traffic/gestion_trafico.py ip=' + sys.argv[1] + ' port=5004'


command = (os.path.exists('/home/pi/testbed-v2/Scenario-IoTs/TrafficLight/gestion_semaforos.py') and 
os.path.exists('/home/pi/testbed-v2/Scenario-IoTs/StreetLight/gestion_farolas.py') and 
os.path.exists('/home/pi/testbed-v2/Scenario-IoTs/Traffic/gestion_trafico.py'))


if command:
    os.system('python /home/pi/testbed-v2/Scenario-IoTs/TrafficLight/gestion_semaforos.py ip=' + sys.argv[1] + ' port=5000 & python /home/pi/testbed-v2/Scenario-IoTs/StreetLight/gestion_farolas.py ip=' + sys.argv[1] + ' port=5002 & python /home/pi/testbed-v2/Scenario-IoTs/Traffic/gestion_trafico.py ip=' + sys.argv[1] + ' port=5004')
else:
    estan=False
    print 'no estan'
    while not estan:
	if command:
	    estan=true
	    os.system('python /home/pi/testbed-v2/Scenario-IoTs/TrafficLight/gestion_semaforos.py ip=' + sys.argv[1] + ' port=5000 & python /home/pi/testbed-v2/Scenario-IoTs/StreetLight/gestion_farolas.py ip=' + sys.argv[1] + ' port=5002 & python /home/pi/testbed-v2/Scenario-IoTs/Traffic/gestion_trafico.py ip=' + sys.argv[1] + ' port=5004')

