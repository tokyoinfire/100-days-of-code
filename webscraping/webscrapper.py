from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/500-greatest-movies/"

response = requests.get(URL)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name = "h2")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode = "w", encoding = "utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")