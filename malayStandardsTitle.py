import requests
import pandas as pd
from lxml import html

print("script started >>>")

base_url = 'https://mysol.jsm.gov.my/search-catalogue?is-advance=1&sector=216&page='
page_number = 1

def fetch_data(url):
    try:
        response = requests.get(url)
        tree = html.fromstring(response.content)
        return tree         

    except Exception as e:
        return str(e)
    
results = []

while True:
    url = f"{base_url}{page_number}"
    tree = fetch_data(url)

    # check if there's data on the page using xpath
    if not tree.xpath('/html/body/div[3]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/h5/a/b/text()'):
        break

    # process the data using xpath
    data = tree.xpath('/html/body/div[3]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/h5/a/b/text()')
    for item in data:
        results.append(item.strip())
            
    page_number +=1

# create a data frame 
df = pd.DataFrame(results, columns=['Data'])

# save the data frame to excel
df.to_excel('D:/workbench/malay2/results.xlsx', index = False)

print("data has been successfully saved to results")