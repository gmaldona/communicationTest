import xml.etree.ElementTree as ET


tree = ET.parse('communication.xml')
root = tree.getroot()
for message in root.findall('message'):
    message = message.text
    print(message)
