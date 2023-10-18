from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
from xml.dom import minidom 
import os 



root = etree.Element("Library")
m1 = etree.Element("Technical")
root.append(m1)
m2 = etree.Element("Cookery")
root.append(m2)

b1 = etree.SubElement(m1,"Author")
b1.text="John Jabobs"

b2 = etree.SubElement(m2,"Author")
b2.text= "Sally Austin"m

f1 = etree.SubElement(m1,"ISBN")
f1.text = "1234"

f2 = etree.SubElement(m2,"ISBN")
f2.text= "2345"

tree = etree.ElementTree(root) 
with open ("fileName.xml", "wb") as files : 
    tree.write(files)







