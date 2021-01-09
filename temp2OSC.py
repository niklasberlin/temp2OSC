# -*- coding: utf-8 -*-

from pythonosc import udp_client
from gpiozero import CPUTemperature
import time

# Network config of the companion instance that should display the CPU Temp 
targetIP = "127.0.0.1"  
targetPort = 12321
targetPage = 99  # page in companion that will display the CPU Temp
targetButton = 21 # button in companion that will display the CPU Temp

tempWarning = 60 # threshold for warning background color
tempAlert = 75 # threshold for Alert background color

bgWarning = [255, 100, 0] #color for warning
bgAlert = [255, 0, 0] #color for alert
bgNormal = [0, 0, 0] #color for normal operation

########################################
#
#   No changes needed beyond this Point
#
########################################


#create client
companion = udp_client.SimpleUDPClient(targetIP, targetPort)

OSCaddressText = '/style/text/'+str(targetPage)+'/'+str(targetButton)
OSCaddressBG = '/style/bgcolor/'+str(targetPage)+'/'+str(targetButton)
while True:
    #get CPU temp
    cpuTemp = CPUTemperature().temperature
    if (cpuTemp > tempAlert):
        companion.send_message(OSCaddressBG, bgAlert)
    elif (cpuTemp > tempWarning):
        companion.send_message(OSCaddressBG, bgWarning)
    else:
        companion.send_message(OSCaddressBG, bgNormal)


    ButtonText = "CPU Temp "+str(cpuTemp)[:-1] + " °C"
    companion.send_message(OSCaddressText, ButtonText)
    time.sleep(1) #sleep for one second


