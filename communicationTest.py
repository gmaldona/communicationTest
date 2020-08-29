import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import requests
import bluetooth
import os
   
def pullXML():
    url = 'https://raw.githubusercontent.com/gmaldona/communicationTest/master/communication.xml'

    response  = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('communication.xml', 'w') as file:
        file.write(str(soup))
        
def readXML():
    tree = ET.parse('communication.xml')
    root = tree.getroot()
    for message in root.findall('message'):
        message = message.text
        print(message)
        
def discover():
    devices = []
    times = 1
    while len(devices) == 0:
        devices = bluetooth.discover_devices(lookup_names=True)
        print('devices not found ({})'.format(times))
        times = times + 1 
    print('')
    print('{} devices found:'.format(len(devices)))
    print(devices)
    for device in devices:
        _, name = device

        if name != 'iPhoneRoom317Greg':
            discover()
        else:
            changeXML('1')
            
    #print(type(nearby_devices[0]))
    # if bytes("b'F8:2D:7C:26:E0:14'", 'utf-8') == devices[0]:
    #     print('iPhone found')
    
    
        
    
    
def changeXML(m):
    tree = ET.parse('communication.xml')
    root = tree.getroot()
    for message in root.findall('message'):
        message.text = str(m)
        tree.write('communication.xml')
    os.system("git commmit -am 'update'")
    os.system('git push')

os.system('clear')
changeXML('1')
discover()