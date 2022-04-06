import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

read_path = 'C:/Users/evans/OneDrive/Desktop/Language_Technology/txt_files/'
write_path = 'C:/Users/evans/OneDrive/Desktop/Language_Technology/tag_files/'
openclasscategorytags = ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'NN', 'NNS', 'NNP','NNPS','VB','VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'FW']
entries = os.listdir(read_path)
txt_id = 0
for i in entries:
    r_sub_path = read_path + i    
    with open(r_sub_path, 'r',encoding="utf8") as f:
        this_file = f.read()
    NLP_tokens=word_tokenize(this_file)
    stop_words = stopwords.words("english") ##remove stop words from txt. for better pos tagging.
    other_stuff = [' ', ':', '.', ',','(',')','”','“','!','?','-','”','—','#','/','⟶','“','’','@',';','*','[',']','$','%','+','`','...','....','..','<','>']
    stop_words.extend(other_stuff)
    filtered_sen = []
    for w in NLP_tokens:
        if w not in stop_words:
            w = w.split(".")[0] #remove words that are like that : a.b or a. and keeps only a
            filtered_sen.append(w)

    tagged = nltk.pos_tag(filtered_sen)
    tag_name = write_path + str(txt_id)

    with open(tag_name, 'w',encoding="utf8") as f:
        for i in tagged:
            if i[1] in openclasscategorytags:
                f.write(i[0] + '\t' + i[1] + '\n')
    f.close()
    txt_id = txt_id + 1
