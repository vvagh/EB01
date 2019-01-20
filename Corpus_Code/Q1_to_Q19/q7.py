import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0678 = open("WP_tables/tables_redi2_1/re_tables-0678.json", "r")
sourceFile_0592 = open("WP_tables/tables_redi2_1/re_tables-0592.json", "r")
sourceFile_0155 = open("WP_tables/tables_redi2_1/re_tables-0155.json", "r")
sourceFile_0033 = open("WP_tables/tables_redi2_1/re_tables-0033.json", "r")
sourceFile_0266 = open("WP_tables/tables_redi2_1/re_tables-0266.json", "r")
sourceFile_0406 = open("WP_tables/tables_redi2_1/re_tables-0406.json", "r")
sourceFile_0291 = open("WP_tables/tables_redi2_1/re_tables-0291.json", "r")
sourceFile_0367 = open("WP_tables/tables_redi2_1/re_tables-0367.json", "r")
sourceFile_1582 = open("WP_tables/tables_redi2_1/re_tables-1582.json", "r")
sourceFile_1417 = open("WP_tables/tables_redi2_1/re_tables-1417.json", "r")
sourceFile_1056 = open("WP_tables/tables_redi2_1/re_tables-1056.json", "r")
sourceFile_1492 = open("WP_tables/tables_redi2_1/re_tables-1492.json", "r")
sourceFile_0453 = open("WP_tables/tables_redi2_1/re_tables-0453.json", "r")
sourceFile_1485 = open("WP_tables/tables_redi2_1/re_tables-1485.json", "r")
sourceFile_0127 = open("WP_tables/tables_redi2_1/re_tables-0127.json", "r")
sourceFile_0048 = open("WP_tables/tables_redi2_1/re_tables-0048.json", "r")
sourceFile_1219 = open("WP_tables/tables_redi2_1/re_tables-1219.json", "r")

# Loading the source files specified above
json_data_0678 = json.load(sourceFile_0678)
json_data_0592 = json.load(sourceFile_0592)
json_data_0155 = json.load(sourceFile_0155)
json_data_0033 = json.load(sourceFile_0033)
json_data_0266 = json.load(sourceFile_0266)
json_data_0406 = json.load(sourceFile_0406)
json_data_0291 = json.load(sourceFile_0291)
json_data_0367 = json.load(sourceFile_0367)
json_data_1582 = json.load(sourceFile_1582)
json_data_1417 = json.load(sourceFile_1417)
json_data_1056 = json.load(sourceFile_1056)
json_data_1492 = json.load(sourceFile_1492)
json_data_0453 = json.load(sourceFile_0453)
json_data_1485 = json.load(sourceFile_1485)
json_data_0127 = json.load(sourceFile_0127)
json_data_0048 = json.load(sourceFile_0048)
json_data_1219 = json.load(sourceFile_1219)

# Top 20 table IDs for Query 1
t1 = json_data_0678["table-0678-625"]
t2 = json_data_0678["table-0678-627"]
t3 = json_data_0592["table-0592-701"]
t4 = json_data_0155["table-0155-146"]
t5 = json_data_0033["table-0033-959"]
t6 = json_data_0266["table-0266-218"]
t7 = json_data_0406["table-0406-281"]
t8 = json_data_0291["table-0291-159"]
t9 = json_data_0367["table-0367-173"]
t10 = json_data_1582["table-1582-619"]
t11 = json_data_1417["table-1417-774"]
t12 = json_data_1056["table-1056-349"]
t13 = json_data_1492["table-1492-675"]
t14 = json_data_0453["table-0453-280"]
t15 = json_data_1485["table-1485-305"]
t16 = json_data_0127["table-0127-274"]
t17 = json_data_0048["table-0048-583"]
t18 = json_data_1219["table-1219-416"]
t19 = json_data_0048["table-0048-585"]
t20 = json_data_0048["table-0048-575"]

d = {}
d["table-0678-625"] = t1
d["table-0678-627"] = t2
d["table-0592-701"] = t3
d["table-0155-146"] = t4
d["table-0033-959"] = t5
d["table-0266-218"] = t6
d["table-0406-281"] = t7
d["table-0291-159"] = t8
d["table-0367-173"] = t9
d["table-1582-619"] = t10
d["table-1417-774"] = t11
d["table-1056-349"] = t12
d["table-1492-675"] = t13
d["table-0453-280"] = t14
d["table-1485-305"] = t15
d["table-0127-274"] = t16
d["table-0048-583"] = t17
d["table-1219-416"] = t18
d["table-0048-585"] = t19
d["table-0048-575"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_7.json', 'w') as f:
    json.dump(d, f)
