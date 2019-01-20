import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1334=open("WP_tables/tables_redi2_1/re_tables-1334.json", "r")
sourceFile_0709=open("WP_tables/tables_redi2_1/re_tables-0709.json", "r")
sourceFile_0709=open("WP_tables/tables_redi2_1/re_tables-0709.json", "r")
sourceFile_0385=open("WP_tables/tables_redi2_1/re_tables-0385.json", "r")
sourceFile_1333=open("WP_tables/tables_redi2_1/re_tables-1333.json", "r")
sourceFile_0385=open("WP_tables/tables_redi2_1/re_tables-0385.json", "r")
sourceFile_1005=open("WP_tables/tables_redi2_1/re_tables-1005.json", "r")
sourceFile_0385=open("WP_tables/tables_redi2_1/re_tables-0385.json", "r")
sourceFile_0385=open("WP_tables/tables_redi2_1/re_tables-0385.json", "r")
sourceFile_0245=open("WP_tables/tables_redi2_1/re_tables-0245.json", "r")
sourceFile_1508=open("WP_tables/tables_redi2_1/re_tables-1508.json", "r")
sourceFile_1015=open("WP_tables/tables_redi2_1/re_tables-1015.json", "r")
sourceFile_0194=open("WP_tables/tables_redi2_1/re_tables-0194.json", "r")
sourceFile_1647=open("WP_tables/tables_redi2_1/re_tables-1647.json", "r")
sourceFile_1402=open("WP_tables/tables_redi2_1/re_tables-1402.json", "r")
sourceFile_1489=open("WP_tables/tables_redi2_1/re_tables-1489.json", "r")
sourceFile_1356=open("WP_tables/tables_redi2_1/re_tables-1356.json", "r")
sourceFile_0598=open("WP_tables/tables_redi2_1/re_tables-0598.json", "r")
sourceFile_0735=open("WP_tables/tables_redi2_1/re_tables-0735.json", "r")
sourceFile_1015=open("WP_tables/tables_redi2_1/re_tables-1015.json", "r")
# Loading the source files specified above
json_data_1334= json.load(sourceFile_1334)
json_data_0709= json.load(sourceFile_0709)
json_data_0709= json.load(sourceFile_0709)
json_data_0385= json.load(sourceFile_0385)
json_data_1333= json.load(sourceFile_1333)
json_data_0385= json.load(sourceFile_0385)
json_data_1005= json.load(sourceFile_1005)
json_data_0385= json.load(sourceFile_0385)
json_data_0385= json.load(sourceFile_0385)
json_data_0245= json.load(sourceFile_0245)
json_data_1508= json.load(sourceFile_1508)
json_data_1015= json.load(sourceFile_1015)
json_data_0194= json.load(sourceFile_0194)
json_data_1647= json.load(sourceFile_1647)
json_data_1402= json.load(sourceFile_1402)
json_data_1489= json.load(sourceFile_1489)
json_data_1356= json.load(sourceFile_1356)
json_data_0598= json.load(sourceFile_0598)
json_data_0735= json.load(sourceFile_0735)
json_data_1015= json.load(sourceFile_1015)

# Top 20 table IDs for Query 20
t1 =json_data_1334["table-1334-944"]
t2 =json_data_0709["table-0709-586"]
t3 =json_data_0709["table-0709-584"]
t4 =json_data_0385["table-0385-764"]
t5 =json_data_1333["table-1333-198"]
t6 =json_data_0385["table-0385-766"]
t7 =json_data_1005["table-1005-652"]
t8 =json_data_0385["table-0385-765"]
t9 =json_data_0385["table-0385-768"]
t10 =json_data_0245["table-0245-556"]
t11 =json_data_1508["table-1508-914"]
t12 =json_data_1015["table-1015-246"]
t13 =json_data_0194["table-0194-547"]
t14 =json_data_1647["table-1647-305"]
t15 =json_data_1402["table-1402-905"]
t16 =json_data_1489["table-1489-146"]
t17 =json_data_1356["table-1356-222"]
t18 =json_data_0598["table-0598-146"]
t19 =json_data_0735["table-0735-908"]
t20 =json_data_1015["table-1015-247"]		
# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('output.json', 'w') as f:
    json.dump(t1, f)

with open('output.json', 'w') as f:
    json.dump(t2, f)

with open('output.json', 'w') as f:
    json.dump(t3, f)

with open('output.json', 'w') as f:
    json.dump(t4, f)

with open('output.json', 'w') as f:
    json.dump(t5, f)

with open('output.json', 'w') as f:
    json.dump(t6, f)

with open('output.json', 'w') as f:
    json.dump(t7, f)

with open('output.json', 'w') as f:
    json.dump(t8, f)

with open('output.json', 'w') as f:
    json.dump(t9, f)

with open('output.json', 'w') as f:
    json.dump(t10, f)

with open('output.json', 'w') as f:
    json.dump(t11, f)

with open('output.json', 'w') as f:
    json.dump(t12, f)

with open('output.json', 'w') as f:
    json.dump(t13, f)

with open('output.json', 'w') as f:
    json.dump(t14, f)

with open('output.json', 'w') as f:
    json.dump(t15, f)

with open('output.json', 'w') as f:
    json.dump(t16, f)

with open('output.json', 'w') as f:
    json.dump(t17, f)

with open('output.json', 'w') as f:
    json.dump(t18, f)

with open('output.json', 'w') as f:
    json.dump(t19, f)

with open('output.json', 'w') as f:
    json.dump(t20, f)