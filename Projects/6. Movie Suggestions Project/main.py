import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response=requests.get(URL)
web=response.text
soup=BeautifulSoup(web, "html.parser")
#allmovie=soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
allmovie=soup.find_all(name="h3", class_="title")
title=[movie.getText() for movie in allmovie]
movies=title[::-1] #splice operation
with open("movies.text", mode="w") as file:
    for m in movies:
        file.write(f"{m}\n") 