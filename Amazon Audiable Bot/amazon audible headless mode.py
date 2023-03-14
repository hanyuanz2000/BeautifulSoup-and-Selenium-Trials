from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
# activate headless mode
options.headless = True
# we add the below line because in headless mode, driver.maximize_window() doesn't work very well
options.add_argument('window-size=1920x1080')

web = 'https://www.audible.com/search'
path = '/Applications/chromedriver_mac_arm64/chromedriver'
# note below we add options argument
driver = webdriver.Chrome(path, options=options)
driver.get(web)

# we comment out the below line because we already added window-size=1920x1080 argument above
# driver.maximize_window()

container = driver.find_element_by_class_name('adbl-impression-container')
products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')

book_title = []
book_author = []
book_length = []

for product in products:
    title = product.find_element_by_xpath('.//h3[contains(@class,"bc-heading")]').text
    book_title.append(title)

    author = product.find_element_by_xpath('.//li[contains(@class,"authorLabel")]').text
    book_author.append(author)

    length = product.find_element_by_xpath('.//li[contains(@class,"runtimeLabel")]').text
    book_length.append(length)

driver.quit()
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books_headless.csv', index=False)








