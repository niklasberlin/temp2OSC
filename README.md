# temp2OSC
This script will continously read the CPU Temperature of an RaspberryPi and send it to an instance of Companion by Bitfocus [1]. At the beginning of the file are some variables to configure IP-address and port of the companion instance as well as the page and button on which the temperature should be displayed. At defined thresholds (default 60°C) the background-color will be set to orange and at another treshold (75°C) the background-color will be turned red, otherwise the background will be black(all colors can be configured at the beginning of the script).

## installing needed tools

To run this script you need to have python3 installed, to do so use the following command:
> sudo apt-get install python3

To install the used libraries pip is used, therefor we need to install pip:
> sudo apt-get install pip3

Now you can install the used libraries, for OSC Python-OSC [2] is used:
> pip3 install python-osc

To get the temperature the gpiozero [3] library is used:
> pip3 install gpiozero

## Configure the script

By Default the script assumes that it runs on the same pi as companion and that the CPU Temperature should be displayed on button 21 on page 99 (bottom right Button on the last page of a 15-key streamdeck), if this is OK for you, you can skip this step.

To change the page change the following line
> targetPage = 99

To change the button change the following line
> targetButton = 21

If companion does not run on the same raspberryPi you can define the IP of the companion computer in the following line:
> targetIP = "127.0.0.1"

## run the script

to start the script navigate to the folder with the script and type:
> python3 temp2OSC.py

if you want to run it in the background use this:
> python3 temp2OSC.py &

## enable auto start

This step is based on the instructions on how to auto start companion on a Linux system [4]

first we need to create a UNIT-File at /etc/systemd/system/temp2osc.service
> sudo nano /etc/systemd/system/temp2osc.service
copy the below code into this file, adjust the path to the script depending on your setup and save the file
> [Unit]
> Description=Temp2OSC
> After=network-online.target
> Wants=network-online.target
> 
> [Service]
> Type=simple
> User=pi
> WorkingDirectory=/home/pi/scripts
> ExecStart=python3 /home/pi/scripts/temp2OSC.py
> Restart=on-failure
> KillSignal=SIGINT
> TimeoutStopSec=60
> 
> [Install]
> WantedBy=multi-user.target

now we need to enable this service with the following command
> sudo systemctl enable temp2osc.service

and after this we reboot
> sudo reboot

###### Links
[1] Companion: https://bitfocus.io/companion/  
[2] Python-OSC: https://pypi.org/project/python-osc/  
[3] gpiozero: https://github.com/gpiozero/gpiozero  
[4] https://github.com/bitfocus/companion/wiki/Auto-Start-Companion-on-Linux-Using-systemd
