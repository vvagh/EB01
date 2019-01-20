import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0370 = open("WP_tables/tables_redi2_1/re_tables-0370.json", "r")
sourceFile_1020 = open("WP_tables/tables_redi2_1/re_tables-1020.json", "r")
sourceFile_0037 = open("WP_tables/tables_redi2_1/re_tables-0037.json", "r")
sourceFile_0255 = open("WP_tables/tables_redi2_1/re_tables-0255.json", "r")
sourceFile_1000 = open("WP_tables/tables_redi2_1/re_tables-1000.json", "r")
sourceFile_1042 = open("WP_tables/tables_redi2_1/re_tables-1042.json", "r")
sourceFile_1402 = open("WP_tables/tables_redi2_1/re_tables-1402.json", "r")
sourceFile_1423 = open("WP_tables/tables_redi2_1/re_tables-1423.json", "r")
sourceFile_0730 = open("WP_tables/tables_redi2_1/re_tables-0730.json", "r")
sourceFile_0914 = open("WP_tables/tables_redi2_1/re_tables-0914.json", "r")
sourceFile_0552 = open("WP_tables/tables_redi2_1/re_tables-0552.json", "r")
sourceFile_0464 = open("WP_tables/tables_redi2_1/re_tables-0464.json", "r")
sourceFile_0904 = open("WP_tables/tables_redi2_1/re_tables-0904.json", "r")
sourceFile_0216 = open("WP_tables/tables_redi2_1/re_tables-0216.json", "r")
sourceFile_0554 = open("WP_tables/tables_redi2_1/re_tables-0554.json", "r")
sourceFile_1391 = open("WP_tables/tables_redi2_1/re_tables-1391.json", "r")
sourceFile_0063 = open("WP_tables/tables_redi2_1/re_tables-0063.json", "r")

# Loading the source files specified above
json_data_0370 = json.load(sourceFile_0370)
json_data_1020 = json.load(sourceFile_1020)
json_data_0037 = json.load(sourceFile_0037)
json_data_0255 = json.load(sourceFile_0255)
json_data_1000 = json.load(sourceFile_1000)
json_data_1042 = json.load(sourceFile_1042)
json_data_1402 = json.load(sourceFile_1402)
json_data_1423 = json.load(sourceFile_1423)
json_data_0730 = json.load(sourceFile_0730)
json_data_0914 = json.load(sourceFile_0914)
json_data_0552 = json.load(sourceFile_0552)
json_data_0464 = json.load(sourceFile_0464)
json_data_0904 = json.load(sourceFile_0904)
json_data_0216 = json.load(sourceFile_0216)
json_data_0554 = json.load(sourceFile_0554)
json_data_1391 = json.load(sourceFile_1391)
json_data_0063 = json.load(sourceFile_0063)

# Top 20 table IDs for Query 1
t1 = json_data_0370["table-0370-614"]
t2 = json_data_1020["table-1020-619"]
t3 = json_data_0037["table-0037-411"]
t4 = json_data_0255["table-0255-236"]
t5 = json_data_1000["table-1000-57"]
t6 = json_data_1042["table-1042-895"]
t7 = json_data_1402["table-1402-139"]
t8 = json_data_1423["table-1423-774"]
t9 = json_data_0730["table-0730-168"]
t10 = json_data_0914["table-0914-101"]
t11 = json_data_0914["table-0914-103"]
t12 = json_data_0552["table-0552-510"]
t13 = json_data_0464["table-0464-505"]
t14 = json_data_0552["table-0552-511"]
t15 = json_data_0904["table-0904-852"]
t16 = json_data_0216["table-0216-976"]
t17 = json_data_0554["table-0554-923"]
t18 = json_data_1391["table-1391-8"]
t19 = json_data_0063["table-0063-827"]
t20 = json_data_0216["table-0216-970"]

d = {}
d["table-0370-614"] = t1
d["table-1020-619"] = t2
d["table-0037-411"] = t3
d["table-0255-236"] = t4
d["table-1000-57"] = t5
d["table-1042-895"] = t6
d["table-1402-139"] = t7
d["table-1423-774"] = t8
d["table-0730-168"] = t9
d["table-0914-101"] = t10
d["table-0914-103"] = t11
d["table-0552-510"] = t12
d["table-0464-505"] = t13
d["table-0552-511"] = t14
d["table-0904-852"] = t15
d["table-0216-976"] = t16
d["table-0554-923"] = t17
d["table-1391-8"] = t18
d["table-0063-827"] = t19
d["table-0216-970"] = t20


# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_1.json', 'w') as f:
    json.dump(d, f)
