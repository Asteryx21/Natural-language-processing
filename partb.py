def preprocess(data):
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    import re
    import nltk
    
    stop_words = stopwords.words("english") ##remove stop words from txt. for better pos tagging.
    lemmatizer = WordNetLemmatizer()
    openclasscategorytags = ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'NN', 'NNS', 'NNP','NNPS','VB','VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'FW']
    regex = re.compile('[^a-zA-Z ]')
    all_docs = []
    for d in data:
        d=str(d)
        # tokenize the doc
        wordArr = word_tokenize(d)
        # remove stop words
        wordArr = [word for word in wordArr if word not in stop_words]
        wordArr = [word.split("\\n")[0] for word in wordArr]
        wordArr = [word.split("\\t")[0] for word in wordArr]
        wordArr = [word.split("\\")[0] for word in wordArr]
        # remove punctuation
        wordArr = [regex.sub('', str(word)) for word in wordArr]
    
        # lemmatize every word
        wordArr = [lemmatizer.lemmatize(word.split(".")[0]) for word in wordArr]
        #pos tagger
        tagged = nltk.pos_tag(wordArr)
        wordArr = [i[0] for i in tagged if i[1] in openclasscategorytags]
        #remove spaces and one letter words 
        wordArr = [word for word in wordArr if len(word)>1]
        #merged tokenized words back to sentence
        filtered_sentence = (" ").join(wordArr)
        all_docs.append(filtered_sentence)
    return all_docs

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.metrics import accuracy_score
import sklearn.datasets as skd

#files paths
path_E = 'C:/Users/evans/OneDrive/Desktop/Language_Technology/20news-bydate-train/'
path_A = 'C:/Users/evans/OneDrive/Desktop/Language_Technology/20news-bydate-test/'

#load set A and set E
news_train = skd.load_files(path_E, encoding= 'ISO-8859-1')
news_test = skd.load_files(path_A, encoding= 'ISO-8859-1')

#preprocess news documents
set_E = preprocess(news_train.data)
set_A = preprocess(news_test.data)

#vectors
count_vect = CountVectorizer()
set_E_tf = count_vect.fit_transform(set_E)
set_A_tf = count_vect.transform(set_A)

# tfidf calculations
tfidf_transformer = TfidfTransformer()
set_E_tfidf = tfidf_transformer.fit_transform(set_E_tf)
set_A_tfidf = tfidf_transformer.transform(set_A_tf)

# train the model
clf = MultinomialNB().fit(set_E_tfidf, news_train.target)

#do prediction
predicted = clf.predict(set_A_tfidf)
#print accuracy and other metrics
metrics = metrics.classification_report(news_test.target, predicted, target_names=news_test.target_names)
print(metrics)