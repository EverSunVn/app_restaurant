import json
import os

# =================
# CLASS
# =================

class Dishes:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        

class Table:
    def __init__(self, table_number ,state):
        self._table_number = table_number
        self.state = state

    # ====================================

    @property
    def table_number(self):
        return self._table_number

    @table_number.setter
    def table_number(self, value):
        if not value<=0:
            raise ValueError("Table number must be greater than 0")
        self._table_number = value
        
     # ====================================


class Bill:
    def __init__(self, table_number):
        self.id = table_number
        self.dishes_list = []
        self.total_money = 0

# =================
# JSON LOGIC
# =================

DISHES_DATA = {}
TABLE_DATA = {}
BILL_DATA = {}

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'data.json')

try:
    with open(file_path, "r", encoding="utf-8") as file:
        data_file = json.load(file)

    print("File data =", data_file)

except FileNotFoundError:
    print("Error: 'data.json' file was not found.")

for table_number, obj in data_file['tables'].items():
    TABLE_DATA[int(table_number)] = Table(int(table_number), obj["state"])

for dishID, obj in data_file['dishes'].items():
    DISHES_DATA[dishID] = Dishes(obj["name"], obj["cost"])


# ==========================================
# DATA GETTING FUNCTION (LẤY HÀM CƠ BẢN)
# ==========================================
def get_free_tables(): # Lấy bàn trống
    tables = []
    for table_number, table in TABLE_DATA.items():
        if table.state == True:
            tables.append(table_number)
    return tables

def get_occupied_tables(): # Lấy bàn không trống
    tables = []
    for table_number, table in TABLE_DATA.items():
            if table.state == False:
                tables.append(table_number)
    return tables

def get_dish(dishID): # Lấy món ăn
    return DISHES_DATA.get(dishID)

def get_table(table_number): # Lấy bàn
    return TABLE_DATA.get(table_number)

def open_table(table_number) -> tuple[bool, str]: # Mở bàn
    table = TABLE_DATA.get(table_number)
    if table is None:
        return False, "This table is not available!"
    if table.state == False:
        return False, "This table is occupied!"
        
    table.state = False
    return True, "This table is successfully opened!"

def close_table(table_number): # Đóng bàn
    table = TABLE_DATA.get(table_number)
    if table is not None:
        table.state = True
        
    if table.id in BILL_DATA:
        del BILL_DATA[table_number]

def get_bill(table_number): # Lấy Bill
    if table_number not in BILL_DATA:
        BILL_DATA[table_number] = Bill(table_number)

    return BILL_DATA[table_number]
