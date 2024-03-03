import xml.etree.ElementTree as ET

#filePath = "/Users/jakehong/python/etc/GC00930024.xml"
#tree = ET.parse(filePath)
#ET.dump(tree)

def _pretty_print(current, parent=None, index=-1, depth=0):
    for i, node in enumerate(current):
        # print( ('\t' * depth), i, node)
        # print(current, parent, index, depth, i, node)
        _pretty_print(node, current, i, depth + 1)
    if parent is not None:
        if index == 0:
            parent.text = parent.text +'\n' + ('\t' * depth) 
        else:
            parent[index - 1].tail = parent[index - 1].tail + '\n' + ('\t' * depth) 
        if index == len(parent) - 1:
            current.tail = current.tail + '\n' + ('\t' * (depth - 1)) 


filePath = "/Users/jakehong/python/etc/GC00930024.xml"
tree = ET.parse(filePath)

# ET.dump(tree)

_pretty_print(tree.getroot())
print("----------------------------")
ET.dump(tree)