#import xml.etree.ElementTree as ET

import pandas as pd
import xml.etree.ElementTree as et

file1 = '''
<?xml version="1.0" encoding="UTF-8"?>
<students>
    <student>
        <name>Joe Jones</name>
        <year>Soph.</year>
        <testgrade>95</testgrade>
    </student>
    <student>
        <name>Alice Brown</name>
        <year>senior</year>
        <testgrade>97</testgrade>
    </student>
    <student>
        <name>Sam Smith</name>
        <year>senior</year>
        <testgrade>90</testgrade>
    </student>
</students>
    '''


  
#xtree=et.parse("students.xml")

#xtree=et.parse(file1)
xtree = et.fromstring(file1)
print(file1)

xroot=xtree.getroot()
print(xroot)
exit()

df_cols=["name","year","testgrade"]
row=[]
  
for node in xroot:
  s_name=node.find("name").text
  s_year=node.find("year").text if node is not None else None
  s_grade=node.find("testgrade").text if node is not None else None
  #s_age=node.find("age").text if node is not None else None
  
  rows.append({"name":s_name, "year":s_year,
               "testgrade":s_grade})
  
  out_df = pd.DataFrame(rows,colums=df_cols) 


'''import pandas as pd
import xml.etree.ElementTree as et'''
  
def parse_XML(xml_file,df_cols):  
    xtree=et.parse("students.xml")
    xroot=xtree.getroot()
    row=[]
  
    for node in xroot:
  	res=[]
   	res.append(node.attrib.get(df_cols[0]))
    	for el in f_cols[1:]:
   	  if node is not None and node.find(el) is not None:
     		res.append(node.find(el).text)
  	  else:
   		res.append(None)
        row.append({df_cols[i]:res[i] 
  		    for i,_ in enumerate(df_cols)})
  
    out_df=pd.DataFrame(rows,columns=df_cols)
    return out_df
  
    out_df= pd.DataFrame(rows,colums=df_cols) 
  
#   parse_XML( "students.xml", ["name","email","grade","age"])


