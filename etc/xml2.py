import xml.etree.ElementTree as ET

tree = ET.parse('/Users/jakehong/python/etc/GC00930024.xml')
root = tree.getroot()

# GC00930024

print(root.tag, root.attrib)

for book in root:
  print("-->1 ",book.tag, book.attrib, "x",book.text, "i",book.tail)

  for book1 in book:
    print("---->2 ", book1.tag, book1.attrib, "x",book1.text, "i",book1.tail)

    for book2 in book1:
        print("------>3",book2.tag, book2.attrib, "x",book2.text, "i",book2.tail)
        
        for book3 in book2:
            print("-------->4",book3.tag, book3.attrib, "x",book3.text, "i",book3.tail)

            for book4 in book3:
                print("---------->5",book4.tag, book4.attrib, "x",book4.text, "i",book4.tail)



