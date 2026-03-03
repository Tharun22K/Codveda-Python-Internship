import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("span", class_="titleline")

    with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Headlines"])

        for title in titles:
            writer.writerow([title.text])

    print("Headlines saved to headlines.csv")
else:
    print("Failed to fetch website")
