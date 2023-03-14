# Web scrapping Trials
In this repository, we are trying to test the functions of different major web-scrapping tools, 
including BeautifulSoup, Selenium, and Scrappy. 

Since the html structure of websites may change, I will also include some output result in each folder.
## part 1 BeautifulSoup
In this part, we conduct experiments to test how BeautifulSoup works. Our target website is https://subslikescript.com. 
We are trying to scrape the scripts for different movies. 
We implement below functions: use pagination to enter each page of the target website. 
For each movie inside each page, 
we enter its corresponding page to scrape its scripts 
and store the results in txt files.

## part 2 Selenium: Soccer Match
In this part, we conduct experiments to test how Selenium works. Our target website is https://www.adamchoi.co.uk/overs/detailed.
We are trying to scrape the results of 22-23 season premier league & La Liga matches.
We implement the function to select dropdown and scrap information from tables.

## part 3 Selenium: Amazon Audible Bot
In this part, we conduct experiments to further test how Selenium works with Xpath. 
Our target website is https://www.audible.com/search.
We are trying to gather the information of name, author, book length for each audible book.
We include headless mode of Selenium and implement pagination function in this part.
