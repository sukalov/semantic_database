This is a working directory of one of the projects of the Moscow Lexical Typology (MLexT) group (http://lextyp.org/). 

The main objective of the project:
convertation of collected lexical typological data from .tsv / .csv / .xls(x) files into a unified .xml format

Collaborators:
Taisia Metelkina
Ekaterina Mizerova
Daria Ryzhova
Matvey Sokolovsky

Higher School of Economics
February, 2019

NB! By the moment, the metalanguage of all data collections is RUSSIAN.


************************************
OUR TERMINOLOGY:

field -- semantic field (= semantic domain)
frame -- a typologically oriented lexical meaning (presumably, a member of a universal set of possible lexical meanings)
lexeme -- a lexical item in a given language
microframe -- instantiation of a frame 
taxonomic class -- semantic class of a lexeme (cf. size, color, intensifier, etc.)

EXAMPLE
lexeme: sharp
frame: instrument with a cutting edge (other possible frames: instrument with a piercing point, object of a tapering form, etc.)
microframes: knife, scissors, saw, sabre...
taxonomic class: physical properties 


************************************
INPUT DATA formats

Our programs deal with tables of two main types:
(1) automatically generated 
(2) manually prepared


	(1) Automatically generated files
Automatically generated tables appear as an output of the algorithms of automatic data collection.

###
useful links:
http://www.dialog-21.ru/media/4553/ryzhovadaplusetal.pdf -- paper presenting the main theoretical issues
https://github.com/panteleeva48/WorkshopLexTyp -- the main GitHub storage of the project
https://github.com/vyhuholl/kr/ -- GitHub storage of the project on Finnish data collection
###

The generated tables are in .tsv and should include the following rows and columns:

first row: \t\t\t lexeme1 \t lexeme2 \t lexeme3 ...
other rows: frame \t microframe \t translation of the microframe \t + \t  \t + ...

"+" (or "1") indicates that a given lexeme covers a given frame / microframe (i.e., a lexeme has this meaning = is used in this context).
In case a lexeme is not used in a given context, the corresponding field should be left blank or filled with the "-" / "0". 

See an example in ...

The following data is inserted manually when the convertation program is running:
the language of the data in the table
a taxonomic class of a lexeme in a given meaning
semantic field
type of the meaning (direct or figurative in a given context).


	(2) Manually prepared files

Manually prepared tables usually contain more detailed data.

Recommended columns are as follows:
lexeme
usage type (whether the lexeme is used or not in a given context; should be filled with "1" or "0")
language
microframe (can be omitted)
translation of the microframe (can be omitted)
frame
taxonomic class
semantic field
type of the meaning (direct or figurative)
example (with a translation, can be omitted)
comment (can be omitted)

The first row must contain the names of the columns:
LEXEME, USAGE, LANG, MFRAME, MFRAME_TRANS, FRAME, TAX_CLASS, FIELD, MEANING, EXAMPLE, COMMENT respectively.

See an example in ...

********************************************
OUTPUT DATA FORMAT

Structure of the xml-tree:

<root>
<field>
<frame meaning ="" tax_class="">
<lexeme lang="">
<mframe example="" mframe_trans="" usage=""/>
</lexeme>
</frame>
</field>
</root>

EXAMPLE:

<root>
<field> острый
<frame meaning = "d" tax_class = "физ.свойства">
инструмент с режущим краем
<lexeme lang = "русский">
острый
<mframe mframe_trans="нож" usage ="1">
острый_нож
</mframe>
<mframe mframe_frame="борода" usage="0">
колючий_борода
</mframe>
...
</lexeme>
...
</frame>
...
</field>
...
</root>


**********************************************
ELEMENTS of the tree
(in alphabetic order; names of the tags are given in CAPS)

example - examples and their translations into Russian or English; attribute of the tag MFRAME
FIELD — semantic field (domain), cf. 'sharp', 'heavy', 'falling', 'oscillation', etc. 
FRAME — frame 
lang — language, attribute of the tag LEXEME (full name of a language or an idiom in Russian)
LEXEME — lexical item
meaning — type of the meaning, attribute of the tag FRAME. Possible values: "d" (stands for "direct") and "f" (stands for "figurative")
MFRAME - microframe (see "Our terminology" above)
mframe_trans — translation of the microframe in Russian, attribute of the tag MFRAME
tax_class — taxonomic class (see "Our terminology" above), attribute of the tag FRAME
usage — indicates whether the lexeme is used or not in the given context; attribute of the MFRAME 
