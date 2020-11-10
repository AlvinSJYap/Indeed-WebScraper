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

URL = "https://ca.indeed.com/jobs?q=Data+Analyst&l=Toronto%2C+ON"
page = req.get(URL)


print(page.text)

f = open("indeedSearch.txt", "x")
f.write(page.text)
f.close()
