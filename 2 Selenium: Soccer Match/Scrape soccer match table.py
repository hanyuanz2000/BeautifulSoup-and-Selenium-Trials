from selenium import webdriver
import pandas as pd

website = 'https://www.adamchoi.co.uk/overs/detailed'
# path of my chrome driver
path = '/Applications/chromedriver_mac_arm64/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)

# click the all match button to get a single table
all_matches_button = driver.find_element_by_xpath("//label[@analytics-event='All matches']")
all_matches_button.click()

# put all information of a match into a single string
matches = driver.find_elements_by_tag_name('tr')
for match in matches[:3]:
    print(match.text)
    # results is in form: 12-03-2023 Newcastle 3 - 2 Wolves
    # all text inside tr will be included

# We can also use xpath to separately store different info
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
df.to_csv('premier league matches.csv', index=False)

# don't forget to di it!
driver.quit()
