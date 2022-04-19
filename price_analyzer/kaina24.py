from bs4 import BeautifulSoup as BF
import requests
import time

search_model = str(input("modelio numeris: "))
search_model_fixed = search_model.replace(" ", "+")
main_url = "https://www.kaina24.lt/"
page = 2 

super_link = main_url + "search?q=" + search_model_fixed
request_data = requests.get(super_link, headers={"User-Agent": "Mozilla/5.0"})
soup = BF(request_data.text, "html.parser")

# paginator check
while True:
    time.sleep(7)
    paginator_link = super_link + "&page=" + str(page)
    paginator_check = soup.find("a", {"href": paginator_link })
    request_data = requests.get(paginator_link, headers={"User-Agent": "Mozilla/5.0"})
    soup = BF(request_data.text, "html.parser")
    page += 1
    if paginator_check != None:
        print("\nCONTINUE linkas egzistuoja: ", paginator_link)
        continue
    else:
        print("\nBREAK nera linko: ", paginator_link)
        break
    

# print(super_link)

# def grab_and_scratch(super_link):
#     request_data = requests.get(super_link, headers={"User-Agent": "Mozilla/5.0"})
#     soup = BF(request_data.text, "html.parser")
#     main_content = soup.findAll("div", {"class": "product-item-h"})

#     print(main_content)

# grab_and_scratch(super_link)