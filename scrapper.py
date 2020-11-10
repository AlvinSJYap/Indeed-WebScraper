"""
Indeed Job Webscraper 
Built by: Alvin Yap
Inspiration - https://realpython.com/beautiful-soup-web-scraper-python/
"""


"""
Breakdown of url:https://ca.indeed.com/jobs?q=data+analyst&l=Toronto%2C+ON
-https://ca.indeed.com/ = main body
-jobs? = start
- q=data+analyst&l=Toronto%2C+ON
q=data+analyst  is the search for the position
l=Toronto%2C+ON is the location (before the %2C+ is the city, after is the province)
& is the seperater

"""

import requests as req
from bs4 import BeautifulSoup

URL = "https://ca.indeed.com/jobs?q=Data+Analyst&l=Toronto%2C+ON"
page = req.get(URL)


soup = BeautifulSoup(page.content, 'html.parser')

#each posting has a job card and these cards have the jobsearch-serpjobcard class

job_cards = soup.findAll("div", {"class":"jobsearch-SerpJobCard"})

#for location, it can exist as both a span or a div for whatever reason

for job_elem in job_cards:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('span', class_='company')
    location_elem = job_elem.find(['div','span'], class_='location accessible-contrast-color-location')
    
    print(title_elem.text)
    print(company_elem.text)
    print(location_elem.text)

 
