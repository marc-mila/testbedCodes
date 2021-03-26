import os
import sys
import subprocess
import shlex

#comprovar si existeix fitxers

cmd1 = 'python /home/pi/testbed-v2/Scenario-IoTs/TrafficLight/gestion_semaforos.py ip=' + sys.argv[1] + ' port=5000' 
cmd2 = 'python /home/pi/testbed-v2/Scenario-IoTs/StreetLight/gestion_farolas.py ip=' + sys.argv[1] + ' port=5002'
cmd3 = 'python /home/pi/testbed-v2/Scenario-IoTs/Traffic/gestion_trafico.py ip=' + sys.argv[1] + ' port=5004'

subprocess.Popen(shlex.split(cmd1), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.Popen(shlex.split(cmd2), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.Popen(shlex.split(cmd3), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

