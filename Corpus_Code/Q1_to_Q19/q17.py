import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0677 = open("WP_tables/tables_redi2_1/re_tables-0677.json", "r")
sourceFile_1027 = open("WP_tables/tables_redi2_1/re_tables-1027.json", "r")
sourceFile_1007 = open("WP_tables/tables_redi2_1/re_tables-1007.json", "r")
sourceFile_0160 = open("WP_tables/tables_redi2_1/re_tables-0160.json", "r")
sourceFile_1258 = open("WP_tables/tables_redi2_1/re_tables-1258.json", "r")
sourceFile_1442 = open("WP_tables/tables_redi2_1/re_tables-1442.json", "r")
sourceFile_0349 = open("WP_tables/tables_redi2_1/re_tables-0349.json", "r")
sourceFile_1365 = open("WP_tables/tables_redi2_1/re_tables-1365.json", "r")
sourceFile_1571 = open("WP_tables/tables_redi2_1/re_tables-1571.json", "r")
sourceFile_0653 = open("WP_tables/tables_redi2_1/re_tables-0653.json", "r")
sourceFile_1216 = open("WP_tables/tables_redi2_1/re_tables-1216.json", "r")

# Loading the source files specified above
json_data_0677 = json.load(sourceFile_0677)
json_data_1027 = json.load(sourceFile_1027)
json_data_1007 = json.load(sourceFile_1007)
json_data_0160 = json.load(sourceFile_0160)
json_data_1258 = json.load(sourceFile_1258)
json_data_1442 = json.load(sourceFile_1442)
json_data_0349 = json.load(sourceFile_0349)
json_data_1365 = json.load(sourceFile_1365)
json_data_1571 = json.load(sourceFile_1571)
json_data_0653 = json.load(sourceFile_0653)
json_data_1216 = json.load(sourceFile_1216)

t1 = json_data_0677["table-0677-684"]
t2 = json_data_1027["table-1027-78"]
t3 = json_data_1027["table-1027-79"]
t4 = json_data_1007["table-1007-884"]
t5 = json_data_0160["table-0160-841"]
t6 = json_data_1258["table-1258-777"]
t7 = json_data_1442["table-1442-99"]
t8 = json_data_1442["table-1442-89"]
t9 = json_data_1442["table-1442-88"]
t10 = json_data_1442["table-1442-90"]
t11 = json_data_0349["table-0349-674"]
t12 = json_data_1442["table-1442-91"]
t13 = json_data_1442["table-1442-78"]
t14 = json_data_1365["table-1365-564"]
t15 = json_data_1442["table-1442-92"]
t16 = json_data_1442["table-1442-96"]
t17 = json_data_1571["table-1571-18"]
t18 = json_data_0653["table-0653-392"]
t19 = json_data_1365["table-1365-563"]
t20 = json_data_1216["table-1216-304"]

d = {}
d["table-0677-684"] = t1
d["table-1027-78"] = t2
d["table-1027-79"] = t3
d["table-1007-884"] = t4
d["table-0160-841"] = t5
d["table-1258-777"] = t6
d["table-1442-99"] = t7
d["table-1442-89"] = t8
d["table-1442-88"] = t9
d["table-1442-90"] = t10
d["table-0349-674"] = t11
d["table-1442-91"] = t12
d["table-1442-78"] = t13
d["table-1365-564"] = t14
d["table-1442-92"] = t15
d["table-1442-96"] = t16
d["table-1571-18"] = t17
d["table-0653-392"] = t18
d["table-1365-563"] = t19
d["table-1216-304"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_17.json', 'w') as f:
    json.dump(d, f)
