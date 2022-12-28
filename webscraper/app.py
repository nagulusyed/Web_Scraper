from bs4 import BeautifulSoup
import requests

# Send an HTTP request to the website
response = requests.get('https://timesofindia.indiatimes.com/?from=mdr')

# Parse the HTML of the website
soup = BeautifulSoup(response.text, 'html.parser')

# Find the title of each article
titles = soup.find_all('h1')

# Save the titles to a file
with open('titles.txt', 'w') as f:
    for title in titles:
        f.write(title.text + '\n')
