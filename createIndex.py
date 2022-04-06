import os
from preprocessing import all_frequencies

###################################### tf calculation  ####################
#TF = (Frequency of the word in the txt file) / (Total number of words in the txt file)
def comptuteTF(dictionary):
    TF= {} #dictionary for all txts word TF calculation
    i = 0
    for key, value in all_frequencies.items():
        tf_per_txt_file = {} #dictionary per txt file for word TF calculation
        count_words_per_txt = len(value)
        for word, count in value.items(): #count is the value of the key in the dictionary therefore the frequency of the word
            tf_per_txt_file[word] = count / count_words_per_txt
        TF[i] = tf_per_txt_file
        i = i + 1
    return TF

############################ idf calculation ##################################
#IDF: (Total number of txt files)/(Number of txt files containing each word)
def comptuteIDF(dictionary):
    import math
    word_per_txt = {} #dictionary for count appearance of words per  tag txt file
    for sentence, f_table in all_frequencies.items():
        for word, count in f_table.items():
            if word in word_per_txt:
                word_per_txt[word] += 1
            else:
                word_per_txt[word] = 1

    total_txts = len(all_frequencies)  #total number of texts files(sentences)

    IDF = {}
    i = 0
    for sent, f_table in all_frequencies.items():
        idf_table = {}
        for word in f_table.keys():
            idf_table[word] = math.log10(total_txts / float(word_per_txt[word]))
        IDF[i] = idf_table
        i = i + 1
    return IDF

################################# tfidf calculation ######################
def comptuteTFIDF(tf,idf):
    TF_IDF = {}
    i = 0
    for w , tf_value in tf.items():
        tfidf = {}
        for word,val in tf_value.items():
            tfidf[word] = float(val*idf[w][word])
        TF_IDF[i] = tfidf
        i = i + 1
    return TF_IDF

################ create the index dictionary to parse in the xml #################
def create_index(tfidf):
    from preprocessing import entries
    index = {}
    #txt_id is stored the text file id --> entries all the txt files
    for (w, tfidf_value), txt_id in zip(calculate_tfidf.items(), entries):
        for word, weight in tfidf_value.items():
            descr = [str(txt_id), weight]
            if word in index:
                # append new document id with weight if lemma already exist in dictionary
                index[word].append(descr)
            else:
                # add the new lemma to the index
                index[word] = [descr]
    return index

################ run the functions ###############
calculate_tf = comptuteTF(all_frequencies)
calculate_idf = comptuteIDF(all_frequencies)
calculate_tfidf = comptuteTFIDF(calculate_tf,calculate_idf)
dictionary_index = create_index (calculate_tfidf)

############ create xml file and parse the dictionary ################
name = 'index.xml'
with open(name, 'w', encoding='utf8') as xml_file:
    xml_file.write('<inverted_index>\n')

    for lemma, entries in dictionary_index.items():
        line = '<lemma name='+'"'+lemma+'"'+'>\n'
        xml_file.write(line)

        for i in entries:
            line = '\t<document id= "' + str(i[0]) + '"' + ' weight= "' + str(i[1]) + '"' + '/>\n'
            xml_file.write(line)

        xml_file.write('</lemma>\n')

    xml_file.write('</inverted_index>')

xml_file.close()