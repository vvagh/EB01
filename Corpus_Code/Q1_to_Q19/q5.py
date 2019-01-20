import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0452 = open("WP_tables/tables_redi2_1/re_tables-0452.json", "r")
sourceFile_1264 = open("WP_tables/tables_redi2_1/re_tables-1264.json", "r")
sourceFile_0600 = open("WP_tables/tables_redi2_1/re_tables-0600.json", "r")
sourceFile_1530 = open("WP_tables/tables_redi2_1/re_tables-1530.json", "r")
sourceFile_1258 = open("WP_tables/tables_redi2_1/re_tables-1258.json", "r")
sourceFile_1444 = open("WP_tables/tables_redi2_1/re_tables-1444.json", "r")
sourceFile_1513 = open("WP_tables/tables_redi2_1/re_tables-1513.json", "r")
sourceFile_1371 = open("WP_tables/tables_redi2_1/re_tables-1371.json", "r")
sourceFile_0248 = open("WP_tables/tables_redi2_1/re_tables-0248.json", "r")
sourceFile_1421 = open("WP_tables/tables_redi2_1/re_tables-1421.json", "r")
sourceFile_1088 = open("WP_tables/tables_redi2_1/re_tables-1088.json", "r")
sourceFile_1455 = open("WP_tables/tables_redi2_1/re_tables-1455.json", "r")
sourceFile_1599 = open("WP_tables/tables_redi2_1/re_tables-1599.json", "r")
sourceFile_0735 = open("WP_tables/tables_redi2_1/re_tables-0735.json", "r")
sourceFile_1424 = open("WP_tables/tables_redi2_1/re_tables-1424.json", "r")

# Loading the source files specified above
json_data_0452 = json.load(sourceFile_0452)
json_data_1264 = json.load(sourceFile_1264)
json_data_0600 = json.load(sourceFile_0600)
json_data_1530 = json.load(sourceFile_1530)
json_data_1258 = json.load(sourceFile_1258)
json_data_1444 = json.load(sourceFile_1444)
json_data_1513 = json.load(sourceFile_1513)
json_data_1371 = json.load(sourceFile_1371)
json_data_0248 = json.load(sourceFile_0248)
json_data_1421 = json.load(sourceFile_1421)
json_data_1088 = json.load(sourceFile_1088)
json_data_1455 = json.load(sourceFile_1455)
json_data_1599 = json.load(sourceFile_1599)
json_data_0735 = json.load(sourceFile_0735)
json_data_1424 = json.load(sourceFile_1424)

# Top 20 table IDs for Query 1
t1 = json_data_0452["table-0452-375"]
t2 = json_data_1264["table-1264-72"]
t3 = json_data_0600["table-0600-606"]
t4 = json_data_0600["table-0600-604"]
t5 = json_data_0600["table-0600-605"]
t6 = json_data_0600["table-0600-601"]
t7 = json_data_0600["table-0600-600"]
t8 = json_data_1530["table-1530-281"]
t9 = json_data_1258["table-1258-614"]
t10 = json_data_1444["table-1444-333"]
t11 = json_data_1513["table-1513-956"]
t12 = json_data_1371["table-1371-139"]
t13 = json_data_0248["table-0248-862"]
t14 = json_data_1421["table-1421-60"]
t15 = json_data_1088["table-1088-407"]
t16 = json_data_1421["table-1421-59"]
t17 = json_data_1455["table-1455-559"]
t18 = json_data_1599["table-1599-557"]
t19 = json_data_0735["table-0735-615"]
t20 = json_data_1424["table-1424-83"]

d = {}
d["table-0452-375"] = t1
d["table-1264-72"] = t2
d["table-0600-606"] = t3
d["table-0600-604"] = t4
d["table-0600-605"] = t5
d["table-0600-601"] = t6
d["table-0600-600"] = t7
d["table-1530-281"] = t8
d["table-1258-614"] = t9
d["table-1444-333"] = t10
d["table-1513-956"] = t11
d["table-1371-139"] = t12
d["table-0248-862"] = t13
d["table-1421-60"] = t14
d["table-1088-407"] = t15
d["table-1421-59"] = t16
d["table-1455-559"] = t17
d["table-1599-557"] = t18
d["table-0735-615"] = t19
d["table-1424-83"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_5.json', 'w') as f:
    json.dump(d, f)

