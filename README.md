This is a working directory of one of the projects of the Moscow Lexical Typology (MLexT) group (http://lextyp.org/). 

<p>The main objective of the project:</br>
convertation of collected lexical typological data from .tsv / .csv / .xls(x) files into a unified .xml format</p>

<p><strong>Collaborators:</strong> </br>
Taisia Metelkina </br>
Ekaterina Mizerova </br>
Daria Ryzhova </br>
Matvey Sokolovsky </p>

<p>Higher School of Economics </p>
<p>February, 2019 </p>

<p>NB! By the moment, the metalanguage of all data collections is RUSSIAN.</p>


************************************
<h1>OUR TERMINOLOGY:</h1>

<strong>field</strong> -- semantic field (= semantic domain)</br>
<strong>frame</strong> -- a typologically oriented lexical meaning (presumably, a member of a universal set of possible lexical meanings)</br>
<strong>lexeme</strong> -- a lexical item in a given language</br>
<strong>microframe</strong> -- instantiation of a frame </br>
<strong>taxonomic class</strong> -- semantic class of a lexeme (cf. size, color, intensifier, etc.) </br>

<h2>EXAMPLE</h2>
<strong>lexeme:</strong> sharp </br>
<strong>frame:</strong> instrument with a cutting edge (other possible frames: instrument with a piercing point, object of a tapering form, etc.) </br>
<strong>microframes:</strong> knife, scissors, saw, sabre... </br>
<strong>taxonomic class:</strong> physical properties </br>


************************************
<h1>INPUT DATA formats </h1>

<p>Our programs deal with tables of two main types:</p>
<ol>
<li> automatically generated </li> 
<li> manually prepared </li>
</ol>


<h2> Automatically generated files </h2>
<p>Automatically generated tables appear as an output of the algorithms of automatic data collection.</p>

<p> useful links: </br>
http://www.dialog-21.ru/media/4553/ryzhovadaplusetal.pdf —— paper presenting the main theoretical issues </br>
https://github.com/panteleeva48/WorkshopLexTyp —— the main GitHub storage of the project </br>
https://github.com/vyhuholl/kr/ —— GitHub storage of the project on Finnish data collection </p>


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

The code, converting a .csv table (with separators = '\t'), is [CSVtoXMLconverter.py](../master/CSVtoXMLconverter.py)

<p>Required columns are as follows:</p>
<ul>
<li>lexeme</li>
<li>usage (whether the lexeme is used or not in a given context; should be filled with "1" or "0")</li>
<li>lang (for language)</li>
<li>mframe (for microframe) (can be omitted) (empty column still required)</li>
<li>mframe_trans (translation of the microframe) (can be omitted) (empty column still required)</li>
<li>frame</li>
<li>tax_class (taxonomic class)</li>
<li>field (for semantic field)</li>
<li>meaning (type of meaning) (filled with "d" or "f", meaning direct or figurative)</li>
<li>example (with a translation, can be omitted) (empty column still required)</li>
<li>comment (can be omitted) (empty column still required)</li>
</ul>

The first row must contain the names of these columns in free order. 
See an example in [a table with adjectives](../master/adjectives/adjectives.csv)

********************************************
<h1>OUTPUT DATA FORMAT</h1>

<p>Structure of the xml-tree:</p>

``` xml
<root>
    <field>
        <frame meaning ="" tax_class="">
            <lexeme lang="">
                <mframe example="" mframe_trans="" usage=""/>
            </lexeme>
        </frame>
    </field>
</root>
```

<h2>EXAMPLE:</h2>

``` xml
<root>
    <field>
    острый
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
```

**********************************************
<h1>ELEMENTS of the tree</h1>
<p>(in alphabetic order; names of the tags are given in CAPS)</p>

<ul>
<li><strong>example</strong> - examples and their translations into Russian or English; attribute of the tag MFRAME</li>
	<li><strong>FIELD</strong> — semantic field (domain), cf. 'sharp', 'heavy', 'falling', 'oscillation', etc. </li>
	<li><strong>FRAME</strong> — frame </li> 
<li><strong>lang</strong> — language, attribute of the tag LEXEME (full name of a language or an idiom in Russian)</li>
	<li><strong>LEXEME</strong> — lexical item</li>
<li><strong>meaning</strong> — type of the meaning, attribute of the tag FRAME. Possible values: "d" (stands for "direct") and "f" (stands for "figurative")</li>
	<li><strong>MFRAME</strong> - microframe (see "Our terminology" above)</li>
	<li><strong>mframe_trans</strong> — translation of the microframe in Russian, attribute of the tag MFRAME</li>
	<li><strong>tax_class</strong> — taxonomic class (see "Our terminology" above), attribute of the tag FRAME</li>
<li><strong>usage</strong> — indicates whether the lexeme is used or not in the given context; attribute of the MFRAME </li>
</ul>
