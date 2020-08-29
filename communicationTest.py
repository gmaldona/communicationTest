import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import requests
   
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
    
def changeXML(m):
    tree = ET.parse('communication.xml')
    root = tree.getroot()
    for message in root.findall('message'):
        message.text = str(m)
        tree.write('communication.xml')
    
changeXML('1')