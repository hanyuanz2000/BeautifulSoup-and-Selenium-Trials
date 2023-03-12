from bs4 import BeautifulSoup
import requests
import os

root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text
print(last_page)  # 1780

links = []
for page in range(1, int(last_page))[:1]:
    website = f'https://subslikescript.com/movies_letter-A?page={page}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_='main-article')
    for link in box.find_all('a', href=True):
        # href=True means we want to search for all elements with href attribute
        links.append(link['href'])
# print(links)

for link in links:
    try:
        website = f'{root}/{link}'
        print(website)
        result = requests.get(website)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')

        box = soup.find('article', class_='main-article')
        title = box.find('h1').get_text()
        transcript = soup.find('div', class_='full-script').get_text(strip=True, separator=' ')

        new_directory_path = './script_collection/'
        if not os.path.exists(new_directory_path):
            os.makedirs(new_directory_path)

        new_file_path = new_directory_path + f'{title}.txt'
        with open(new_file_path, 'w') as f:
            f.write(transcript)
    except:
        print('___something wrong with this link')
