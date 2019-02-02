import xml.etree.ElementTree as ET
from xml.dom import minidom
import pandas as pd
import re

def save_xml(filename, xml_code):   #ВАЖНО. сейчас режим writing,
    xml_string = ET.tostring(xml_code).decode()

    xml_prettyxml = minidom.parseString(xml_string).toprettyxml()
    with open(filename, 'w', encoding = "utf-8") as xml_file:
        xml_file.write(xml_prettyxml)


def correcting_lexemes(lexeme):  #стирание минусов в начале лексем
    lexeme = str(lexeme)
    if lexeme.startswith('-'):
        lexeme = lexeme[1:]
    if lexeme == 'nan':
        lexeme = ''
    return lexeme

def main():
    df = pd.read_csv("db_full_v2.csv", sep='\t', index_col=False)  #создаём пандасовский датафрейм

    df = df.sort_values(by=['field', 'frame', 'lexeme', 'mframe'])  #сортируем его по всей иерархии

    df = df.assign(usage= df.lexeme.str.startswith('-', na=False))   #этими тремя строчками решаем вопрос с минусами вначале лексем
    df = df.replace({'usage': {False:"+", True:'-'}})                #(превращаем их в колонку usage с минусами и плюсами)
    df["lexeme"]  =  df["lexeme"].apply(correcting_lexemes)          #дело это скорее специфичное для таблицы db_full_v2


    df.to_csv('PANDAS_RESULT.csv', sep='\t')      #это можно и убрать. делаем csv файл, чтобы посмотреть на его вариант таблицы

    fields = []
    for elem in df["field"]:
        if elem not in fields:
            fields.append(elem)

    checkfield = "X"
    checkframe = "X"
    checklexeme = "X"
    checkmframe = "X"

    root = ET.Element ('root')
    root.text = ""
    for index, string in df.iterrows():

            if string.field != checkfield:
                checkfield = string.field
                field = ET.SubElement (root, 'field')
                field.text = string.field

            if string.frame != checkframe:
                checkframe = string.frame
                meaning = ET.Element ("meaning")
                meaning.text = string.meaning
                tax_class = ET.Element ("tax_class")
                tax_class.text = str(string.tax_class)
                if tax_class.text != "" and tax_class.text != "nan":
                    frame = ET.SubElement (field, "frame", attrib = {"meaning":meaning.text, "tax_class":tax_class.text})
                    frame.text = string.frame
                else:
                    frame = ET.SubElement (field, "frame", attrib = {"meaning":meaning.text})
                    frame.text = string.frame

            if string.lexeme != checklexeme:
                checklexeme = string.lexeme
                lang = ET.Element("lang")
                lang.text = string.lang
                lexeme = ET.SubElement (frame, 'lexeme', attrib = {"lang":lang.text})
                lexeme.text = string.lexeme

            if string.mframe != checkmframe:
                checkmframe = string.mframe
                usage = ET.Element ("usage")
                usage.text = string.usage
                mframe_trans = ET.Element ("mframe_trans")
                mframe_trans.text = str(string.mframe_trans)
                if mframe_trans.text != "" and mframe_trans.text != "nan":
                    mframe = ET.SubElement (lexeme, 'mframe', attrib = {"usage":usage.text, "trans":mframe_trans.text})
                    mframe.text = string.mframe
                else:
                    mframe = ET.SubElement (lexeme, 'mframe', attrib = {"usage":usage.text})
                    mframe.text = string.mframe

    save_xml('PANDAS_test.xml', root)

if __name__ ==  '__main__':
    main()