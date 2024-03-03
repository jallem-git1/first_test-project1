import xml.etree.ElementTree as ET

def p_text(current, parent=None, index=-1, depth=1):
    for i, node in enumerate(current):
        # print( ('\t' * depth), i, node)
        print("     " * depth, ">", end = "" )
        if node.tag  == ""  :
            print("")
        else:
            print(node.tag, end = "")
        node_cnt =0 

        for n_cnt in node.attrib:
            node_cnt += 1

        if node_cnt > 0 :
            print( node.attrib, end = "")
        else:
            print("", end = "")

        #print(node.attrib, end = "");
            
        print("x", end = "")
        if node.text != None:
            txt = node.text.strip()
        else:
            txt = ""  #node.text
        print(txt,  end = "")

        print("t", end = "")
        if node.tail != None :
            tail = node.tail.strip()
        else:
            tail = node.tail
        print(tail, end = "\n")

        p_text(node, current, i, depth=depth + 1)

    #depth = depth + 1

    # if parent is not None:
    #     if index == 0:
    #         parent.text = parent.text +'\n' + ('\t' * depth) 
    #     else:
    #         parent[index - 1].tail = parent[index - 1].tail + '\n' + ('\t' * depth) 
    #     if index == len(parent) - 1:
    #         current.tail = current.tail + '\n' + ('\t' * (depth - 1)) 


filePath = "/Users/jakehong/python/etc/GC00930024.xml"
tree = ET.parse(filePath)
root = tree.getroot()
# ET.dump(tree)
print(root.tag)

p_text(tree.getroot())
print("*"*50)
#ET.dump(tree)