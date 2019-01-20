import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0354 = open("WP_tables/tables_redi2_1/re_tables-0354.json", "r")
sourceFile_0370 = open("WP_tables/tables_redi2_1/re_tables-0370.json", "r")
sourceFile_1281 = open("WP_tables/tables_redi2_1/re_tables-1281.json", "r")
sourceFile_1579 = open("WP_tables/tables_redi2_1/re_tables-1579.json", "r")
sourceFile_0503 = open("WP_tables/tables_redi2_1/re_tables-0503.json", "r")
sourceFile_0896 = open("WP_tables/tables_redi2_1/re_tables-0896.json", "r")
sourceFile_1392 = open("WP_tables/tables_redi2_1/re_tables-1392.json", "r")
sourceFile_0534 = open("WP_tables/tables_redi2_1/re_tables-0534.json", "r")
sourceFile_1350 = open("WP_tables/tables_redi2_1/re_tables-1350.json", "r")
sourceFile_0352 = open("WP_tables/tables_redi2_1/re_tables-0352.json", "r")
sourceFile_1277 = open("WP_tables/tables_redi2_1/re_tables-1277.json", "r")
sourceFile_1250 = open("WP_tables/tables_redi2_1/re_tables-1250.json", "r")
sourceFile_1647 = open("WP_tables/tables_redi2_1/re_tables-1647.json", "r")
sourceFile_1621 = open("WP_tables/tables_redi2_1/re_tables-1621.json", "r")
sourceFile_1317 = open("WP_tables/tables_redi2_1/re_tables-1317.json", "r")
sourceFile_0833 = open("WP_tables/tables_redi2_1/re_tables-0833.json", "r")
sourceFile_1012 = open("WP_tables/tables_redi2_1/re_tables-1012.json", "r")
sourceFile_0259 = open("WP_tables/tables_redi2_1/re_tables-0259.json", "r")

# Loading the source files specified above
json_data_0354 = json.load(sourceFile_0354)
json_data_0370 = json.load(sourceFile_0370)
json_data_1281 = json.load(sourceFile_1281)
json_data_1579 = json.load(sourceFile_1579)
json_data_0503 = json.load(sourceFile_0503)
json_data_0896 = json.load(sourceFile_0896)
json_data_1392 = json.load(sourceFile_1392)
json_data_0534 = json.load(sourceFile_0534)
json_data_1350 = json.load(sourceFile_1350)
json_data_0352 = json.load(sourceFile_0352)
json_data_1277 = json.load(sourceFile_1277)
json_data_1250 = json.load(sourceFile_1250)
json_data_1647 = json.load(sourceFile_1647)
json_data_1621 = json.load(sourceFile_1621)
json_data_1317 = json.load(sourceFile_1317)
json_data_0833 = json.load(sourceFile_0833)
json_data_1012 = json.load(sourceFile_1012)
json_data_0259 = json.load(sourceFile_0259)

t1 = json_data_0354["table-0354-325"]
t2 = json_data_0370["table-0370-691"]
t3 = json_data_1281["table-1281-687"]
t4 = json_data_1579["table-1579-731"]
t5 = json_data_0503["table-0503-892"]
t6 = json_data_0896["table-0896-9"]
t7 = json_data_1392["table-1392-358"]
t8 = json_data_1579["table-1579-348"]
t9 = json_data_0534["table-0534-18"]
t10 = json_data_1350["table-1350-486"]
t11 = json_data_0352["table-0352-129"]
t12 = json_data_1277["table-1277-865"]
t13 = json_data_1250["table-1250-339"]
t14 = json_data_1647["table-1647-73"]
t15 = json_data_1621["table-1621-415"]
t16 = json_data_1317["table-1317-895"]
t17 = json_data_0833["table-0833-423"]
t18 = json_data_1012["table-1012-862"]
t19 = json_data_1317["table-1317-894"]
t20 = json_data_0259["table-0259-660"]

d = {}
d["table-0354-325"] = t1
d["table-0370-691"] = t2
d["table-1281-687"] = t3
d["table-1579-731"] = t4
d["table-0503-892"] = t5
d["table-0896-9"] = t6
d["table-1392-358"] = t7
d["table-1579-348"] = t8
d["table-0534-18"] = t9
d["table-1350-486"] = t10
d["table-0352-129"] = t11
d["table-1277-865"] = t12
d["table-1250-339"] = t13
d["table-1647-73"] = t14
d["table-1621-415"] = t15
d["table-1317-895"] = t16
d["table-0833-423"] = t17
d["table-1012-862"] = t18
d["table-1317-894"] = t19
d["table-0259-660"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_14.json', 'w') as f:
    json.dump(d, f)
