import xml.etree.ElementTree as ET

filePath = "/Users/jakehong/python/etc/GC00930024.xml"
tree = ET.parse(filePath)
#ET.dump(tree)

current = tree.getroot()
print(current)

for i, node in enumerate(current):
    # print( ('\t' * depth), i, node)
    print(current, i, node)