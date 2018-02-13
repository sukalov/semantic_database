import xml.etree.ElementTree as ET
from xml.dom import minidom

def save_xml(filename, xml_code):
    xml_string = ET.tostring(xml_code).decode()
 
    xml_prettyxml = minidom.parseString(xml_string).toprettyxml()
    with open(filename, 'a', encoding = "utf-8") as xml_file:
        xml_file.write(xml_prettyxml)

#            field = [6]
#            frame = [4]
#            lexeme = [0]           
#            meaning = [7]
#            tax_class = [5]
#            lang = [1]
#            mframe = [2]

def write_txt(what, where):
    doc = open(where, 'w', encoding='utf-8')
    doc.write(what)
    doc.close()

name = "db_full_v2.txt"

f = open (name, 'r', encoding = 'utf-8')
all_strings = f.read()
f.close()
strings = all_strings.split ("\n")

lexdic - {}

for st in strings:
    param = string.split("\t")
    if param[0] not in fieldic:
        lexdic[param[0]] = [param]
    else:
        lexdic[param[0]].append(param)

fieldic = {} #dictionary. key - field, val - list consisting of LISTS. each list is a string with the field
for elem in lexdic:
    dic = {}
    for string in lexdic[elem]:
        if string[6] not in fieldic:
            dic[string[6]] = [param]
        else:
            dic[string[6]].append(param)
    fieldic[]

fulldic = {} #key - field, val - dictionary with frames. 
for _field_ in fieldic:
    dic = {} #dictionary. key - frame, val - all table strings whith the frame
    for stri in fieldic[_field_]:
        if stri[4] not in dic:
            dic[stri[4]] = [stri]
        else:
            dic[stri[4]].append(stri)
    fulldic[_field_] = dic

write_txt(str(fulldic), "FLDC.txt")

root = ET.Element ('root')
root.text = ""  
for _field_ in fulldic:
    
    ##field = ET.SubElement (root, 'field')
    field = ET.SubElement (root, 'field')
    field.text = _field_
    dic = fulldic[_field_]
   
    for _frame_ in dic:

        meaning = ET.Element ("meaning")
        if param [7] == "и":
            meaning.text = "d"
        elif param [7] == "п":
            meaning.text = "f"
        elif _list_ [7] == "":
            meaning.text = 'unknown'

        tax_class = ET.Element ("tax_class")
        tax_class.text = param[5]
        
        frame = ET.SubElement (field, "frame", attrib = {"meaning":meaning.text, "tax_class":tax_class.text})
        for el in dic[_frame_]:
            frame.text = _frame_
            lang = ET.Element ("lang")
            lang.text = el[1]

            usage = ET.Element ("usage")
            if el[0].startswith ('-'):
                usage.text = "-"
                el[0] = el[0].strip('-')
            else:
                usage.text = "+"

            lexeme = ET.SubElement (frame, 'lexeme', attrib = {"lang":lang.text, "usage":usage.text})
            lexeme.text = el[0]

            if el[2] != '':
                mframe = ET.SubElement (lexeme, "mframe")#, attrib = {"trans":translation_micro_frame.text)
                mframe.text = el[2]

               # trans = ET.Element ("trans")
               # trans.text = el[5]
                
               # example = ET.SubElement (mframe, "example", attrib = {"trans":trans.text})
               # example.text = el[4]

save_xml('xml__db_full_v2.xml', root)
