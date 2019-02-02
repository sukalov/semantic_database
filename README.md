This is a working directory of one of the projects of the Moscow Lexical Typology (MLexT) group (http://lextyp.org/). 

<p>The main objective of the project:</br>
convertation of collected lexical typological data from .tsv / .csv / .xls(x) files into a unified .xml format</p>

<p>Collaborators: </br>
Taisia Metelkina </br>
Ekaterina Mizerova </br>
Daria Ryzhova </br>
Matvey Sokolovsky </p>

<p>Higher School of Economics </p>
<p>February, 2019 </p>

<p>NB! By the moment, the metalanguage of all data collections is RUSSIAN.</p>


************************************
<h1>OUR TERMINOLOGY:</h1>

field -- semantic field (= semantic domain)</br>
frame -- a typologically oriented lexical meaning (presumably, a member of a universal set of possible lexical meanings)</br>
lexeme -- a lexical item in a given language</br>
microframe -- instantiation of a frame </br>
taxonomic class -- semantic class of a lexeme (cf. size, color, intensifier, etc.) </br>

<h2>EXAMPLE</h2>
lexeme: sharp </br>
frame: instrument with a cutting edge (other possible frames: instrument with a piercing point, object of a tapering form, etc.) </br>
microframes: knife, scissors, saw, sabre... </br>
taxonomic class: physical properties </br>


************************************
<h1>INPUT DATA formats </h1>

<p>Our programs deal with tables of two main types:</p>
<ol>
</li> automatically generated </li> 
</li> manually prepared </li>
<ol>


<h2> Automatically generated files </h2>
<p>Automatically generated tables appear as an output of the algorithms of automatic data collection.</p>

###
<p> useful links: </br>
http://www.dialog-21.ru/media/4553/ryzhovadaplusetal.pdf -- paper presenting the main theoretical issues </br>
https://github.com/panteleeva48/WorkshopLexTyp -- the main GitHub storage of the project </br>
https://github.com/vyhuholl/kr/ -- GitHub storage of the project on Finnish data collection </p>
###

<p> The generated tables are in .tsv and should include the following rows and columns: </p>

<p> first row: \t\t\t lexeme1 \t lexeme2 \t lexeme3 ... </br>
other rows: frame \t microframe \t translation of the microframe \t + \t  \t + ... </p>

<p> "+" (or "1") indicates that a given lexeme covers a given frame / microframe (i.e., a lexeme has this meaning = is used in this context). </p>
<p> In case a lexeme is not used in a given context, the corresponding field should be left blank or filled with the "-" / "0". </p>

<p>See an example in ... </p>

<p>The following data is inserted manually when the convertation program is running:</p>
<ul>
<li>the language of the data in the table </li>
<li>a taxonomic class of a lexeme in a given meaning </li>
<li>semantic field </li>
<li>type of the meaning (direct or figurative in a given context) </li>
</ul>

<h2>Manually prepared files</h2>

<p>Manually prepared tables usually contain more detailed data.</p>

<p>Recommended columns are as follows:</p>
<ul>
<li>lexeme</li>
<li>usage type (whether the lexeme is used or not in a given context; should be filled with "1" or "0")</li>
<li>language</li>
<li>microframe (can be omitted)</li>
<li>translation of the microframe (can be omitted)</li>
<li>frame</li>
<li>taxonomic class</li>
<li>semantic field</li>
<li>type of the meaning (direct or figurative)</li>
<li>example (with a translation, can be omitted)</li>
<li>comment (can be omitted)</li>

<p>The first row must contain the names of the columns:</br>
LEXEME, USAGE, LANG, MFRAME, MFRAME_TRANS, FRAME, TAX_CLASS, FIELD, MEANING, EXAMPLE, COMMENT respectively.</p>

<p>See an example in ...</p>

********************************************
<h1>OUTPUT DATA FORMAT</h1>

<p>Structure of the xml-tree:</p>

'''
<root>
<field>
<frame meaning ="" tax_class="">
<lexeme lang="">
<mframe example="" mframe_trans="" usage=""/>
</lexeme>
</frame>
</field>
</root>
'''

<h2>EXAMPLE:</h2>

'''
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
'''

**********************************************
<h1>ELEMENTS of the tree</h1>
<p>(in alphabetic order; names of the tags are given in CAPS)</p>

<ul>
<li>example - examples and their translations into Russian or English; attribute of the tag MFRAME</li>
	<li>FIELD — semantic field (domain), cf. 'sharp', 'heavy', 'falling', 'oscillation', etc. </li>
	<li>FRAME — frame </li> 
<li>lang — language, attribute of the tag LEXEME (full name of a language or an idiom in Russian)</li>
	<li>LEXEME — lexical item</li>
<li>meaning — type of the meaning, attribute of the tag FRAME. Possible values: "d" (stands for "direct") and "f" (stands for "figurative")</li>
	<li>MFRAME - microframe (see "Our terminology" above)</li>
	<li>mframe_trans — translation of the microframe in Russian, attribute of the tag MFRAME</li>
	<li>tax_class — taxonomic class (see "Our terminology" above), attribute of the tag FRAME</li>
<li>usage — indicates whether the lexeme is used or not in the given context; attribute of the MFRAME </li>
</ul>
