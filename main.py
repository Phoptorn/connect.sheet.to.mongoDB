import gspread
import os

from schema import Model
from init import connections

cwd = os.getcwd()

client = gspread.service_account(
    filename=f"{cwd}/database/astral-charter-361607-8f3da3c68253.json"
)
sh = client.open_by_key("1GVsX4DUEFNYCqvnZfM8Xe2SF8Wrq3Q95P2QLeBZ_08k")
worksheet = sh.worksheet("data")

###### get_all_values gives a list of rows. ######
rows = worksheet.get_all_values()
rows.pop(0)
print(rows[0])

data = []
for row in rows:
    result = Model(
        bot_id="62f9bbca33a56207edf3f460",
        chat_req_msg=str(row[1]),
        Conversation_Name=str(row[0]),
        status_training={
            "select_Conversation_Name": str(row[0]),
            "add_to_Conversation": False,
            "add_to_Default": False,
            "delete": False,
        },
    )
    data.append(dict(result))

data2 = connections.conn_pf_bots.find()
x = connections.conn_pf_sheets.insert_many(data)
