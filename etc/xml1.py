import xml.etree.ElementTree as ET

#tree = ET.parse('/Users/jakehong/python/etc/books.xml')
tree = ET.parse('/Users/jakehong/python/etc/GC00930024.xml')

root = tree.getroot()

# GC00930024

print(root.tag)
print("-11111111111111-----------------")

for book in root:
  #print(book.attrib)
  #print(book.tag)
  print(book.tag, book.attrib)

print("-222222222222222-----------------")

for book in root.findall('항목명'):
  # title = book.find("한글항목명").text
  print(book.tag, book.attrib)

  #print(title)
print("--3333333333333----------------")

for book in root.findall('book'):
  title = book.find("title").text
  price = book.find("price").text
  print(title, "--->", price)
print("------------------")

for book in root.iter("description"):
  print(book.text)
print("-66666666666--")

for book in root.findall('book'):
  description = book.find("description").text
  print(description)
print("------------------")