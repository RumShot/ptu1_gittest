from tkinter import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from tkinter import ttk
from sql_data_base import PriceAnalyzer
import controller

engine = create_engine('sqlite:///price_analyzer/search_history.db')
Session = sessionmaker(bind=engine)
session = Session()

# customer_data = PriceAnalyzer(sql_input="Plokste", sql_name="NVidea", sql_price="555.69", sql_url = "www.randomss.com")
# session.add(customer_data)
# session.commit()

def refresh():
    children = tree.get_children()
    for child in children:
        tree.delete(child)
    read_all = session.query(PriceAnalyzer).all()
    for single_read in read_all:
        tree.insert('', 'end', text="1", values=single_read)

def search_button():
    text_in_search = input_entry.get()
    print(text_in_search)
    final_product = controller.searcher()
    lowest_name = final_product[0]
    lowest_price = final_product[1]
    lowest_url = final_product[2]
    lowest_img = final_product[3]
    lowest_ico = final_product[4]
    name_label['text']=f"Name: {lowest_name}"
    price_label['text']=f"Price: {lowest_price}"
    print(lowest_url)

def remove_id():
    selected_id = remove_entry.get()
    if selected_id.isdigit():
        read_data = session.query(PriceAnalyzer).get(selected_id)
        session.delete(read_data)
        remove_entry.delete(0, 'end')
        session.commit()
        refresh()

window = Tk()
window.title('Lowest Price Analyzer')
window.geometry("901x450")

tree_style = ttk.Style()
tree_style.theme_use('clam')

frame = Frame(window)
# row2
empty_row = Label(text="")
input_label = Label(text="Input Model")
input_entry = Entry(window)
search_btn = Button(width = 8, text="Search")
search_btn.bind("<Button-1>", lambda event: search_button())
name_label = Label(text="Name:", padx= 10)
# row3
empty_row2 = Label(text="")
remove_label = Label(text="ID")
remove_entry = Entry(window)
remove_btn = Button(width = 8, text="Remove")
remove_btn.bind("<Button-1>", lambda event: remove_id())
price_label = Label(text="Price:", padx= 10)
# row4
empty_row3 = Label(text="")
add_btn = Button(width = 8, text="Add")
# row5
info_label = Label(text="info")
# row6 tree
tree = ttk.Treeview(window, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=20,selectmode='extended')

tree.column("# 1", anchor=CENTER, width=4)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=W)
tree.heading("# 2", text="Input")
tree.column("# 3", anchor=W)
tree.heading("# 3", text="Name")
tree.column("# 4", anchor=CENTER, width=80)
tree.heading("# 4", text="Price")
tree.column("# 5", anchor=W)
tree.heading("# 5", text="URL")
tree.column("# 6", anchor=CENTER)
tree.heading("# 6", text="Created")
# tree data insert

# ------------------------
# row2
empty_row.grid(row=1, column=1)
input_label.grid(row=2, column=1, sticky=W)
input_entry.grid(row=2, column=3)
search_btn.grid(row=2, column=4, sticky=E)
name_label.grid(row=2, column=6)
# row3
empty_row2.grid(row=3, column=1)
remove_label.grid(row=4, column=1)
remove_entry.grid(row=4, column=3)
remove_btn.grid(row=4, column=4, sticky=E)
price_label.grid(row=4, column=6)
# row4
empty_row3.grid(row=5, column=2)
add_btn.grid(row=6, column=4, sticky=E)
# row5
info_label.grid(row=7, column=6)
# row6
tree.grid(row=8, columnspan=18,sticky=E+W)

refresh()
window.mainloop()