import requests
from bs4 import BeautifulSoup
import re
import urllib
from selenium import webdriver
import os

'''

https://www.google.com/search?q=test&client=safari&rls=en&sxsrf=ALiCzsZpAFvafGKiekztQ4TEF_DSjSgMYA:1655842600751&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiw8pWwrr_4AhWVmmoFHQzeB5wQ_AUoAXoECAEQAw&biw=1440&bih=717&dpr=2

/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img 

search xpath library


curl 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRK1H66AxIvEJ9Np-04UMsLGCp5REiB-M_KpRzGdcAxDDcuKluOGkU6AWRLBA&s' \
  -H 'authority: encrypted-tbn0.gstatic.com' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: no-cache' \
  -H 'pragma: no-cache' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: none' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36' \
  -H 'x-client-data: CJa2yQEIo7bJAQjBtskBCKmdygEIg/HKAQiUocsBCNvvywEI5oTMAQiLq8wBCImyzAEI8rPMAQiEtMwBCIa0zAEInbXMARirqcoB' \
  --compressed ;
curl 'https://encrypted-tbn0.gstatic.com/favicon.ico' \
  -H 'authority: encrypted-tbn0.gstatic.com' \
  -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: no-cache' \
  -H 'pragma: no-cache' \
  -H 'referer: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRK1H66AxIvEJ9Np-04UMsLGCp5REiB-M_KpRzGdcAxDDcuKluOGkU6AWRLBA&s' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: image' \
  -H 'sec-fetch-mode: no-cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36' \
  -H 'x-client-data: CJa2yQEIo7bJAQjBtskBCKmdygEIg/HKAQiUocsBCNvvywEI5oTMAQiLq8wBCImyzAEI8rPMAQiEtMwBCIa0zAEInbXMARirqcoB' \
  --compressed

'''


URL = "https://aucaparthistory.wordpress.com/the-250/"
page = requests.get(URL)
text = page.text
soup = BeautifulSoup(text, 'html.parser')


art_list_OG = []

for ol_tags in soup.find_all("div"):
    for li_tags in ol_tags.find_all("li"):
        li_tags = str(li_tags)
        if li_tags.startswith("<li>"):
            art_list_OG.append(li_tags)

art_list_with_tags = []

for i in art_list_OG:
    if i not in art_list_with_tags:
        art_list_with_tags.append(i)

art_list_with_spaces = []

for art in art_list_with_tags:
    if art.startswith("<li><em>"):
        art_list_with_spaces.append(art[11: len(art) - 6])
    else:
        art_list_with_spaces.append(art[8: len(art) - 6])

art_list = []

for tags in art_list_with_spaces:
    if tags.startswith(" "):
        art_list.append(tags[1: len(tags)])
    elif tags.startswith(" </em>"):
        art_list.append(tags[6: len(tags)])
    elif tags.startswith(". "):
        art_list.append(tags[2: len(tags)])
    elif tags.startswith(". </em><em>"):
        art_list.append(tags[11: len(tags)])
    elif tags.startswith(" </em>"):
        art_list.append(tags[6: len(tags)])
    elif tags.startswith(". </em><em>"):
        art_list.append(tags[11: len(tags)])
    else:
        art_list.append(tags)

# for view2 in art_list:
#     print(view2)
#     print(" ")

art_name = []

for name in art_list:
    name = re.split("[<.]", name, 1)
    art_name.append(name[0])

# for view3 in art_name:
#     print(view3, "\n")
#
# print(len(art_name))

# link_list = []
#
# for art_piece in art_name:
#     for link in search(str(art_piece) + " khan academy", tld="com", stop=1):
#         print(link)
#         link_list.append(link)

# images = []
#
# for khan in link_list:
#     khan_page = requests.get(khan)
#     khan_text = khan_page.text
#     khan_soup = BeautifulSoup(khan_text, 'html.parser')
#
#     check = False
#
#     while check is not True:
#         for img in khan_soup.findAll('img'):
#             images.append(img.get('src'))
#             print(img)
#             if len(images) == 1:
#                 check = True

#                 ACTUAL CODE DOWN HERE
# link = "https://www.google.com/search?q=" + "hall of the bulls" + "&source=lnms&tbm=isch"
# page2 = requests.get(link)
# text2 = page2.text
# image_soup = BeautifulSoup(text2, 'html.parser')
#
# image_list = []
#
# for image_link in image_soup.find_all("img"):
#     image_list.append(image_link.get("src"))
#
# print(image_list[2])
#
# urllib.request.urlretrieve(image_list[2], str(image_list[2]) + ".jpg")

#              END OF ACTUAL CODE

# for image_name in art_name:
#     URL2 = "https://www.google.com/search?q=" + image_name + "&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjPnP6hl9P2AhUQmuAKHcN1ArAQ_AUoAXoECAEQAw"
#     page2 = requests.get(URL2)
#     text2 = page2.text
#     image_soup = BeautifulSoup(text2, 'html.parser')
#
#     image_soup.prettify()
#
#     print(image_soup)

# #for art in art_name:
# driver.get("https://www.google.com/search?q=" + "apolla 11 stones" + "&source=lnms&tbm=isch")
# html = driver.page_source
# image_soup = BeautifulSoup(html, 'html.parser')
# image_soup.prettify()

repeat = 0
for view in art_name:
    print(view)
for image_name in art_name:
    repeat = repeat + 1
    link = "https://www.google.com/search?q=" + image_name + "&source=lnms&tbm=isch"
    page2 = requests.get(link, {'authority': 'encrypted-tbn0.gstatic.com'})
    text2 = page2.text
    image_soup = BeautifulSoup(text2, 'html.parser')

    art_images = []

    for image in image_soup.findAll("img"):
        art_images.append(image.get('src'))

    print("Adding", image_name, "to the file...")

    print(art_images)

    try:
        real_image = art_images[1]
    except:
        print(art_images)
        print(image)
        print(image_name)
        break
    fh = open("/Users/Daniel/Documents/Art_Images/arts.txt", "a+")
    fh.write(str(repeat) + ". " + str(real_image) + "\n")
    fh.write("\n")
