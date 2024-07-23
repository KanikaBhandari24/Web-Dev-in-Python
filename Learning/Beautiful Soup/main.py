from bs4 import BeautifulSoup #bs4 latest version of beautiful soup library
#import lxml
with open("/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/Web dev Projects in Python/5. Beautiful Soup Project/website.html", encoding="utf-8") as file:
    contents=file.read()
soup=BeautifulSoup(contents,"html.parser")
print(soup.title) 
print(soup.title.string)
a=soup.find_all(name="a")
for tag in a:
    print(tag.getText()) 