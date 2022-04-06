import os
import numpy as np
import csv
from nltk.stem import WordNetLemmatizer
read_path = 'C:/Users/evans/OneDrive/Desktop/Language_Technology/tag_files/'
entries = os.listdir(read_path)
lemmatizer = WordNetLemmatizer()
all_txts = []
#loop through all tag txt files in folder.
for e in entries:
    sub_path = read_path + e 
    if os.stat(sub_path).st_size != 0:
        with open(sub_path, encoding="utf8") as f:
            my_List = list(csv.reader(f, delimiter='\t')) #we read as csv because its like a table structed txt files
        f.close()
    else:
        continue   
    # convert list to array
    tagsArr = np.array(my_List)    
    all_txts.append(np.char.lower(tagsArr))    #make all chars lowrcase for better indexing   

################# frequensies #############################################
all_frequencies = {} #dictionary for ALL lemanized word frequencies
i = 0
for all in all_txts:
    txt_freq = {} #dictionary per tag file for lemanized word frequency
    for w in all:
        word = w[0]
        word = lemmatizer.lemmatize(word)
        if word in txt_freq:
            txt_freq[word] += 1
        else:
            txt_freq[word] = 1
    all_frequencies[i] = txt_freq
    i = i + 1
