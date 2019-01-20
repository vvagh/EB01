import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0791 = open("WP_tables/tables_redi2_1/re_tables-0791.json", "r")
sourceFile_1091 = open("WP_tables/tables_redi2_1/re_tables-1091.json", "r")
sourceFile_1387 = open("WP_tables/tables_redi2_1/re_tables-1387.json", "r")
sourceFile_1384 = open("WP_tables/tables_redi2_1/re_tables-1384.json", "r")
sourceFile_0152 = open("WP_tables/tables_redi2_1/re_tables-0152.json", "r")
sourceFile_0384 = open("WP_tables/tables_redi2_1/re_tables-0384.json", "r")
sourceFile_0512 = open("WP_tables/tables_redi2_1/re_tables-0512.json", "r")
sourceFile_0984 = open("WP_tables/tables_redi2_1/re_tables-0984.json", "r")
sourceFile_1398 = open("WP_tables/tables_redi2_1/re_tables-1398.json", "r")
sourceFile_0921 = open("WP_tables/tables_redi2_1/re_tables-0921.json", "r")
sourceFile_1462 = open("WP_tables/tables_redi2_1/re_tables-1462.json", "r")

# Loading the source files specified above
json_data_0791 = json.load(sourceFile_0791)
json_data_1091 = json.load(sourceFile_1091)
json_data_1387 = json.load(sourceFile_1387)
json_data_1384 = json.load(sourceFile_1384)
json_data_0152 = json.load(sourceFile_0152)
json_data_0384 = json.load(sourceFile_0384)
json_data_0512 = json.load(sourceFile_0512)
json_data_0984 = json.load(sourceFile_0984)
json_data_1398 = json.load(sourceFile_1398)
json_data_0921 = json.load(sourceFile_0921)
json_data_1462 = json.load(sourceFile_1462)

# Top 20 table IDs for Query 1
t1 = json_data_0791["table-0791-274"]
t2 = json_data_1091["table-1091-421"]
t3 = json_data_1387["table-1387-237"]
t4 = json_data_1384["table-1384-649"]
t5 = json_data_1384["table-1384-651"]
t6 = json_data_1384["table-1384-654"]
t7 = json_data_1384["table-1384-652"]
t8 = json_data_0152["table-0152-596"]
t9 = json_data_0384["table-0384-352"]
t10 = json_data_0384["table-0384-354"]
t11 = json_data_1384["table-1384-653"]
t12 = json_data_0384["table-0384-349"]
t13 = json_data_0384["table-0384-350"]
t14 = json_data_0512["table-0512-745"]
t15 = json_data_0384["table-0384-348"]
t16 = json_data_0384["table-0384-351"]
t17 = json_data_0984["table-0984-275"]
t18 = json_data_1398["table-1398-928"]
t19 = json_data_0921["table-0921-716"]
t20 = json_data_1462["table-1462-369"]

d = {}
d["table-0791-274"] = t1
d["table-1091-421"] = t2
d["table-1387-237"] = t3
d["table-1384-649"] = t4
d["table-1384-651"] = t5
d["table-1384-654"] = t6
d["table-1384-652"] = t7
d["table-0152-596"] = t8
d["table-0384-352"] = t9
d["table-0384-354"] = t10
d["table-1384-653"] = t11
d["table-0384-349"] = t12
d["table-0384-350"] = t13
d["table-0512-745"] = t14
d["table-0384-348"] = t15
d["table-0384-351"] = t16
d["table-0984-275"] = t17
d["table-1398-928"] = t18
d["table-0921-716"] = t19
d["table-1462-369"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_10.json', 'w') as f:
    json.dump(d, f)

d = {}

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_10.json', 'w') as f:
    json.dump(d, f)
