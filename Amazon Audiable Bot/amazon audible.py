from selenium import webdriver
import pandas as pd

web = 'https://www.audible.com/search'
# path of my chrome driver
path = '/Applications/chromedriver_mac_arm64/chromedriver'
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

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
df_books.to_csv('books.csv', index=False)








