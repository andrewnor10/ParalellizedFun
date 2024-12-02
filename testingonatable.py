import requests 
import bs4

request = requests.get("https://cs111.byu.edu/Projects/project04/assets/data.html")
soup = bs4.BeautifulSoup(request.content)

table = soup.find_all('table')[0]
heads = table.find_all('th')
headers = [item.string for item in heads]
rows = table.find_all('tr')
data = []
for row in rows:
    data.append([])
    columns = row.find_all('td')
    for datas in columns:
        data[-1].append(datas.string)

print(data)