from bs4 import BeautifulSoup as BF
import requests
import time
import re
import json


def model_search(search_model):
    search_model_fixed = str(search_model).replace(" ", "+")
    main_url = "https://www.kaina24.lt/"
    super_link = main_url + "search?q=" + search_model_fixed
    request_data = requests.get(super_link, headers={"User-Agent": "Mozilla/5.0"})
    soup = BF(request_data.text, "html.parser")
    page = 2
    paginator(super_link,page,soup)

# 210-AWVO   u2720q
def grab_and_scratch(soup):
    data_array = []
    main_content = soup.findAll("div", {"class": "product-item-h"})
    for product in main_content:
        # print("------------")
        # image
        try:
            img_block = product.find("a", {"class": "image-wrap"})
            img_url = img_block.find("img", {"class": "lazy"})
            image = img_url["data-src"]
        except TypeError:
            image = "None"
        # print("Image URL: ", image)
        # icon
        try:
            icon_block = product.find("p", {"class": "shop"})
            icon_url = icon_block.find("img", {"class": "lazy"})
            icon = icon_url["data-src"]
        except TypeError:
            icon = "None"
        # print("Icon URL: ", icon)
        # url
        product_block = product.find("p", {"class": "name"})
        product_onclick = product_block("a", {"rel": "nofollow"})
        final_url = product_onclick[0].get("onclick")
        product_url = re.search("(?P<url>https?://[^\s]+)", final_url).group("url")
        # name

        # FIX ME HERE

        named_text = product_block(text=True)
        full_name = str(named_text).replace("\"", "inch").replace("<b>", "").replace("</b>", "").replace("/", "|")
        # print("Product URL: ", product_url)
        # price
        price_block = product.find("p", {"class": "price"})
        price_with_currency = price_block(text=True)
        price = price_with_currency[0].replace(" €", "")
        # print("Price:  ", price)
        data = [full_name, price, product_url, image, icon]
        # print(data)
        data_array.append(data)
    with open('price_analyzer/products.json','r+') as file:
        json.dump(data_array, file, indent = 5)

# paginator check
def paginator(super_link,page,soup):
    while True:
        time.sleep(2)
        paginator_link = super_link + "&page=" + str(page)
        paginator_check = soup.find("a", {"href": paginator_link })
        request_data = requests.get(paginator_link, headers={"User-Agent": "Mozilla/5.0"})
        soup = BF(request_data.text, "html.parser")
        page += 1
        grab_and_scratch(soup)
        if paginator_check != None:
            print("\nCONTINUE linkas egzistuoja: ", paginator_link)
            continue
        else:
            print("\nBREAK nera linko: ", paginator_link)
            break

# search_model = str(input("modelio numeris: "))
# model_search(search_model)