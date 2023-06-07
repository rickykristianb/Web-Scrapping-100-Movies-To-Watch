import requests
from bs4 import BeautifulSoup
import html

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
title = soup.find_all(name="h3", class_="title")

movie_title = [movie.getText() for movie in title]
title = movie_title[::-1]
with open(file="movie_chart.txt", mode="w", encoding="utf-8") as chart_data:
    for moviess in title:
        chart_data.write(f"{moviess}\n")

# for text_title in title[::-1]:
#     try:
#         with open(file="movie_chart.txt", mode="a") as chart_data:
#             text = text_title.getText()
#             chart_data.write(f"{text}\n")
#     except UnicodeError as error:
#         print(error)
#         with open(file="movie_chart.txt", mode="a", encoding="utf-8") as chart_data:
#             text = text_title.getText()
#             chart_data.write(f"{text}\n")
#     print(text_title.getText())



