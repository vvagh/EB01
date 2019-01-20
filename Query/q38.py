import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1017 = open("WP_tables/tables_redi2_1/re_tables-1017.json", "r")
sourceFile_0520 = open("WP_tables/tables_redi2_1/re_tables-0520.json", "r")
sourceFile_1451 = open("WP_tables/tables_redi2_1/re_tables-1451.json", "r")
sourceFile_0116 = open("WP_tables/tables_redi2_1/re_tables-0116.json", "r")
sourceFile_0403 = open("WP_tables/tables_redi2_1/re_tables-0403.json", "r")
sourceFile_0507 = open("WP_tables/tables_redi2_1/re_tables-0507.json", "r")
sourceFile_1379 = open("WP_tables/tables_redi2_1/re_tables-1379.json", "r")
sourceFile_1650 = open("WP_tables/tables_redi2_1/re_tables-1650.json", "r")
sourceFile_1388 = open("WP_tables/tables_redi2_1/re_tables-1388.json", "r")
sourceFile_1204 = open("WP_tables/tables_redi2_1/re_tables-1204.json", "r")
sourceFile_1292 = open("WP_tables/tables_redi2_1/re_tables-1292.json", "r")
sourceFile_1386 = open("WP_tables/tables_redi2_1/re_tables-1386.json", "r")
sourceFile_1035 = open("WP_tables/tables_redi2_1/re_tables-1035.json", "r")
sourceFile_0001 = open("WP_tables/tables_redi2_1/re_tables-0001.json", "r")
sourceFile_1640 = open("WP_tables/tables_redi2_1/re_tables-1640.json", "r")
sourceFile_0985 = open("WP_tables/tables_redi2_1/re_tables-0985.json", "r")
sourceFile_1205 = open("WP_tables/tables_redi2_1/re_tables-1205.json", "r")
sourceFile_1363 = open("WP_tables/tables_redi2_1/re_tables-1363.json", "r")
sourceFile_1017 = open("WP_tables/tables_redi2_1/re_tables-1017.json", "r")
sourceFile_0571 = open("WP_tables/tables_redi2_1/re_tables-0571.json", "r")

# Loading the source files specified above
json_data_1017= json.load(sourceFile_1017)
json_data_0520= json.load(sourceFile_0520)
json_data_1451= json.load(sourceFile_1451)
json_data_0116= json.load(sourceFile_0116)
json_data_0403= json.load(sourceFile_0403)
json_data_0507= json.load(sourceFile_0507)
json_data_1379= json.load(sourceFile_1379)
json_data_1650= json.load(sourceFile_1650)
json_data_1388= json.load(sourceFile_1388)
json_data_1204= json.load(sourceFile_1204)
json_data_1292= json.load(sourceFile_1292)
json_data_1386= json.load(sourceFile_1386)
json_data_1035= json.load(sourceFile_1035)
json_data_0001= json.load(sourceFile_0001)
json_data_1640= json.load(sourceFile_1640)
json_data_0985= json.load(sourceFile_0985)
json_data_1205= json.load(sourceFile_1205)
json_data_1363= json.load(sourceFile_1363)
json_data_1017= json.load(sourceFile_1017)
json_data_0571= json.load(sourceFile_0571)

# Top 20 table IDs for Query 20
t1 = json_data_1017["table-1017-538"]
t2 = json_data_0520["table-0520-707"]
t3 = json_data_1451["table-1451-328"]
t4 = json_data_0116["table-0116-212"]
t5 = json_data_0403["table-0403-805"]
t6 = json_data_0507["table-0507-56"]
t7 = json_data_1379["table-1379-82"]
t8 = json_data_1650["table-1650-920"]
t9 = json_data_1388["table-1388-470"]
t10 = json_data_1204["table-1204-839"]
t11 = json_data_1292["table-1292-436"]
t12 = json_data_1386["table-1386-110"]
t13 = json_data_1035["table-1035-439"]
t14 = json_data_0001["table-0001-400"]
t15 = json_data_1640["table-1640-953"]
t16 = json_data_0985["table-0985-943"]
t17 = json_data_1205["table-1205-318"]
t18 = json_data_1363["table-1363-588"]
t19 = json_data_1017["table-1017-458"]
t20 = json_data_0571["table-0571-533"]

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