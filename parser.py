import os
from bs4 import BeautifulSoup

read_path = 'C:/Users/evans/OneDrive/Desktop/Language_Technology/html_pages/'
write_path = 'C:/Users/evans/OneDrive/Desktop/Language_Technology/txt_files/'
entries = os.listdir(read_path)
txt_file = []
for i in entries:
    r_sub_path = read_path + i
    with open(r_sub_path, 'rb') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
    f.close()
    txt_name = write_path + i + '.txt'
    only_text = open(txt_name,"w",encoding="utf8")
   
    for div in soup.find_all('div', class_='c-entry-content'):
        for p in div.find_all('p'):
            txt_file = p.text
            only_text.write(txt_file)       
    only_text.close()
