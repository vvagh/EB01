import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0891 = open("WP_tables/tables_redi2_1/re_tables-0891.json", "r")
sourceFile_1016 = open("WP_tables/tables_redi2_1/re_tables-1016.json", "r")
sourceFile_0362 = open("WP_tables/tables_redi2_1/re_tables-0362.json", "r")
sourceFile_0179 = open("WP_tables/tables_redi2_1/re_tables-0179.json", "r")
sourceFile_1579 = open("WP_tables/tables_redi2_1/re_tables-1579.json", "r")
sourceFile_0028 = open("WP_tables/tables_redi2_1/re_tables-0028.json", "r")
sourceFile_1622 = open("WP_tables/tables_redi2_1/re_tables-1622.json", "r")
sourceFile_1627 = open("WP_tables/tables_redi2_1/re_tables-1627.json", "r")
sourceFile_1256 = open("WP_tables/tables_redi2_1/re_tables-1256.json", "r")
sourceFile_1383 = open("WP_tables/tables_redi2_1/re_tables-1383.json", "r")
sourceFile_0265 = open("WP_tables/tables_redi2_1/re_tables-0265.json", "r")
sourceFile_1423 = open("WP_tables/tables_redi2_1/re_tables-1423.json", "r")
sourceFile_1479 = open("WP_tables/tables_redi2_1/re_tables-1479.json", "r")
sourceFile_0951 = open("WP_tables/tables_redi2_1/re_tables-0951.json", "r")
sourceFile_0313 = open("WP_tables/tables_redi2_1/re_tables-0313.json", "r")
sourceFile_1283 = open("WP_tables/tables_redi2_1/re_tables-1283.json", "r")
sourceFile_1518 = open("WP_tables/tables_redi2_1/re_tables-1518.json", "r")

# Loading the source files specified above
json_data_0891 = json.load(sourceFile_0891)
json_data_1016 = json.load(sourceFile_1016)
json_data_0362 = json.load(sourceFile_0362)
json_data_0179 = json.load(sourceFile_0179)
json_data_1579 = json.load(sourceFile_1579)
json_data_0028 = json.load(sourceFile_0028)
json_data_1622 = json.load(sourceFile_1622)
json_data_1627 = json.load(sourceFile_1627)
json_data_1256 = json.load(sourceFile_1256)
json_data_1383 = json.load(sourceFile_1383)
json_data_0265 = json.load(sourceFile_0265)
json_data_1423 = json.load(sourceFile_1423)
json_data_1479 = json.load(sourceFile_1479)
json_data_0951 = json.load(sourceFile_0951)
json_data_0313 = json.load(sourceFile_0313)
json_data_1283 = json.load(sourceFile_1283)
json_data_1518 = json.load(sourceFile_1518)

t1 = json_data_0891["table-0891-868"]
t2 = json_data_0891["table-0891-869"]
t3 = json_data_1016["table-1016-927"]
t4 = json_data_0362["table-0362-968"]
t5 = json_data_0179["table-0179-26"]
t6 = json_data_1579["table-1579-543"]
t7 = json_data_0028["table-0028-393"]
t8 = json_data_1622["table-1622-305"]
t9 = json_data_1627["table-1627-735"]
t10 = json_data_1256["table-1256-358"]
t11 = json_data_1383["table-1383-130"]
t12 = json_data_0265["table-0265-529"]
t13 = json_data_1423["table-1423-213"]
t14 = json_data_1479["table-1479-56"]
t15 = json_data_1479["table-1479-55"]
t16 = json_data_0951["table-0951-285"]
t17 = json_data_0313["table-0313-781"]
t18 = json_data_0951["table-0951-286"]
t19 = json_data_1283["table-1283-492"]
t20 = json_data_1518["table-1518-448"]

d = {}
d["table-0891-868"] = t1
d["table-0891-869"] = t2
d["table-1016-927"] = t3
d["table-0362-968"] = t4
d["table-0179-26"] = t5
d["table-1579-543"] = t6
d["table-0028-393"] = t7
d["table-1622-305"] = t8
d["table-1627-735"] = t9
d["table-1256-358"] = t10
d["table-1383-130"] = t11
d["table-0265-529"] = t12
d["table-1423-213"] = t13
d["table-1479-56"] = t14
d["table-1479-55"] = t15
d["table-0951-285"] = t16
d["table-0313-781"] = t17
d["table-0951-286"] = t18
d["table-1283-492"] = t19
d["table-1518-448"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_11.json', 'w') as f:
    json.dump(d, f)
