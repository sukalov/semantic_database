import xml.etree.ElementTree as ET
from xml.dom import minidom
import pandas as pd


def main():
    df = pd.read_csv("db_full_v2.csv", sep='\t', index_col=False)

    df = df.sort_values(by=['field', 'frame', 'lexeme'])

    df = df.assign(usage= df.lexeme.str.startswith('-', na=False))

    df = df.replace({'usage': {False:"+", True:'-'}})

    df.to_csv('PANDAS_RESULT.csv', sep='\t')
    
    



'''
dftest = df[(df.mframe == 'Жаркий спор')]'''
'''
df_fieldlist = df.drop_duplicates(subset='field', keep='first', inplace=False)
fieldlist = list(df2.field))

for element in fieldlist:
    df_1_field = df[(df.field == element)]
    

df_1_ = df.drop_duplicates(subset='field', keep='first', inplace=False)

df = df.sort_values(by=['field', 'frame', 'lexeme'])
'''



#OLD
'''
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
#            maframe_translation = [3]

name = "db_full_v2.txt"

f = open (name, 'r', encoding = 'utf-8')
all_strings = f.read()
f.close()
strings = all_strings.split ("\n")


fieldic = {} #dictionary. key - field, val - LIST consisting of lists2. each list2 is a string relating to the field

for string in strings:
    if not string.startswith('\t'):
        param = string.split("\t")
        if param[6] not in fieldic:
            fieldic[param[6]] = [param]
        else:
            fieldic[param[6]].append(param)

fulldic = {} #key - field, val - dictionary with frames. 
for _field_ in fieldic:
    dic = {} #key – frame, val – lexdic parts
    lexdic = {} #dictionary. key - lexeme, val - list of strings

    for stri in fieldic[_field_]:
        if stri[0] not in lexdic:
            lexdic[stri[0]] = [stri]
        else:
            lexdic[stri[0]].append(stri)

    for lex in lexdic:
        lexframe = lexdic[lex][0][4]
        if lexframe not in dic:
            dic[lexframe] = {}
            dic[lexframe][lex] = lexdic[lex]
        else:
             dic[lexframe][lex] = lexdic[lex]

    fulldic[_field_] = dic

    # fulldic structure:
    # ROOTdic   key - fields, val - dic1.
    # dic1      key - frames, val - dic2
    # dic2      key - lexemes, val – a list of all strings with this lexeme.

    # field1:
    #   frame1:
    #       lexeme1:
    #           string with lexeme1 + microframe1
    #           string with lexeme1 + microframe2
    #           string with lexeme1 + microframe3
    #       lexeme2:
    #           string with lexeme2
    #   frame2:
    #       lexeme3:
    # field2

root = ET.Element ('root')
root.text = ""  
for _field_ in fulldic:

    field = ET.SubElement (root, 'field')
    field.text = _field_
    framedic = fulldic[_field_]
   
    for _frame_ in framedic:

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

        lexedic = framedic[_frame_]
        for lexe in lexedic:
            frame.text = _frame_

            lang = ET.Element ("lang")
            lang.text = lexedic[lexe][0][1]
            usage = ET.Element ("usage")

            if lexe.startswith ('-'):
                usage.text = "-"
                lexe2 = lexe.strip('-')
            else:
                usage.text = "+"
                lexe2 = lexe

            lexeme = ET.SubElement (frame, 'lexeme', attrib = {"lang":lang.text, "usage":usage.text})
            lexeme.text = lexe2

            for el in lexedic[lexe]:

                if el[2] != '':
                    if el[3] != '':
                        mframe_trans = ET.Element("trans")
                        mframe_trans.text = el[3]
                        mframe = ET.SubElement (lexeme, "mframe", attrib = {"trans":mframe_trans.text})#, attrib = {"trans":translation_micro_frame.text)
                        mframe.text = el[2]
                    else:
                        mframe = ET.SubElement (lexeme, "mframe")#, attrib = {"trans":translation_micro_frame.text)
                        mframe.text = el[2]

               # trans = ET.Element ("trans")
               # trans.text = el[5]
                
               # example = ET.SubElement (mframe, "example", attrib = {"trans":trans.text})
               # example.text = el[4]

save_xml('adjectives_test.xml', root)

'''

if __name__ ==  '__main__':
    main()