from tkinter import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tkinter import ttk
from sql_data_base import PriceAnalyzer
import controller
import kaina24
import webbrowser
from PIL import ImageTk, Image
import requests
from io import BytesIO
import logging
import sql_data_base as sql


# LOG
logger = logging.getLogger(__name__)
logger_file = logging.FileHandler('info.log')
logger.addHandler(logger_file)
logger.setLevel(logging.INFO)
logger_formater = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)s:%(message)s')
logger_file.setFormatter(logger_formater)

# SQL DB
def data_base():
    sql.PriceAnalyzer

data_base()

# GUI
engine = create_engine('sqlite:///search_history.db')
Session = sessionmaker(bind=engine)
session = Session()

window = Tk()
window.title('Lowest Price Analyzer')
window.geometry("1390x600")

def refresh():
    children = tree.get_children()
    for child in children:
        tree.delete(child)
    tree_id = [r.id for r in session.query(PriceAnalyzer.id)]
    for single_read in tree_id:
        tree_input = session.query(PriceAnalyzer.sql_input).filter(PriceAnalyzer.id == single_read).first()
        tree_name = session.query(PriceAnalyzer.sql_name).filter(PriceAnalyzer.id == single_read).first()
        tree_price = session.query(PriceAnalyzer.sql_price).filter(PriceAnalyzer.id == single_read).first()
        tree_url = session.query(PriceAnalyzer.sql_url).filter(PriceAnalyzer.id == single_read).first()
        tree_time = session.query(PriceAnalyzer.sql_time).filter(PriceAnalyzer.id == single_read).first()
        tree.insert('', 'end', text="", values=(single_read, tree_input[0], tree_name[0],tree_price[0], tree_url[0], tree_time[0],))

def search_button():
    name_label['text']=f"Name: "
    price_label['text']=f"Lowest price: "
    url_label['text']=f"URL: "
    try:
        info_label["text"]=f"Searching please wait while we display results"
        controller.flush_json()
        search_model = input_entry.get()
        kaina24.model_search(search_model)
        try:
            final_product = controller.searcher()
        except:
            logger.info("Somethin is wrong with .json file or bad .json format")
        lowest_name = final_product[0]
        lowest_price = final_product[1]
        lowest_url = final_product[2]
        lowest_img = final_product[3]
        lowest_ico = final_product[4]
        name_label['text']=f"Name: {lowest_name}"
        price_label['text']=f"Lowest price:  {lowest_price}"
        url_label['text']=f"URL: {lowest_url}"
        info_label["text"]=f"Search complete"
        try:
            img_response = requests.get(lowest_img)
            img_data = img_response.content
            img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
            image_label.configure(image=img)
            image_label.image=img
        except ValueError:
            image_label["text"]=f"No image"
            logger.info("No image")
        try:
            ico_response = requests.get(lowest_ico)
            ico_data = ico_response.content
            ico = ImageTk.PhotoImage(Image.open(BytesIO(ico_data)))
            ico_label.configure(image=ico)
            ico_label.image=ico
        except ValueError:
            ico_label["text"]=f"No icon"
            logger.info("No image")
    except ValueError:
        info_label["text"]=f"No data received on input: {input_entry.get()}"
        logger.info("No text was added")

def remove_id():
    try:
        selected_id = remove_entry.get()
        if selected_id.isdigit():
            read_data = session.query(PriceAnalyzer).get(selected_id)
            session.delete(read_data)
            remove_entry.delete(0, 'end')
            session.commit()
            refresh()
            info_label["text"]=f"ID: {remove_entry.get()} was removed"
            remove_entry['text'] = ""
        else:
            info_label["text"]=f"Please insert digit"
    except:
        print(remove_entry.get())
        info_label["text"]=f"There's no such ID: {remove_entry.get()}"
        logger.info("There was no such ID")

def add_to_sql():
    try:
        from_input = input_entry.get()
        from_name = name_label.cget("text")[6:]
        from_price = price_label.cget("text")[15:]
        from_url = url_label.cget("text")[5:][:-2]
        to_sql_data = PriceAnalyzer(from_input, from_name, from_price, from_url,)
        session.add(to_sql_data)
        session.commit()
        input_entry.delete(0, 'end')
        refresh()
    except ValueError:
        logger.info("Nothing to add")

def open_url():
    open_link = url_label.cget("text")[5:][:-2]
    webbrowser.open_new_tab(open_link)

def selectItem(a):
    try:
        selected_input_entry.delete(0, 'end')
        selected_name_entry.delete(0, 'end')
        selected_price_entry.delete(0, 'end')
        selected_url_entry.delete(0, 'end')
        selected_time_entry.delete(0, 'end')
        curItem = tree.focus()
        selected_data = tree.item(curItem)
        selected_input_entry.insert(0,selected_data["values"][1])
        selected_name_entry.insert(0,selected_data["values"][2])
        selected_price_entry.insert(0,selected_data["values"][3])
        selected_url_entry.insert(0,selected_data["values"][4])
        selected_time_entry.insert(0,selected_data["values"][5])
    except IndexError:
        print("first always a miss")

tree_style = ttk.Style()
tree_style.theme_use('clam')

frame = Frame(window)
# row2
empty_row = Label(text="")
input_label = Label(text="Input Model")
input_entry = Entry(window, width= 30)
search_btn = Button(width = 8, text="Search")
search_btn.bind("<Button-1>", lambda event: search_button())
name_label = Label(text="Name: ", padx= 10, wraplength=650)
# images insert
image_label = Label(window, text="")
ico_label = Label(window, text="")
# row3
empty_row2 = Label(text="")
remove_label = Label(text="ID")
remove_entry = Entry(window, width= 30)
remove_btn = Button(width = 8, text="Remove")
remove_btn.bind("<Button-1>", lambda event: remove_id())
price_label = Label(text="Lowest price: ", padx= 10)
# row4
empty_row3 = Label(text="")
add_btn = Button(width = 8, text="Add")
add_btn.bind("<Button-1>", lambda event:add_to_sql())
url_label = Label(text="URL: ", padx= 10, wraplength=650)
url_label.bind("<Button-1>", lambda event:open_url())
# row5
info_label = Label(text="", fg= "red", font=25)
# row6
selected_input_entry= Entry(window, width= 30)
selected_name_entry = Entry(window, width= 30)
selected_price_entry = Entry(window, width= 30)
selected_url_entry= Entry(window, width= 30)
selected_time_entry = Entry(window, width= 30)
# row7 tree
tree = ttk.Treeview(window, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=20, selectmode='browse')
tree.bind("<Button-1>", selectItem)
tree.column("# 1", anchor=CENTER, width=4)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=W)
tree.heading("# 2", text="Input")
tree.column("# 3", anchor=W, width=450)
tree.heading("# 3", text="Name")
tree.column("# 4", anchor=CENTER, width=80)
tree.heading("# 4", text="Price")
tree.column("# 5", anchor=W, width=450)
tree.heading("# 5", text="URL")
tree.column("# 6", anchor=CENTER)
tree.heading("# 6", text="Created")
# ------------------------
# row2 config
empty_row.grid(row=1, column=1)
input_label.grid(row=2, column=1, sticky=E)
input_entry.grid(row=2, column=2)
search_btn.grid(row=2, column=3)
name_label.grid(row=2, column=4, sticky=W)

image_label.grid(rowspan=4, column=6)
ico_label.grid(row=7, column=6)
# row3 config
empty_row2.grid(row=3, column=1)
remove_label.grid(row=4, column=1, sticky=E)
remove_entry.grid(row=4, column=2)
remove_btn.grid(row=4, column=3)
price_label.grid(row=4, column=4, sticky=W)
# row4 config
empty_row3.grid(row=5, column=2)
add_btn.grid(row=6, column=3)
url_label.grid(row=6, column=4, sticky=W)
# row5 config
info_label.grid(row=7, columnspan=5)
# row6 config
selected_input_entry.grid(row=8, column=1)
selected_name_entry.grid(row=8, column=2)
selected_price_entry.grid(row=8, column=3)
selected_url_entry.grid(row=9, column=1)
selected_time_entry.grid(row=9, column=3)
# row7 config
tree.grid(row=10, columnspan=100,sticky=E+W)

refresh()
window.mainloop()