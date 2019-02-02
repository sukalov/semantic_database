import xml.etree.ElementTree as ET
from xml.dom import minidom
import pandas as pd
import numpy as np

def save_xml(filename, xml_code):   #ВАЖНО. сейчас режим writing, т.е. каждый запуск переписывает новый файл с нуля
    xml_string = ET.tostring(xml_code).decode()
    xml_prettyxml = minidom.parseString(xml_string).toprettyxml()
    with open(filename, 'w', encoding = "utf-8") as xml_file:
        xml_file.write(xml_prettyxml)


def main():

    FILE_IN = str(input("Название файла с таблицей (расширение файла csv. оно не указывается): "))

    df = pd.read_csv(FILE_IN + '.csv', sep='\t', index_col=False)  #создаём пандасовский датафрейм
    df = df.replace(np.nan, '', regex=True) # во избежание ошибок вставляем пустые строки во все пустые клетки таблицы
    df = df[df.lexeme != '']   # удаление строк с пустым значением лексемы.
    df = df.sort_values(by=['field', 'frame', 'lexeme', 'mframe'])  #сортируем датафрейм по всей иерархии (по уровням {XML)


    # df.to_csv('pandas_table.csv', sep='\t', index=False)

    # закомментированная строка создаёт дополнительный файл с таблицей после преобразований.
    # если таблица удовлетворяет всем требованиям, это не нужно
    # если нет, сверху можно вписывать дополнительные преобразования, и, сохраняя дополнительную pandas_table,
    # смотреть, соответствует ли таблица условиям после них


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
                checkframe = str(string.frame)
                meaning = ET.Element ("meaning")
                meaning.text = str(string.meaning)
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
                lang.text = str(string.lang)
                lexeme = ET.SubElement (frame, 'lexeme', attrib = {"lang":lang.text})
                lexeme.text = str(string.lexeme)

            if string.mframe != checkmframe:
                checkmframe = string.mframe
                usage = ET.Element ("usage")
                usage.text = str(string.usage)

                mframe_trans = ET.Element ("mframe_trans")
                mframe_trans.text = str(string.mframe_trans)

                example = ET.Element ("example")
                example.text = str(string.example)

                comment = ET.Element ("comment")
                comment.text = str(string.comment)

                if mframe_trans.text != "" and mframe_trans.text != "nan":  # неоптимальное решение проблемы того, что все аттрибуты микрофрейма кроме usage -- опциональны. (тупое перечисление всех возможных комбинаций аттрибутов)
                    if example.text != "" and example.text != "nan":
                        if comment.text != "" and comment.text != "nan":
                            mframe = ET.SubElement (lexeme, 'mframe', attrib = {"usage":usage.text, "trans":mframe_trans.text, "example":example.text, "comment":comment.text})
                            mframe.text = str(string.mframe)
                        else:
                            mframe = ET.SubElement (lexeme, 'mframe', attrib = {"usage":usage.text, "trans":mframe_trans.text, "example":example.text})
                            mframe.text = str(string.mframe)
                    else:
                        if comment.text != "" and comment.text != "nan":
                            mframe = ET.SubElement (lexeme, 'mframe', attrib = {"usage":usage.text, "trans":mframe_trans.text, "comment":comment.text})
                            mframe.text = str(string.mframe)
                        else:
                            mframe = ET.SubElement (lexeme, 'mframe', attrib = {"usage":usage.text, "trans":mframe_trans.text})
                            mframe.text = str(string.mframe)
                else:
                    if example.text != "" and example.text != "nan":
                        if comment.text != "" and comment.text != "nan":
                            mframe = ET.SubElement (lexeme, 'mframe', attrib = {"usage":usage.text, "example":example.text, "comment":comment.text})
                            mframe.text = str(string.mframe)
                        else:
                            mframe = ET.SubElement (lexeme, 'mframe', attrib = {"usage":usage.text, "example":example.text})
                            mframe.text = str(string.mframe)
                    else:
                        if comment.text != "" and comment.text != "nan":
                            mframe = ET.SubElement (lexeme, 'mframe', attrib = {"usage":usage.text, "comment":comment.text})
                            mframe.text = str(string.mframe)
                        else:
                            mframe = ET.SubElement (lexeme, 'mframe', attrib = {"usage":usage.text})
                            mframe.text = str(string.mframe)



    save_xml(FILE_IN + '.xml', root)

if __name__ ==  '__main__':
    main()