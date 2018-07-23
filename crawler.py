import requests 
from bs4 import BeautifulSoup 
import os
import re

os.makedirs('./img/', exist_ok=True)
baseurl = 'https://hello-aiueo.com/gift/'
count = 1

for page in range(1,35):
    url = baseurl + 'page/' + '%s' %page +'/'
    site = requests.get(url) 
    soup = BeautifulSoup(site.text, 'html.parser')
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile(".*?\.jpg")})

    for hqimg in sub_urls:
        hqimg_url = hqimg['href']
        temhqimg_name = hqimg_url.split('/')[-1]
        r = requests.get(hqimg_url)
        m = re.search(".*?\.jpg", temhqimg_name)
        if m:
            img_name = m.group(0)

        with open('./img/%s' %img_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print( count, 'Saved %s' %img_name)
        count += 1