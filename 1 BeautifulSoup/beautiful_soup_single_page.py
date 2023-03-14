from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text
# print(content)

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_='main-article')

title = soup.find('h1').get_text()
title = box.find('h1').get_text()
# both works, 2nd one excludes all things outside the box
print(title)

transcript = soup.find('div', class_='full-script').get_text(strip=True, separator=' ')
# strip delete space in leading space, separator replace new line with blank space
# this makes it easier to save to file
print(transcript)

with open(f'{title}.txt', 'w') as file:
    file.write(transcript)

