from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url = 'https://www.beeradvocate.com/lists/top/'

#server blocks known bot user agents, need to set as a known browser user agent
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

#open page, dump html into a variable, then close
uClient = urlopen(req)
page_html = uClient.read()
uClient.close()

#allow BeautifulSoup to run through html
page_soup = soup(page_html, "html.parser")


#find the table that has all the data, and delete extraneous data
table = page_soup.findAll("tr")
del table[:2] 

#create a .csv file to load data into that has a header
filename = "top_beers.csv"
f = open(filename, "w")
headers = "beer_name, brewery, style, score\n"
f.write(headers)

#loop through table rows and extract relevant data
for table_row in table:
	cells = table_row.find_all('td')
	beer_name= cells[1].a.get_text()
	sub_cell = cells[1].div.find_all('a')
	brewery = sub_cell[0].get_text()
	style   = sub_cell[1].get_text()
	score   = cells[2].get_text()

	f.write(beer_name + "," + brewery + "," + style + "," + score + "\n")

f.close()
	


