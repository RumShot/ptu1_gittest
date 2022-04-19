from bs4 import BeautifulSoup as BF
import requests
import time
import json
import re

search_model = str(input("modelio numeris: "))
search_model_fixed = search_model.replace(" ", "+")
main_url = "https://www.kaina24.lt/"
page = 2 

super_link = main_url + "search?q=" + search_model_fixed
request_data = requests.get(super_link, headers={"User-Agent": "Mozilla/5.0"})
soup = BF(request_data.text, "html.parser")

# 210-AWVO
def grab_and_scratch():
    main_content = soup.findAll("div", {"class": "product-item-h"})
    for product in main_content:
        print("------------")
        # icon
        icon_block = product.find("p", {"class": "shop"})
        icon_url = icon_block.find("img", {"class": "lazy"})
        print("Icon URL: ", icon_url["data-src"])
        # url
        product_block = product.find("p", {"class": "name"})
        product_onclick = product_block("a", {"rel": "nofollow"})
        product_url = product_onclick[0].get("onclick")
        final_url = re.search("(?P<url>https?://[^\s]+)", product_url).group("url")
        print("Product URL: ", final_url)
        # price
        price_block = product.find("p", {"class": "price"})
        price_with_currency = price_block(text=True)
        price = price_with_currency[0].replace(" €", "")
        print("Price:  ", price)
        # print(product)

# paginator check
while True:
    time.sleep(2)
    paginator_link = super_link + "&page=" + str(page)
    paginator_check = soup.find("a", {"href": paginator_link })
    request_data = requests.get(paginator_link, headers={"User-Agent": "Mozilla/5.0"})
    soup = BF(request_data.text, "html.parser")
    page += 1
    grab_and_scratch()
    if paginator_check != None:
        print("\nCONTINUE linkas egzistuoja: ", paginator_link)
        continue
    else:
        print("\nBREAK nera linko: ", paginator_link)
        break