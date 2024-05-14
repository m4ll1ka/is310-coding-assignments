import requests
import csv
from bs4 import BeautifulSoup
print('hiiii')
soup = BeautifulSoup(open("humanist_homepage.html"), features="html.parser")
#print(soup.prettify())
links = soup.find_all('a')
#for link in links:
#    print(link)

response = requests.get("https://humanist.kdl.kcl.ac.uk/")

#print(response.status_code)
#print(response.headers)

with open('humanist_volumes.csv', 'w') as file:
    writer = csv.writer(file)
    # Write the headers
    writer.writerow(['Link', 'Volume Text'])
    for link in links:
        if "Archives" in link.get('href'):
            volume_url = "https://humanist.kdl.kcl.ac.uk" + link.get('href')
            volume_response = requests.get(volume_url)
            volume_soup = BeautifulSoup(volume_response.text, "html.parser")
            writer.writerow([link.get_text(), volume_soup.get_text()])

print('done!')