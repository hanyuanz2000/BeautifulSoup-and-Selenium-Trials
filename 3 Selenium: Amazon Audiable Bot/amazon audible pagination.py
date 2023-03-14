from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

options = Options()
# deactivate headless mode
options.headless = False
# we add the below line because in headless mode, driver.maximize_window() doesn't work very well

web = 'https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=8a113f1a-dc38-418d-b671' \
      '-3cca04245da5&pf_rd_r=JW5BV9V8VTM7CYH84NQ2&pageLoadId=ZCtF7Ed8DInNXNWr&creativeId=1642b4d1-12f3-4375-98fa' \
      '-4938afc1cedc'
path = '/Applications/chromedriver_mac_arm64/chromedriver'
# note below we add options argument
driver = webdriver.Chrome(path, options=options)
driver.get(web)
driver.maximize_window()

# pagination
pagination = driver.find_element_by_xpath('//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements_by_tag_name('li')  # same as //ul[contains(@class, "pagingElements")]/li
last_page = int(pages[-2].text)  # one position before >

current_page = 1
book_title = []
book_author = []
book_length = []

while current_page <= last_page:  # stop when we reach the final page: page 60
    # implicit wait
    # time.sleep(3)

    # explicit wait, more robust
    container = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'adbl-impression-container')))
    products = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, './/li[contains(@class, "productListItem")]')))

    for product in products:
        title = product.find_element_by_xpath('.//h3[contains(@class,"bc-heading")]').text
        book_title.append(title)

        author = product.find_element_by_xpath('.//li[contains(@class,"authorLabel")]').text
        book_author.append(author)

        length = product.find_element_by_xpath('.//li[contains(@class,"runtimeLabel")]').text
        book_length.append(length)

    current_page += 1
    try:
        next_page = driver.find_element_by_xpath('//span[contains(@class, "nextButton")]')
        next_page.click()

    except:
        pass

driver.quit()
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books_best_sell.csv', index=False)
