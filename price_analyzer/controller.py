import json
import kaina24

with open('price_analyzer/products.json','w+') as file:
    print("file created")

search_model = str(input("modelio numeris: "))
kaina24.model_search(search_model)

# 210-AWVO   u2720q
data_received = kaina24.grab_and_scratch
