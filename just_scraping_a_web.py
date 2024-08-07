import re
from bs4 import BeautifulSoup

# save the web site and add the path to the below.

file_path = '/path/to/ins.html'  

try:
    with open(file_path, 'r') as file:
        file_content = file.read()
        html = file_content
        soup = BeautifulSoup(html, 'html.parser')
        raw_text = soup.get_text()
        all_words = re.findall(r'\w+', raw_text)
        c = 0
        for i in all_words:
            c+=1
            print(i, end=" ")
            if(c==10):
                print()
                c=0

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError as e:
    print(f"Error reading file '{file_path}': {e}")

