
import os
import requests
from bs4 import BeautifulSoup
import imghdr


BASE_URL = "https://sites.google.com/site/mtgbasics/home/"
LAND_TYPES = ['island', 'swamp', 'forest', 'mountain', 'plains']


def download_image(image_url, file_out):
    if os.path.isfile(file_out):
        pass
    else:
        img_data = requests.get(image_url)
        with open(file_out, 'wb') as handler:
            handler.write(img_data.content)
        file_type = imghdr.what(file_out)
        if file_type is None:
            print(image_url, 'failed to download')
            os.remove(file_out)
        else:
            print(image_url)


for land in LAND_TYPES:

    url = BASE_URL + land
    html_blob = requests.get(url).content
    soup = BeautifulSoup(html_blob)

    img_tags = soup.find_all('img')
    img_links = [tag['src'] for tag in img_tags]

    for i, link in enumerate(img_links):
        file_out = 'img/' + land + '_' + str(i)
        download_image(link, file_out)
