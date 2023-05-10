# Natural-language-processing
Suggested execution order:
  1. news_spider.py
  2. parser.py
  3. postagger.py
  4. preprocessing.py
  5. createIndex.py
  6. questions.py

 The partb.py is a stand-alone file.
 ## Website crawler
First a crawler was created to collect the documents from [TheVerge](https://www.theverge.com/) news websites. The crawler was made using the [Scrapy](https://scrapy.org/) python framework.
Each sub-category page of the site follows exactly the same structure, so various categories of articles were crawled (film, environment, space, health, books).
The crawler downloads the html page of each article and stores them all in the html_pages folder.
## Parsing
The data gets parsed & goes through a first process using the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) library.
To export only the text of the article we take all the corresponding ***div classes c-entry-content*** which is the article and export the ***p*** elements as text and save them in a txt file.
## Morphological Segmentation
Segmentation is done with the [nltk](https://www.nltk.org/) library. Each plain text file was split into words and each word was identified with a tag.

At this point we define the stopwords (***openclasscategorytags []***) and some symbols (***other_stuff []***) and we put them both in the same table named ***stop_words***.
We then tokenize each txt text and remove and add each word of text to a ***filtered_sen[]*** array removing what is in the ***stop_words[]*** array (tokenization & stop words removal).

Finally, new files are created in the tag_files folder that contains the morphosyntax of each word for each article separately.
A tag file takes the form of a table where column 0 has the word and column 1 has the tag (Parts-of-speec POS tagging).
## Representation in the Vector Space Model.
Here we start with some extra pre-processing of the word tag files. First, for each tag file, we read it as csv because the structure we to follow is that of python a dictionary. 
We insert the data into an array (all_txts) which has the form  ***['forecast', 'nn'], ['authors', 'nns'], ['fight', 'vbd'], ...***

Then a dictionary is created that will store each lemmatize word as a key and as a value how many times it appeared in the text. And it stores all this in another dictionary that will have the text id as key and the previous dictionary as value.

    {..., 1344: {'apple':12, 'compamy': 3, ...} ...}
1344 being the text/document id (key) and the value of the dictionary (the previous dictionary) means that the word apple appeared 12 times and word company 3 times
## Creating the index
This is where TFIDF calculation and index creation take place.
Done with 4 functions (1 to calculate TF, 1 to calculate IDF, 1 to calculate TFIDF and 1 to create the index).

For each unique entry, a record was created in the index, which was in the form of a dictionary, indicating in which texts the entry appears and with what weight (index.xml).

The form of index.xml:
    
    ...
    <lemma name='millionaire'>
        ...
        <document id = "1082" weight = "0.0005748357829"/>
        <document id = "881" weight = "0.0128493028"/>
        ...
    </lemma>
    ....
## Index Evaluation
Implemented a simple query mechanism for the index. The mechanism accepts as aninput a query (consisting of one or more entries), 
which will match to the index entries and will it return the article id and the url of the web pages which contain the entry or the query terms to the user.

The index which is in xml format is loaded into a dictionary with the help of the [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html) library.

# Part B
From [here](http://qwone.com/~jason/20Newsgroups), chose the file ***20news-bydate.tar*** because the site recommends it. It has 2 folders inside 1 for train and one for test.
The purpose of this part is to implement a text categorization system in predefined subject categories
