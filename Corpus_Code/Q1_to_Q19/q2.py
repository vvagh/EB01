import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1408 = open("WP_tables/tables_redi2_1/re_tables-1408.json", "r")
sourceFile_1552 = open("WP_tables/tables_redi2_1/re_tables-1552.json", "r")
sourceFile_0346 = open("WP_tables/tables_redi2_1/re_tables-0346.json", "r")
sourceFile_1578 = open("WP_tables/tables_redi2_1/re_tables-1578.json", "r")
sourceFile_0654 = open("WP_tables/tables_redi2_1/re_tables-0654.json", "r")
sourceFile_0391 = open("WP_tables/tables_redi2_1/re_tables-0391.json", "r")
sourceFile_1600 = open("WP_tables/tables_redi2_1/re_tables-1600.json", "r")
sourceFile_1047 = open("WP_tables/tables_redi2_1/re_tables-1047.json", "r")
sourceFile_0406 = open("WP_tables/tables_redi2_1/re_tables-0406.json", "r")
sourceFile_1621 = open("WP_tables/tables_redi2_1/re_tables-1621.json", "r")
sourceFile_0223 = open("WP_tables/tables_redi2_1/re_tables-0223.json", "r")
sourceFile_0517 = open("WP_tables/tables_redi2_1/re_tables-0517.json", "r")
sourceFile_0562 = open("WP_tables/tables_redi2_1/re_tables-0562.json", "r")
sourceFile_1574 = open("WP_tables/tables_redi2_1/re_tables-1574.json", "r")
sourceFile_1564 = open("WP_tables/tables_redi2_1/re_tables-1564.json", "r")
sourceFile_0331 = open("WP_tables/tables_redi2_1/re_tables-0331.json", "r")
sourceFile_0938 = open("WP_tables/tables_redi2_1/re_tables-0938.json", "r")


# Loading the source files specified above
json_data_1408 = json.load(sourceFile_1408)
json_data_1552 = json.load(sourceFile_1552)
json_data_0346 = json.load(sourceFile_0346)
json_data_1578 = json.load(sourceFile_1578)
json_data_0654 = json.load(sourceFile_0654)
json_data_0391 = json.load(sourceFile_0391)
json_data_1600 = json.load(sourceFile_1600)
json_data_1047 = json.load(sourceFile_1047)
json_data_0406 = json.load(sourceFile_0406)
json_data_1621 = json.load(sourceFile_1621)
json_data_0223 = json.load(sourceFile_0223)
json_data_0517 = json.load(sourceFile_0517)
json_data_0562 = json.load(sourceFile_0562)
json_data_1574 = json.load(sourceFile_1574)
json_data_1564 = json.load(sourceFile_1564)
json_data_0331 = json.load(sourceFile_0331)
json_data_0938 = json.load(sourceFile_0938)

# Top 20 table IDs for Query 1
t1 = json_data_1408["table-1408-874"]
t2 = json_data_1408["table-1408-869"]
t3 = json_data_1552["table-1552-729"]
t4 = json_data_1408["table-1408-870"]
t5 = json_data_1408["table-1408-871"]
t6 = json_data_0346["table-0346-14"]
t7 = json_data_1578["table-1578-197"]
t8 = json_data_0654["table-0654-76"]
t9 = json_data_0391["table-0391-689"]
t10 = json_data_1600["table-1600-861"]
t11 = json_data_1047["table-1047-153"]
t12 = json_data_0406["table-0406-134"]
t13 = json_data_1621["table-1621-634"]
t14 = json_data_0223["table-0223-179"]
t15 = json_data_0517["table-0517-237"]
t16 = json_data_0562["table-0562-150"]
t17 = json_data_1574["table-1574-263"]
t18 = json_data_1564["table-1564-439"]
t19 = json_data_0331["table-0331-42"]
t20 = json_data_0938["table-0938-613"]

d = {}
d["table-1408-874"] = t1
d["table-1408-869"] = t2
d["table-1552-729"] = t3
d["table-1408-870"] = t4
d["table-1408-871"] = t5
d["table-0346-14"] = t6
d["table-1578-197"] = t7
d["table-0654-76"] = t8
d["table-0391-689"] = t9
d["table-1600-861"] = t10
d["table-1047-153"] = t11
d["table-0406-134"] = t12
d["table-1621-634"] = t13
d["table-0223-179"] = t14
d["table-0517-237"] = t15
d["table-0562-150"] = t16
d["table-1574-263"] = t17
d["table-1564-439"] = t18
d["table-0331-42"] = t19
d["table-0938-613"] = t20


# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_2.json', 'w') as f:
    json.dump(d, f)
