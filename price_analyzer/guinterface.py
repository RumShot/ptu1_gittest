from tkinter import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tkinter import ttk
from sql_data_base import PriceAnalyzer
import controller
import kaina24
import webbrowser


engine = create_engine('sqlite:///price_analyzer/search_history.db')
Session = sessionmaker(bind=engine)
session = Session()

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
        tree.insert('', 'end', text="", values= (single_read, tree_input[0], tree_name[0],tree_price[0], tree_url[0], tree_time[0],))

# 210-AWVO   u2720q
def search_button():
    search_model = input_entry.get()
    print(search_model)
    kaina24.model_search(search_model)
    final_product = controller.searcher()
    lowest_name = final_product[0]
    lowest_price = final_product[1]
    lowest_url = final_product[2]
    lowest_img = final_product[3]
    lowest_ico = final_product[4]
    name_label['text']=f"Name: {lowest_name}"
    price_label['text']=f"Lowest price:  {lowest_price}"
    url_label['text']=f"URL: {lowest_url}"

def remove_id():
    selected_id = remove_entry.get()
    if selected_id.isdigit():
        read_data = session.query(PriceAnalyzer).get(selected_id)
        session.delete(read_data)
        remove_entry.delete(0, 'end')
        session.commit()
        refresh()

def add_to_sql():
    from_input = input_entry.get()
    from_name = name_label.cget("text")[6:]
    from_price = price_label.cget("text")[15:]
    from_url = url_label.cget("text")[5:]
    to_sql_data = PriceAnalyzer(from_input, from_name, from_price, from_url)
    session.add(to_sql_data)
    session.commit()
    input_entry.delete(0, 'end')
    refresh()

def open_url():
    open_link = url_label.cget("text")[5:][:-2]
    webbrowser.open_new_tab(open_link)

window = Tk()
window.title('Lowest Price Analyzer')
window.geometry("1210x450")

tree_style = ttk.Style()
tree_style.theme_use('clam')

frame = Frame(window)
# row2
empty_row = Label(text="")
input_label = Label(text="Input Model")
input_entry = Entry(window, width= 30)
search_btn = Button(width = 8, text="Search")
search_btn.bind("<Button-1>", lambda event: search_button())
name_label = Label(text="Name: ", padx= 10)
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
url_label = Label(text="URL: ", padx= 10, )
url_label.bind("<Button-1>", lambda event:open_url())
# row5
info_label = Label(text="info")
# row6 tree
tree = ttk.Treeview(window, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=20, selectmode='extended')

tree.column("# 1", anchor=CENTER, width=4)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=W)
tree.heading("# 2", text="Input")
tree.column("# 3", anchor=W, width=350)
tree.heading("# 3", text="Name")
tree.column("# 4", anchor=CENTER, width=80)
tree.heading("# 4", text="Price")
tree.column("# 5", anchor=W, width=350)
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
name_label.grid(row=2, column=5, sticky=W)
# row3
empty_row2.grid(row=3, column=1)
remove_label.grid(row=4, column=1)
remove_entry.grid(row=4, column=3)
remove_btn.grid(row=4, column=4, sticky=E)
price_label.grid(row=4, column=5, sticky=W)
# row4
empty_row3.grid(row=5, column=2)
add_btn.grid(row=6, column=4, sticky=E)
url_label.grid(row=6, column=5, sticky=W)
# row5
info_label.grid(row=7, column=5)
# row6
tree.grid(row=8, columnspan=20,sticky=E+W)

refresh()
window.mainloop()