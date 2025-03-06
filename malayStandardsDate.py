import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import etree

print("script started >>>>>")

# loading the excel file
df = pd.read_excel("D:/workbench/malay/121.xlsx")

# function to get status from excel
def get_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            dom = etree.HTML(str(soup))
            xpath_result = dom.xpath('//*[@id="code"]/text()')
            sixth_element = xpath_result[5]
            return sixth_element
        else:
            return "URL not accessible"
    except Exception as e:
        return str(e)
    
# applying the function to each row and adding a new column
df['date'] = df["Links"].apply(get_status)

# save the updated data to a new excel file
df.to_excel("D:/workbench/malay/121_updated.xlsx", index=False)

print("script Ended")