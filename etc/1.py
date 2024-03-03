#import os
#print(os.getcwd())

# Python 3.3 code
import xml.etree.ElementTree as ET

file1 = '''<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>'''
tree = ET.fromstring(file1)

#tree = ET.parse(file1)
#root = tree.getroot()

root = ET.fromstring(file1)

print(root.tag)
print(root.attrib)

for child in root[0]:
     print(child.tag, child.attrib, child.text)

#for neighbor in root.iter('neighbor'):
#     print(neighbor.attrib)