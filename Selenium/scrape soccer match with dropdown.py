from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Applications/chromedriver_mac_arm64/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)

# click the all match button to get a single table
all_matches_button = driver.find_element_by_xpath("//label[@analytics-event='All matches']")
all_matches_button.click()

dropdown = Select(driver.find_element_by_id('country'))
target_country = 'Spain'
dropdown.select_by_visible_text(target_country)

# wait browser to load
time.sleep(5)

matches = driver.find_elements_by_tag_name('tr')
date = []
home_team = []
score = []
away_team = []
for match in matches:
    # match is actually //tr
    date.append(match.find_element_by_xpath('./td[1]').text)  # 12-03-2023
    home_team.append(match.find_element_by_xpath('./td[2]').text)  # Newcastle
    score.append(match.find_element_by_xpath('./td[3]').text)  # 3 - 2
    away_team.append(match.find_element_by_xpath('./td[4]').text)  # Wolves

# export to csv
df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv(f'{target_country} league matches.csv', index=False)

# don't forget to di it!
driver.quit()
