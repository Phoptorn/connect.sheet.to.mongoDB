from pymongo import MongoClient

# server = "mongodb://root:example@mongo:27017/"
server = "mongodb://root:example@localhost:27017/" # ใช้ localhost

# server = "mongodb://sirdadmin00:Dsi0800-BTISC@10.59.201.28:27017/"

# conn_pf_users = MongoClient(server).RD_Platform.Platform_Users
# conn_pf_log_auth = MongoClient(server).RD_Platform.Platform_Log_Auth
conn_pf_bots = MongoClient(server).RD_Platform.Platform_Bots #เทสด้วยการดึงข้อมูล platform_bots มาดู
# conn_pf_conver = MongoClient(server).RD_Platform.Platform_Conversations

# ##### dev for test_cursor #####
# conn_pf_cursor = MongoClient(server).test.cursor

# ##### dev for test_heroes #####
# conn_pf_heroes = MongoClient(server).test.heroes

##### dev for test googlesheet #####
conn_pf_sheets = MongoClient(server).RD_Platform.Platform_Training

# server_temp = "mongodb://root:example@10.59.201.28:27017/"
# conn_srv_temp = MongoClient(server_temp).RD_Platform.Platform_Users

# local = "mongodb://root:example@mongo:27017/"
# conn_loc = MongoClient(local).TestDB.Users


# conn = conn_pf_users 
