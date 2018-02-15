import xml.etree.ElementTree as ET
from xml.dom import minidom

def save_xml(filename, xml_code):
    xml_string = ET.tostring(xml_code).decode()
 
    xml_prettyxml = minidom.parseString(xml_string).toprettyxml()
    with open(filename, 'a', encoding = "utf-8") as xml_file:
        xml_file.write(xml_prettyxml)

# 1 – language [0]
# 2 – lexeme [1]
# 3 – lexeme translation [2]
# 4 – frame [3]
# 5 – example [4]
# 6 – example translation [5]
# 7 – comment [6]

name = "metaphors.txt"

f = open (name, 'r', encoding = 'utf-8')
all_strings = f.read()
f.close()
strings = all_strings.split ("\n")

dic = {} #dictionary. key - frame, val - all table strings whith the frame
for string in strings:
    param = string.split("\t")
    if param[3] not in dic:
        dic[param[3]] = [param]
    else:
        dic[param[3]].append(param)

field = ET.Element ('field')
field.text = "глаголы падения"
for fra in dic:
    meaning = ET.Element ("meaning")
    meaning.text = "f" #tamle contents no metaphoric meanings

    frame = ET.SubElement (field, "frame", attrib = {"meaning":meaning.text})#, "tax_class":tax_class.text})
    for el in dic[fra]:
        frame.text = fra

        lang = ET.Element ("lang")
        lang.text = el[0]

        
        lexeme = ET.SubElement (frame, 'lexeme', attrib = {"lang":lang.text})
        lexeme.text = el[1]

        if el[4] != '' and el[5] != '':
            mframe = ET.SubElement (lexeme, "mframe")#, attrib = {"trans":translation_micro_frame.text)
            mframe.text = ""

            trans = ET.Element ("trans")
            trans.text = el[5]
            
            example = ET.SubElement (mframe, "example", attrib = {"trans":trans.text})
            example.text = el[4]

save_xml('metaphors_COMPLETE.xml', field)
    





