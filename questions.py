import xml.etree.ElementTree as ET
import random
import os
import time
import numpy as np
from operator import itemgetter
read_path = 'C:/Users/evans/OneDrive/Desktop/Language_Technology/html_pages/'
entries = os.listdir(read_path)
# load xml to dictionary
inverted_index = r"index.xml"
tree = ET.parse(inverted_index)
all_lemmas = tree.findall("./lemma")

index_dictionary = {}
user_input = []

# iterate trough all the lemma tags
i = 0
for cur_lemma in all_lemmas:
    name = cur_lemma.get('name')
    cur_documents = cur_lemma.findall("./document")
    # select random 150 words for the queries
    r = random.randint(1, 100)
    if i <= 150 and r < 10:
        user_input.append(name)
        i += 1
        # iterate trough all the document tags for every lemma
    for doc in cur_documents:
        ide = doc.get('id')
        weight = doc.get('weight')
        tup = [int(ide), float(weight)]
        if weight in user_input:
            print('in')
        if name in index_dictionary:
            index_dictionary[name].append(tup)
        else:
            index_dictionary[name] = [tup]
# start timer
start = time.time()

#20 queries with 1 word
result1=[]
for i in range(0, 20):
    for k_index,v_index in index_dictionary.items():
        if k_index == user_input[i]:
            for z in v_index: 
                #print(i[1],i[0],entries[i[0]])     
                query1_result = [z[1],z[0],entries[z[0]]]
                result1.append(query1_result)
                result1 = sorted(result1, key=itemgetter(0), reverse=True)    
for line in result1:
    print(*line)
print("-------------------------------------------------------------------------------")
#20 queries with 2 words
result2= []
for i in range(0,20):
    random_number = random.randint(1, 150)
    w1 = user_input[random_number]
    random_number = random.randint(1, 150)
    w2 = user_input[random_number]
    w1_info = index_dictionary[w1]
    w2_info = index_dictionary[w2]
    for id1 in w1_info:
        for id2 in w2_info:
            if id1[0]==id2[0]:
                weights_sum = float(id1[1]+id2[1])
                query2_result = [id2[0],weights_sum,entries[id2[0]]]
                result2.append(query2_result)
                result2 = sorted(result2,key=itemgetter(1), reverse=True)
print("               20 queries with 2 words")
print("-------------------------------------------------------------------------------")
for line in result2:
    print(*line)
print("-------------------------------------------------------------------------------")
#30 queries with 3 words
result3= []
for i in range(0,30):
    random_number = random.randint(1, 150)
    w1 = user_input[random_number]  
    random_number = random.randint(1, 150)
    w2 = user_input[random_number]
    random_number = random.randint(1, 150)
    w3 = user_input[random_number]
    w1_info = index_dictionary[w1]
    w2_info = index_dictionary[w2]
    w3_info = index_dictionary[w3]      
    for id1 in w1_info:
        for id2 in w2_info:
            for id3 in w3_info:
                if id1[0]==id2[0]==id3[0]:
                    weights_sum = float(id1[1]+id2[1]+id3[1])
                    query3_result = [id3[0],weights_sum,entries[id3[0]]]
                    result3.append(query3_result)
                    result3 = sorted(result3,key=itemgetter(1), reverse=True)
print("               30 queries with 3 words")
print("-------------------------------------------------------------------------------")
for line in result3:
    print(*line)
print("-------------------------------------------------------------------------------")               
#30 queries with 4 words
result4= []
for i in range(0,30):
    random_number = random.randint(1, 150)
    w1 = user_input[random_number]  
    random_number = random.randint(1, 150)
    w2 = user_input[random_number]
    random_number = random.randint(1, 150)
    w3 = user_input[random_number]
    random_number = random.randint(1, 150)
    w4 = user_input[random_number]
    
    w1_info = index_dictionary[w1]
    w2_info = index_dictionary[w2]
    w3_info = index_dictionary[w3]
    w4_info = index_dictionary[w4]     
    for id1 in w1_info:
        for id2 in w2_info:
            for id3 in w3_info:
                for id4 in w4_info:
                    if id1[0]==id2[0]==id3[0]==id4[0]:
                        weights_sum = float(id1[1]+id2[1]+id3[1]+id4[1])
                        query4_result = [w1,w2,w3,w4,id3[0],weights_sum,entries[id3[0]]]
                        result4.append(query4_result)
                        result4 = sorted(result4,key=itemgetter(1), reverse=True)
print("               30 queries with 4 words")
print("-------------------------------------------------------------------------------")
for line in result4:
    print(*line)
print("-------------------------------------------------------------------------------")  

# end timer
end = time.time()
final = end - start

print("Average response time: ", final/100)