import json
import kaina24
import sql_data_base as sql

# overwrite file
# with open('price_analyzer/products.json','w+') as file:
#     print("file created")

sql.PriceAnalyzer

def searcher():
    # kaina24.model_search(search_model)

    with open('price_analyzer/products.json', 'r') as myfile:
        data=myfile.read()
        obj = json.loads(data)

    all_prices = []

    for json_single in obj:
        all_prices.append(json_single[1])
    lowest_price_arr = min(all_prices)

    for json_single in obj:
        if lowest_price_arr == json_single[1]:
            final_product = json_single
            break
        else:
            continue
    return final_product
    # print("LOWEST PRICE: ", final_product)

if __name__ == '__main__':
    searcher() 

# 210-AWVO   u2720q

# search_model = str(input("modelio numeris: "))
# searcher(search_model)
# searcher()
